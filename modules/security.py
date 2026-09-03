def authenticate_user(username, password):
    """
    Simulate user authentication.

    Educational simulation only.
    """

    users = {
        "doctor": "doctor123",
        "admin": "admin123"
    }

    if username in users and users[username] == password:
        return {
            "authenticated": True,
            "username": username
        }

    return {
        "authenticated": False,
        "username": username
    }


def check_authorization(username, requested_role):
    """
    Simulate role-based authorization.
    """

    role_permissions = {
        "doctor": ["clinical_data", "patient_summary"],
        "admin": ["system_data", "audit_logs"]
    }

    allowed_resources = role_permissions.get(
        username,
        []
    )

    if requested_role in allowed_resources:
        return {
            "authorized": True,
            "resource": requested_role
        }

    return {
        "authorized": False,
        "resource": requested_role
    }


def check_consent(consent_given):
    """
    Simulate a patient-consent check before data exchange.
    """

    if consent_given:
        return {
            "status": "Approved",
            "message": "Data exchange permitted."
        }

    return {
        "status": "Blocked",
        "message": "Data exchange blocked because consent is unavailable."
    }


def create_audit_event(
    username,
    action,
    resource,
    status
):
    """
    Create a simple audit-log event.
    """

    return {
        "user": username,
        "action": action,
        "resource": resource,
        "status": status
    }