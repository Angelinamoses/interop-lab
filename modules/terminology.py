def map_snomed_concept(term):
    """
    Simulate mapping a clinical term to SNOMED CT.
    """

    terminology_map = {
        "Chest pain": {
            "system": "SNOMED CT",
            "code": "29857009",
            "display": "Chest pain"
        },
        "Shortness of breath": {
            "system": "SNOMED CT",
            "code": "267036007",
            "display": "Dyspnea"
        },
        "Sweating": {
            "system": "SNOMED CT",
            "code": "415690000",
            "display": "Sweating"
        }
    }

    return terminology_map.get(
        term,
        {
            "system": "SNOMED CT",
            "code": "UNKNOWN",
            "display": term
        }
    )


def map_loinc_test(test_name):
    """
    Simulate mapping a laboratory test to LOINC.
    """

    terminology_map = {
        "troponin": {
            "system": "LOINC",
            "code": "6598-7",
            "display": "Troponin T"
        },
        "glucose": {
            "system": "LOINC",
            "code": "2345-7",
            "display": "Glucose"
        }
    }

    return terminology_map.get(
        test_name.lower(),
        {
            "system": "LOINC",
            "code": "UNKNOWN",
            "display": test_name
        }
    )


def map_disease_classification(term):
    """
    Simulate disease classification using ICD.
    """

    classification_map = {
        "myocardial infarction": {
            "system": "ICD-10",
            "code": "I21.9",
            "display": "Acute myocardial infarction, unspecified"
        }
    }

    return classification_map.get(
        term.lower(),
        {
            "system": "ICD-10",
            "code": "UNKNOWN",
            "display": term
        }
    )


def generate_terminology_summary(ehr_record):
    """
    Convert selected clinical information into
    standardized terminology representations.
    """

    symptoms = []

    for symptom in ehr_record["symptoms"]:
        symptoms.append(map_snomed_concept(symptom))

    laboratory = []

    for test_name in ehr_record["laboratory"]:
        laboratory.append(
            map_loinc_test(test_name)
        )

    return {
        "clinical_concepts": symptoms,
        "laboratory_tests": laboratory
    }