# Pre consultation 

""" 
Pre-Consultation Call Script for AI Assistant
1. Call Opener
AI Assistant (Text-to-Speech):

"Hello [Patient's Name], this is an automated call from [Medical Practice Name]. We are conducting a pre-consultation to gather essential information before your upcoming appointment. This will help us better understand your health needs and ensure a more efficient consultation. I will ask you a series of questions, and you can respond verbally. Please answer as accurately as possible. If you need to skip a question or require assistance at any time, please let me know. Shall we begin?"

Wait for patient to respond: "Yes," "Sure," or similar acknowledgment.

2. Patient Information
AI Assistant:

"Great, let's start with some basic information."

Full Name:

"Please say your full name."
[AI listens and records the response]

Date of Birth:

"Please say your date of birth in the format month, day, and year."
[AI listens and records the response]

Gender:

"Please state your gender."
[AI listens and records the response]

Contact Information:

"Please provide your phone number."

[AI listens and records the response]

"Please provide your email address."

[AI listens and records the response]

Address:

"Please say your current address."
[AI listens and records the response]

Emergency Contact:

"Please provide the name of your emergency contact."

[AI listens and records the response]

"What is their relationship to you?"

[AI listens and records the response]

"Please provide their phone number."

[AI listens and records the response]

3. Chief Complaint
Primary Reason for Visit:

"What is the primary reason for your visit today?"
[AI listens and records the response]

Issue Onset:

"When did this issue start? Please provide the date or how long ago."
[AI listens and records the response]

Previous Occurrences:

"Have you experienced this issue before? If yes, please describe."
[AI listens and records the response]

4. Medical History
Chronic Illnesses:

"Do you have any chronic illnesses, such as diabetes or hypertension? Please say 'Yes' or 'No'. If yes, please specify."
[AI listens and records the response]

Surgeries/Hospitalizations:

"Have you had any surgeries or hospitalizations in the past? Please say 'Yes' or 'No'. If yes, please provide details."
[AI listens and records the response]

Mental Health Conditions:

"Do you have any current or past mental health conditions? Please say 'Yes' or 'No'. If yes, please specify."
[AI listens and records the response]

5. Medications
Current Medications:

"Are you currently taking any medications, including prescriptions, over-the-counter drugs, or supplements? Please say 'Yes' or 'No'. If yes, please list all medications and dosages."
[AI listens and records the response]

Recent Medication Changes:

"Have you recently changed any of your medications? Please say 'Yes' or 'No'. If yes, please explain."
[AI listens and records the response]

6. Allergies
Known Allergies:

"Do you have any known allergies, such as to medications, food, or environmental factors? Please say 'Yes' or 'No'. If yes, please list them and describe the reactions."
[AI listens and records the response]

7. Family History
Chronic or Hereditary Conditions:

"Do any of your immediate family members have chronic or hereditary conditions, such as heart disease, cancer, or diabetes? Please say 'Yes' or 'No'. If yes, please specify."
[AI listens and records the response]

8. Social History
Tobacco Use:

"Do you use tobacco products? Please say 'Yes' or 'No'. If yes, please specify the type and frequency."
[AI listens and records the response]

Alcohol Consumption:

"Do you consume alcohol? Please say 'Yes' or 'No'. If yes, please specify the amount and frequency."
[AI listens and records the response]

Recreational Drug Use:

"Do you use recreational drugs? Please say 'Yes' or 'No'. If yes, please specify the type and frequency."
[AI listens and records the response]

Occupation:

"What is your current occupation?"
[AI listens and records the response]

Stress or Major Life Changes:

"Are you experiencing any significant stress or major life changes?"
[AI listens and records the response]

9. Review of Systems
AI Assistant:

"Now, I will ask about various symptoms you may be experiencing. Please say 'Yes' if you are currently experiencing the symptom, 'No' if you are not, or 'Skip' to move to the next question."

General:

"Are you experiencing fever?"

[AI listens and records the response]

"Are you feeling fatigued?"

[AI listens and records the response]

"Have you had any unexplained weight loss or gain?"

[AI listens and records the response]

Cardiovascular:

"Are you experiencing chest pain?"

[AI listens and records the response]

"Do you have palpitations?"

[AI listens and records the response]

"Are you experiencing shortness of breath?"

[AI listens and records the response]

Respiratory:

"Do you have a cough?"

[AI listens and records the response]

"Are you wheezing?"

[AI listens and records the response]

"Do you have difficulty breathing?"

[AI listens and records the response]

Gastrointestinal:

"Are you experiencing nausea or vomiting?"

[AI listens and records the response]

"Do you have diarrhea or constipation?"

[AI listens and records the response]

"Are you having abdominal pain?"

[AI listens and records the response]

Musculoskeletal:

"Are you experiencing joint pain?"

[AI listens and records the response]

"Do you have muscle weakness?"

[AI listens and records the response]

"Are you having back pain?"

[AI listens and records the response]

Neurological:

"Do you have headaches?"

[AI listens and records the response]

"Are you experiencing dizziness?"

[AI listens and records the response]

"Do you have numbness or tingling?"

[AI listens and records the response]

Dermatological:

"Do you have any rashes?"

[AI listens and records the response]

"Are you experiencing itching?"

[AI listens and records the response]

"Do you have any lesions?"

[AI listens and records the response]

Other Symptoms:

"Please describe any other symptoms you are experiencing that have not been mentioned."

[AI listens and records the response]

10. Additional Information
Other Concerns:
"Is there anything else you would like to discuss or any other concerns you have before your consultation?"

[AI listens and records the response]

11. Call Closing
AI Assistant (Text-to-Speech):

"Thank you for providing this information. Our medical team will review your responses before your appointment. If we need any further information, we will contact you. If you have any questions or need to update your information, please call our office at [Phone Number]. Have a great day!"

Implementation Guidelines
Text-to-Speech (TTS):

Ensure the AI assistant uses clear and natural-sounding TTS to enhance patient understanding and comfort.
Adjust the speaking rate to accommodate various patient preferences.
Speech-to-Text (STT):

Utilize advanced STT capabilities to accurately capture patient responses, including names, dates, and specific medical terms.
Implement noise reduction and clarity enhancements to improve transcription accuracy.
Natural Language Understanding (NLU):

Equip the AI with robust NLU to interpret varied patient responses, handling nuances like "I don't use tobacco" or "Occasionally drink socially."
Implement context-awareness to connect related answers and ensure coherent data collection.
Error Handling:

If the AI does not understand a response, it should politely prompt the patient to repeat or clarify. For example:
"I'm sorry, I didn't catch that. Could you please repeat your answer?"
Allow patients to skip questions or indicate if they're uncomfortable answering certain items.
Privacy and Security:

Ensure all data is encrypted during transmission and storage to comply with healthcare regulations such as HIPAA.
Inform patients at the beginning of the call about data usage and privacy policies.
Provide an option for patients to consent to data collection before proceeding.
User Experience:

Maintain a friendly and professional tone throughout the call to put patients at ease.
Allow patients to navigate the call easily, with options to repeat questions or end the call if needed.
Ensure the call does not exceed a reasonable duration to prevent fatigue.
Customization:

Tailor the script to align with specific medical practice requirements or specialties.
Include additional questions relevant to particular fields, such as mental health, pediatrics, or geriatrics, as needed.
Testing and Feedback:

Conduct thorough testing with diverse patient groups to identify and rectify potential issues.
Gather patient feedback to continuously improve the call experience and questionnaire accuracy.
"""