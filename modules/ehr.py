def create_ehr_record(patient_data):
    """
    Simulate storing patient-generated and clinical data
    inside an Electronic Health Record / Hospital Information System.
    """

    ehr_record = {
        "system": "INTEROP-LAB EHR/HIS",
        "patient": patient_data["patient"],
        "encounter": patient_data["encounter"],
        "clinical_observations": patient_data["clinical_observations"],
        "symptoms": patient_data["symptoms"],
        "laboratory": patient_data["laboratory"],
        "imaging": patient_data["imaging"],
        "medication": patient_data["medication"],
        "device_data": patient_data["device_data"],
        "patient_generated_data": patient_data["patient_generated_data"]
    }

    return ehr_record


def get_patient_summary(ehr_record):
    """
    Generate a simple summary of the patient's EHR record.
    """

    return {
        "Patient ID": ehr_record["patient"]["patient_id"],
        "Patient Name": ehr_record["patient"]["name"],
        "Age": ehr_record["patient"]["age"],
        "Encounter": ehr_record["encounter"]["type"],
        "Department": ehr_record["encounter"]["department"],
        "Symptoms": len(ehr_record["symptoms"]),
        "Laboratory Tests": len(ehr_record["laboratory"]),
        "Imaging Studies": 1,
        "Medications": len(ehr_record["medication"]["current"])
    }