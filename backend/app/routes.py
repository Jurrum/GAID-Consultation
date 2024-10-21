# backend/app/routes.py

from flask import Blueprint, request, jsonify, session
from . import db
from .models import Patient, Call, Response as CallResponse
from .utils import transcribe_speech, analyze_emotional_tone, generate_generative_response
from datetime import datetime

bp = Blueprint('api', __name__)

@bp.route('/start_call', methods=['POST'])
def start_call():
    """
    Initialize a new call session and return the first question.
    Expected JSON payload: { "patient_id": 1 }
    """
    data = request.get_json()
    patient_id = data.get('patient_id')
    
    if not patient_id:
        return jsonify({'error': 'patient_id is required.'}), 400
    
    patient = Patient.query.get(patient_id)
    if not patient:
        return jsonify({'error': 'Patient not found.'}), 404
    
    # Define the questionnaire
    questions = [
        {"id": 1, "question": "What is the primary reason for your visit today?"},
        {"id": 2, "question": "When did this issue start? Please provide the date or how long ago."},
        {"id": 3, "question": "Have you experienced this issue before? If yes, please describe."},
        # Add more questions as needed
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
def handle_speech():
    """
    Handle incoming speech audio, transcribe it, analyze, and respond with the next question or summary.
    Expects a file upload with key 'file'.
    """
    if 'call_id' not in session:
        return jsonify({'error': 'No active call session found.'}), 400
    
    call_id = session['call_id']
    call = Call.query.get(call_id)
    if not call:
        return jsonify({'error': 'Call session not found.'}), 404
    
    if 'file' not in request.files:
        return jsonify({'error': 'No audio file provided.'}), 400
    
    file = request.files['file']
    audio_content = file.read()
    
    # Transcribe the speech to text
    transcribed_text = transcribe_speech(audio_content)
    
    # Analyze emotional tone
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
