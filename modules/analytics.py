def build_integrated_dataset(ehr_record, terminology):
    """
    Combine clinical, laboratory, device, encounter,
    and terminology data into one analytic representation.

    Educational simulation only.
    """

    patient = ehr_record["patient"]
    encounter = ehr_record["encounter"]
    clinical = ehr_record["clinical_observations"]
    laboratory = ehr_record["laboratory"]
    device = ehr_record["device_data"]

    integrated_data = {
        "patient_id": patient["patient_id"],
        "age": patient["age"],
        "sex": patient["sex"],

        "encounter_type": encounter["type"],
        "department": encounter["department"],

        "heart_rate_bpm": clinical["heart_rate_bpm"],
        "systolic_bp_mmhg": clinical["systolic_bp_mmhg"],
        "diastolic_bp_mmhg": clinical["diastolic_bp_mmhg"],
        "oxygen_saturation_percent": clinical["oxygen_saturation_percent"],
        "temperature_c": clinical["temperature_c"],

        "troponin_ng_ml": laboratory["troponin"]["value"],
        "glucose_mg_dl": laboratory["glucose"]["value"],

        "device_heart_rate_bpm": device["heart_rate_bpm"],
        "device_oxygen_saturation_percent": device[
            "oxygen_saturation_percent"
        ],

        "clinical_concepts": len(
            terminology["clinical_concepts"]
        ),
        "coded_laboratory_tests": len(
            terminology["laboratory_tests"]
        )
    }

    return integrated_data


def calculate_data_quality(integrated_data):
    """
    Perform simple data-quality checks.
    """

    total_fields = len(integrated_data)

    missing_fields = [
        field
        for field, value in integrated_data.items()
        if value is None or value == ""
    ]

    completeness = (
        (total_fields - len(missing_fields))
        / total_fields
        * 100
    )

    return {
        "total_fields": total_fields,
        "missing_fields": missing_fields,
        "missing_count": len(missing_fields),
        "completeness_percent": round(completeness, 2)
    }


def generate_analytic_features(integrated_data):
    """
    Generate simple derived features for educational analytics.

    These indicators are NOT clinical diagnoses or medical
    decision-making rules.
    """

    features = {
        "heart_rate_above_100": (
            integrated_data["heart_rate_bpm"] > 100
        ),

        "systolic_bp_above_140": (
            integrated_data["systolic_bp_mmhg"] > 140
        ),

        "troponin_present": (
            integrated_data["troponin_ng_ml"] is not None
        ),

        "device_data_available": (
            integrated_data["device_heart_rate_bpm"] is not None
            and
            integrated_data["device_oxygen_saturation_percent"]
            is not None
        )
    }

    return features