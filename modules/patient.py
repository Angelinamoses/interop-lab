from datetime import datetime


def create_patient():
    patient = {
        "patient": {
            "patient_id": "PAT-001",
            "name": "Ravi Kumar",
            "age": 58,
            "sex": "Male",
            "date_of_birth": "1968-04-12"
        },

        "encounter": {
            "encounter_id": "ENC-001",
            "type": "Emergency",
            "date_time": datetime.now().isoformat(),
            "department": "Emergency Department"
        },

        "clinical_observations": {
            "heart_rate_bpm": 104,
            "systolic_bp_mmhg": 158,
            "diastolic_bp_mmhg": 94,
            "oxygen_saturation_percent": 96,
            "temperature_c": 37.1
        },

        "symptoms": [
            "Chest pain",
            "Shortness of breath",
            "Sweating"
        ],

        "laboratory": {
            "troponin": {
                "value": 0.42,
                "unit": "ng/mL",
                "status": "Preliminary"
            },
            "glucose": {
                "value": 146,
                "unit": "mg/dL",
                "status": "Final"
            }
        },

        "imaging": {
            "modality": "Chest X-ray",
            "study_id": "IMG-001",
            "status": "Completed"
        },

        "medication": {
            "current": [
                "Aspirin 75 mg",
                "Atorvastatin 20 mg"
            ]
        },

        "device_data": {
            "device_type": "Pulse Oximeter",
            "oxygen_saturation_percent": 96,
            "heart_rate_bpm": 104
        },

        "patient_generated_data": {
            "reported_pain_score": 7,
            "reported_symptoms": [
                "Chest pain",
                "Shortness of breath"
            ]
        }
    }

    return patient