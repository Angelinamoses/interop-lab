def create_patient_resource(ehr_record):
    """
    Create a simplified FHIR Patient resource.
    """

    patient = ehr_record["patient"]

    return {
        "resourceType": "Patient",
        "id": patient["patient_id"],
        "name": [
            {
                "text": patient["name"]
            }
        ],
        "gender": patient["sex"].lower(),
        "birthDate": patient["date_of_birth"]
    }


def create_observation_resource(ehr_record):
    """
    Create simplified FHIR Observation resources
    for selected clinical measurements.
    """

    observations = []

    clinical = ehr_record["clinical_observations"]

    observations.append({
        "resourceType": "Observation",
        "id": "OBS-HR-001",
        "status": "final",
        "code": {
            "text": "Heart rate"
        },
        "valueQuantity": {
            "value": clinical["heart_rate_bpm"],
            "unit": "beats/minute"
        }
    })

    observations.append({
        "resourceType": "Observation",
        "id": "OBS-SPO2-001",
        "status": "final",
        "code": {
            "text": "Oxygen saturation"
        },
        "valueQuantity": {
            "value": clinical["oxygen_saturation_percent"],
            "unit": "%"
        }
    })

    return observations


def create_encounter_resource(ehr_record):
    """
    Create a simplified FHIR Encounter resource.
    """

    encounter = ehr_record["encounter"]

    return {
        "resourceType": "Encounter",
        "id": encounter["encounter_id"],
        "status": "in-progress",
        "class": {
            "code": "EMER"
        },
        "serviceProvider": {
            "display": "INTEROP-LAB Hospital"
        }
    }


def create_fhir_bundle(ehr_record):
    """
    Create a simplified FHIR Bundle containing
    multiple resources.
    """

    patient = create_patient_resource(ehr_record)
    encounter = create_encounter_resource(ehr_record)
    observations = create_observation_resource(ehr_record)

    entries = [
        {"resource": patient},
        {"resource": encounter}
    ]

    for observation in observations:
        entries.append({
            "resource": observation
        })

    return {
        "resourceType": "Bundle",
        "type": "collection",
        "entry": entries
    }