from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

# Initialize the app
app = Flask(__name__)
CORS(app)

# Route to serve the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Example symptom-to-disease mapping
disease_data = {
    "fever, cough, fatigue": {
        "disease": "Flu",
        "precautions": ["Drink plenty of fluids", "Rest", "Take over-the-counter fever medicine", "Consult a doctor if symptoms worsen"]
    },
    "fever, headache, body ache, chills": {
        "disease": "Malaria",
        "precautions": ["Take anti-malarial medication", "Stay hydrated", "Consult a doctor", "Avoid mosquito bites"]
    },
    "fever, sore throat, cough": {
        "disease": "COVID-19",
        "precautions": ["Wear a mask", "Isolate", "Consult a doctor", "Get tested for COVID-19"]
    },
    "fatigue, muscle pain, fever": {
        "disease": "Dengue",
        "precautions": ["Stay hydrated", "Rest", "Avoid mosquito exposure", "Consult a doctor for specific treatment"]
    },
    "headache, nausea, vomiting": {
        "disease": "Migraine",
        "precautions": ["Avoid bright lights", "Take prescribed migraine medication", "Rest in a quiet environment"]
    },
    "nausea, vomiting, stomach pain, diarrhea": {
        "disease": "Gastroenteritis",
        "precautions": ["Stay hydrated", "Eat light food", "Consult a doctor if symptoms worsen"]
    },
    "cough, shortness of breath, chest pain": {
        "disease": "Pneumonia",
        "precautions": ["Consult a doctor", "Take prescribed antibiotics", "Rest and stay hydrated"]
    },
    "itchy eyes, sneezing, runny nose": {
        "disease": "Allergic Rhinitis",
        "precautions": ["Avoid allergens", "Take antihistamines", "Consult an allergist"]
    },
    "painful urination, frequent urination, blood in urine": {
        "disease": "Urinary Tract Infection (UTI)",
        "precautions": ["Drink plenty of water", "Take prescribed antibiotics", "Consult a doctor"]
    },
    "chronic cough, wheezing, shortness of breath": {
        "disease": "Asthma",
        "precautions": ["Take prescribed inhalers", "Avoid asthma triggers", "Consult a doctor for management"]
    },
    "fever, fatigue, loss of appetite, yellowing skin": {
        "disease": "Hepatitis",
        "precautions": ["Consult a doctor", "Take prescribed antiviral treatment", "Avoid alcohol and fatty foods"]
    },
    "swollen lymph nodes, fatigue, sore throat, fever": {
        "disease": "Mononucleosis (Mono)",
        "precautions": ["Get plenty of rest", "Stay hydrated", "Avoid contact sports to prevent spleen injury"]
    },
    "abdominal pain, bloating, constipation": {
        "disease": "Irritable Bowel Syndrome (IBS)",
        "precautions": ["Eat a balanced diet", "Exercise regularly", "Consult a doctor for medication"]
    },
    "red rash, itching, blisters": {
        "disease": "Chickenpox",
        "precautions": ["Take calamine lotion", "Avoid scratching the rash", "Consult a doctor for antiviral treatment"]
    },
    "joint pain, swelling, fever": {
        "disease": "Rheumatoid Arthritis",
        "precautions": ["Take prescribed anti-inflammatory medications", "Exercise gently", "Consult a doctor for management"]
    },
    "cough, fever, sore throat, body aches": {
        "disease": "Common Cold",
        "precautions": ["Rest", "Drink warm fluids", "Take over-the-counter cold medicine", "Avoid close contact with others"]
    },
    "sudden weight loss, excessive thirst, frequent urination": {
        "disease": "Diabetes Mellitus",
        "precautions": ["Monitor blood sugar levels", "Take prescribed insulin", "Follow a healthy diet plan"]
    },
    "chest pain, difficulty breathing, sweating": {
        "disease": "Heart Attack",
        "precautions": ["Call emergency services", "Chew aspirin", "Stay calm and rest"]
    },
    "painful joints, red, swollen joints": {
        "disease": "Gout",
        "precautions": ["Avoid alcohol and red meat", "Take prescribed medication", "Consult a doctor"]
    },
    "abdominal bloating, gas, diarrhea": {
        "disease": "Celiac Disease",
        "precautions": ["Follow a gluten-free diet", "Take prescribed supplements", "Consult a doctor"]
    },
    "blurred vision, headaches, excessive thirst, dry mouth": {
        "disease": "Diabetic Retinopathy",
        "precautions": ["Manage blood sugar levels", "Consult an eye doctor for regular checkups", "Follow a diabetic diet"]
    },
    "abdominal pain, jaundice, nausea": {
        "disease": "Gallstones",
        "precautions": ["Consult a doctor", "Limit fat intake", "Stay hydrated"]
    },
    "dry skin, hair loss, fatigue, weight gain": {
        "disease": "Hypothyroidism",
        "precautions": ["Take thyroid hormone replacement", "Consult an endocrinologist", "Follow a healthy diet"]
    }
}


# API endpoint to handle diagnosis
@app.route('/diagnose', methods=['POST'])
def diagnose():
    data = request.json
    symptoms = data.get('symptoms', '').lower()
    result = disease_data.get(
        symptoms,
        {"disease": "Unknown", "precautions": ["Consult a doctor"]}
    )
    result["doctors"] = "Dr. Smith: 1234567890, Dr. Jane: 0987654321"
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
