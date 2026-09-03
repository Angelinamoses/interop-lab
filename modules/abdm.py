def create_abdm_discharge_summary(ehr_record):
    """
    Simulate an ABDM-aligned discharge summary representation.

    Educational simulation only.
    """

    patient = ehr_record["patient"]
    encounter = ehr_record["encounter"]

    return {
        "resourceType": "Bundle",
        "profile": "ABDM DischargeSummaryRecord",
        "patient": {
            "id": patient["patient_id"],
            "name": patient["name"],
            "gender": patient["sex"],
            "birthDate": patient["date_of_birth"]
        },
        "encounter": {
            "id": encounter["encounter_id"],
            "type": encounter["type"],
            "department": encounter["department"]
        },
        "document_status": "Simulated",
        "data_source": "INTEROP-LAB EHR/HIS"
    }


def validate_abdm_record(abdm_record):
    """
    Perform basic structural checks on the simulated
    ABDM-aligned record.
    """

    required_fields = [
        "resourceType",
        "profile",
        "patient",
        "encounter"
    ]

    results = {}

    for field in required_fields:
        if field in abdm_record:
            results[field] = "Present"
        else:
            results[field] = "Missing"

    return results