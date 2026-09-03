def validate_patient_record(ehr_record):
    """
    Basic validation before healthcare data is exchanged.
    """

    required_fields = [
        "patient",
        "encounter",
        "clinical_observations",
        "laboratory"
    ]

    results = {}

    for field in required_fields:
        if field in ehr_record:
            results[field] = "Valid"
        else:
            results[field] = "Missing"

    return results


def check_patient_identity(ehr_record):
    """
    Simulate patient identification before data exchange.
    """

    patient_id = ehr_record["patient"].get("patient_id")

    if patient_id:
        return {
            "status": "Matched",
            "patient_id": patient_id
        }

    return {
        "status": "Failed",
        "patient_id": None
    }


def route_data(ehr_record, destination):
    """
    Simulate routing healthcare information to another system.
    """

    return {
        "source": "INTEROP-LAB EHR/HIS",
        "destination": destination,
        "patient_id": ehr_record["patient"]["patient_id"],
        "status": "Ready for exchange"
    }