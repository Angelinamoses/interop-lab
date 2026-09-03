def generate_hl7_message(ehr_record):
    """
    Generate a simplified HL7 v2-style ADT message
    from the EHR record.

    This is an educational simulation, not a production
    HL7 implementation.
    """

    patient = ehr_record["patient"]
    encounter = ehr_record["encounter"]

    message = [
        "MSH|^~\\&|INTEROP-LAB|HOSPITAL|EHR|HOSPITAL|202609032200||ADT^A01|MSG00001|P|2.5",
        f"PID|1||{patient['patient_id']}|||"
        f"{patient['name']}||{patient['date_of_birth']}|"
        f"{patient['sex']}",
        f"PV1|1|E|{encounter['department']}|||"
        f"ATTENDING^PHYSICIAN"
    ]

    return "\r".join(message)


def parse_hl7_message(message):
    """
    Parse a simplified HL7 message into segments.
    """

    segments = message.split("\r")

    parsed = []

    for segment in segments:
        fields = segment.split("|")

        parsed.append({
            "segment": fields[0],
            "fields": fields[1:]
        })

    return parsed


def get_hl7_segments(message):
    """
    Return the names of HL7 segments contained in the message.
    """

    return [
        segment.split("|")[0]
        for segment in message.split("\r")
    ]