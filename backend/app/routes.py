# backend/app/routes.py

from flask import Blueprint, request, jsonify, session
from . import db
from .models import Patient, Call, Response as CallResponse
from .utils import transcribe_speech, analyze_emotional_tone, generate_generative_response
from datetime import datetime
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('api', __name__)

# Initialize JWT
jwt = JWTManager()

def register_jwt(app):
    jwt.init_app(app)

@bp.route('/register', methods=['POST'])
def register():
    """
    Register a new patient.
    Expected JSON payload: {
        "full_name": "John Doe",
        "date_of_birth": "1990-01-01",
        "gender": "Male",
        "phone_number": "1234567890",
        "email": "johndoe@example.com",
        "password": "securepassword",
        "address": "123 Main St",
        "emergency_contact_name": "Jane Doe",
        "emergency_contact_relationship": "Spouse",
        "emergency_contact_phone": "0987654321"
    }
    """
    data = request.get_json()
    required_fields = ["full_name", "date_of_birth", "phone_number", "email", "password"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields."}), 400
    
    if Patient.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already registered."}), 400
    
    if Patient.query.filter_by(phone_number=data['phone_number']).first():
        return jsonify({"error": "Phone number already registered."}), 400
    
    patient = Patient(
        full_name=data['full_name'],
        date_of_birth=datetime.strptime(data['date_of_birth'], "%Y-%m-%d"),
        gender=data.get('gender'),
        phone_number=data['phone_number'],
        email=data['email'],
        address=data.get('address'),
        emergency_contact_name=data.get('emergency_contact_name'),
        emergency_contact_relationship=data.get('emergency_contact_relationship'),
        emergency_contact_phone=data.get('emergency_contact_phone')
    )
    patient.set_password(data['password'])
    db.session.add(patient)
    db.session.commit()
    
    return jsonify({"message": "Registration successful."}), 201

@bp.route('/login', methods=['POST'])
def login():
    """
    Authenticate a patient.
    Expected JSON payload: {
        "email": "johndoe@example.com",
        "password": "securepassword"
    }
    """
    data = request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"error": "Email and password are required."}), 400
    
    patient = Patient.query.filter_by(email=data['email']).first()
    if not patient or not patient.check_password(data['password']):
        return jsonify({"error": "Invalid email or password."}), 401
    
    access_token = create_access_token(identity=patient.id)
    return jsonify({"access_token": access_token}), 200

@bp.route('/start_call', methods=['POST'])
@jwt_required()
def start_call():
    """
    Initialize a new call session and return the first question.
    Expected JSON payload: {}
    """
    patient_id = get_jwt_identity()
    patient = Patient.query.get(patient_id)
    if not patient:
        return jsonify({'error': 'Patient not found.'}), 404
    
    # Define the questionnaire
    questions = [
        {"id": 1, "question": "What is the primary reason for your visit today?"},
        {"id": 2, "question": "When did this issue start? Please provide the date or how long ago."},
        {"id": 3, "question": "Have you experienced this issue before? If yes, please describe."},
        # Add more questions as needed with conditional logic
    ]
    
    # Create a new call entry
    call = Call(
        patient_id=patient.id,
        scheduled_time=None,  # Not used in prototype
        status='In Progress',
        report_generated=False,
        questions=questions
    )
    db.session.add(call)
    db.session.commit()
    
    # Store call_id in session to track the conversation
    session['call_id'] = call.id
    
    # Return the first question
    first_question = questions[0]['question']
    return jsonify({'response': first_question}), 200

@bp.route('/speech', methods=['POST'])
@jwt_required()
def handle_speech():
    """
    Handle incoming speech audio, transcribe it, analyze, and respond with the next question or summary.
    Expects a file upload with key 'file'.
    """
    patient_id = get_jwt_identity()
    call_id = session.get('call_id')
    if not call_id:
        return jsonify({'error': 'No active call session found.'}), 400
    
    call = Call.query.get(call_id)
    if not call or call.patient_id != patient_id:
        return jsonify({'error': 'Call session not found.'}), 404
    
    if 'file' not in request.files:
        return jsonify({'error': 'No audio file provided.'}), 400
    
    file = request.files['file']
    audio_content = file.read()
    
    # Transcribe the speech to text
    transcribed_text = transcribe_speech(audio_content)
    
    # Analyze emotional tone using IBM Watson Tone Analyzer
    emotional_tone = analyze_emotional_tone(transcribed_text)
    
    # Save the response to the database
    current_question = get_current_question(call)
    if not current_question:
        return jsonify({'error': 'No current question found.'}), 400
    
    response_entry = CallResponse(
        call_id=call.id,
        question=current_question['question'],
        answer=transcribed_text,
        emotional_tone=emotional_tone
    )
    db.session.add(response_entry)
    db.session.commit()
    
    # Determine the next question or summary
    next_question = determine_next_question(call, current_question, transcribed_text)
    
    if next_question:
        # Respond with the next question
        return jsonify({'response': next_question['question']}), 200
    else:
        # All questions answered; generate a summary
        summary = generate_summary(call)
        call.status = 'Completed'
        call.report_generated = True
        db.session.commit()
        return jsonify({'response': summary}), 200

def get_current_question(call):
    """
    Retrieve the current question based on the number of responses.
    """
    questions = call.questions
    num_responses = len(call.responses)
    if num_responses < len(questions):
        return questions[num_responses]
    else:
        return None

def determine_next_question(call, current_question, answer):
    """
    Determine the next question based on the current question and answer.
    For simplicity, using a linear flow.
    """
    questions = call.questions
    current_index = next((i for i, q in enumerate(questions) if q['id'] == current_question['id']), None)
    if current_index is not None and current_index + 1 < len(questions):
        return questions[current_index + 1]
    else:
        return None

def generate_summary(call):
    """
    Generate a summary of all responses using the generative AI model.
    """
    responses = call.responses
    summary_text = "Here is a summary of the patient's responses:\n\n"
    for response in responses:
        summary_text += f"Q: {response.question}\nA: {response.answer}\nEmotional Tone: {response.emotional_tone}\n\n"
    
    # Use OpenAI to generate a concise summary
    summary_prompt = f"Generate a concise summary based on the following patient responses:\n\n{summary_text}\n\nSummary:"
    summary = generate_generative_response(summary_prompt)
    
    return summary
