def generate_cdss_alerts(integrated_data, analytic_features):
    """
    Generate simple educational decision-support alerts
    from integrated patient data.

    This is NOT a clinical diagnostic or treatment system.
    """

    alerts = []

    if analytic_features["heart_rate_above_100"]:
        alerts.append({
            "type": "Vital Sign Signal",
            "message": "Heart rate is above the demonstration threshold.",
            "priority": "Attention"
        })

    if analytic_features["systolic_bp_above_140"]:
        alerts.append({
            "type": "Vital Sign Signal",
            "message": "Systolic blood pressure is above the demonstration threshold.",
            "priority": "Attention"
        })

    if analytic_features["troponin_present"]:
        alerts.append({
            "type": "Laboratory Signal",
            "message": "Troponin result is available for clinical review.",
            "priority": "Review"
        })

    if analytic_features["device_data_available"]:
        alerts.append({
            "type": "Device Signal",
            "message": "Device-generated observations are available.",
            "priority": "Informational"
        })

    return alerts


def generate_clinical_summary(integrated_data, alerts):
    """
    Create an educational summary showing how analytics
    can support clinician review.
    """

    return {
        "patient_id": integrated_data["patient_id"],
        "signals_detected": len(alerts),
        "recommended_action": (
            "Review integrated clinical information "
            "and correlate with the patient's clinical context."
        )
    }