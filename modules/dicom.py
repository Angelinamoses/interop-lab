def create_dicom_study(ehr_record):
    """
    Create a simplified DICOM study representation.

    Educational simulation only. This does not create
    a real DICOM image file.
    """

    patient = ehr_record["patient"]
    imaging = ehr_record["imaging"]

    return {
        "patient_id": patient["patient_id"],
        "patient_name": patient["name"],
        "study_id": imaging["study_id"],
        "modality": imaging["modality"],
        "study_status": imaging["status"],
        "accession_number": "ACC-001",
        "body_part": "Chest"
    }


def create_imaging_workflow(dicom_study):
    """
    Simulate the movement of an imaging study
    through the radiology workflow.
    """

    return [
        {
            "system": "EHR/HIS",
            "action": "Imaging order created",
            "status": "Completed"
        },
        {
            "system": "RIS",
            "action": "Study scheduled",
            "status": "Completed"
        },
        {
            "system": "Imaging Modality",
            "action": "Image acquired",
            "status": "Completed"
        },
        {
            "system": "PACS",
            "action": "Image stored",
            "status": "Completed"
        },
        {
            "system": "Radiologist",
            "action": "Image reviewed",
            "status": "Pending"
        }
    ]