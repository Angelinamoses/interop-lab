def create_xds_document(ehr_record):
    """
    Create a simplified clinical document for HIE exchange.

    Educational simulation only.
    """

    patient = ehr_record["patient"]
    encounter = ehr_record["encounter"]

    return {
        "document_id": "DOC-001",
        "patient_id": patient["patient_id"],
        "document_type": "Emergency Encounter Summary",
        "source": "INTEROP-LAB Hospital",
        "encounter": encounter["encounter_id"],
        "status": "Available"
    }


def register_document(document):
    """
    Simulate registering a document in an XDS registry.
    """

    return {
        "document_id": document["document_id"],
        "patient_id": document["patient_id"],
        "document_type": document["document_type"],
        "registry_status": "Registered"
    }


def store_document(document):
    """
    Simulate storing a document in an XDS repository.
    """

    return {
        "document_id": document["document_id"],
        "repository": "INTEROP-LAB XDS Repository",
        "storage_status": "Stored"
    }


def query_document(patient_id, registry):
    """
    Simulate an authorized query for documents belonging
    to a patient.
    """

    if patient_id == registry["patient_id"]:

        return {
            "status": "Match found",
            "document_id": registry["document_id"],
            "document_type": registry["document_type"]
        }

    return {
        "status": "No matching document",
        "document_id": None,
        "document_type": None
    }


def retrieve_document(document_id, repository):
    """
    Simulate retrieving a document from the repository.
    """

    if document_id == repository["document_id"]:

        return {
            "status": "Retrieved",
            "document_id": document_id
        }

    return {
        "status": "Retrieval failed",
        "document_id": None
    }