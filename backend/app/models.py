# backend/app/models.py

from . import db
from datetime import datetime
from sqlalchemy.dialects.sqlite import JSON  # Using SQLite; adjust for PostgreSQL

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(20))
    phone_number = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(200))
    emergency_contact_name = db.Column(db.String(100))
    emergency_contact_relationship = db.Column(db.String(50))
    emergency_contact_phone = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    calls = db.relationship('Call', backref='patient', lazy=True)

class Call(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    scheduled_time = db.Column(db.DateTime, nullable=True)  # Not used in prototype
    status = db.Column(db.String(20), default='In Progress')  # In Progress, Completed
    report_generated = db.Column(db.Boolean, default=False)
    
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    responses = db.relationship('Response', backref='call', lazy=True)
    
    # Store questions as a JSON list
    questions = db.Column(JSON, nullable=False)

class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    answer = db.Column(db.Text, nullable=False)
    emotional_tone = db.Column(db.String(50))
    
    call_id = db.Column(db.Integer, db.ForeignKey('call.id'), nullable=False)
