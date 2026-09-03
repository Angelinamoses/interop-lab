def create_workflow_steps():
    """
    Create the main healthcare interoperability workflow.
    """

    return [
        {
            "step": 1,
            "system": "Patient",
            "action": "Patient data generated",
            "status": "Completed"
        },
        {
            "step": 2,
            "system": "EHR/HIS",
            "action": "Clinical data stored",
            "status": "Completed"
        },
        {
            "step": 3,
            "system": "Interoperability Engine",
            "action": "Data validated and routed",
            "status": "Completed"
        },
        {
            "step": 4,
            "system": "Terminology Services",
            "action": "Clinical concepts standardized",
            "status": "Completed"
        },
        {
            "step": 5,
            "system": "FHIR / HL7",
            "action": "Data prepared for exchange",
            "status": "Completed"
        },
        {
            "step": 6,
            "system": "HIE",
            "action": "Information shared across systems",
            "status": "Completed"
        },
        {
            "step": 7,
            "system": "Analytics",
            "action": "Integrated data analyzed",
            "status": "Completed"
        },
        {
            "step": 8,
            "system": "CDSS",
            "action": "Decision-support signals generated",
            "status": "Completed"
        },
        {
            "step": 9,
            "system": "Clinician",
            "action": "Information reviewed for clinical action",
            "status": "Pending"
        },
        {
            "step": 10,
            "system": "Patient Outcome",
            "action": "Outcome recorded",
            "status": "Pending"
        }
    ]


def simulate_failure(failure_type):
    """
    Demonstrate common interoperability failure scenarios.
    """

    failures = {
        "Terminology Mapping Failure": {
            "component": "Terminology",
            "effect": "Data is exchanged, but the clinical meaning cannot be reliably mapped.",
            "result": "Semantic interoperability failure"
        },

        "Patient Identity Failure": {
            "component": "Patient Matching",
            "effect": "The receiving system cannot confidently match the patient.",
            "result": "Identity resolution failure"
        },

        "FHIR Validation Failure": {
            "component": "FHIR",
            "effect": "The payload may be valid JSON but does not conform to the expected structure/profile.",
            "result": "Conformance failure"
        },

        "Consent Failure": {
            "component": "Governance",
            "effect": "The exchange is blocked because authorization/consent requirements are not satisfied.",
            "result": "Governance failure"
        }
    }

    return failures.get(
        failure_type,
        {
            "component": "Unknown",
            "effect": "No failure scenario selected.",
            "result": "No simulation"
        }
    )