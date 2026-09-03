import streamlit as st

from modules.patient import create_patient
from modules.ehr import create_ehr_record, get_patient_summary
from modules.interoperability import (
    validate_patient_record,
    check_patient_identity,
    route_data
)
from modules.terminology import (
    generate_terminology_summary,
    map_disease_classification
)
from modules.hl7 import (
    generate_hl7_message,
    parse_hl7_message,
    get_hl7_segments
)
from modules.fhir import (
    create_patient_resource,
    create_encounter_resource,
    create_observation_resource,
    create_fhir_bundle
)
from modules.dicom import (
    create_dicom_study,
    create_imaging_workflow
)
from modules.hie import (
    create_xds_document,
    register_document,
    store_document,
    query_document,
    retrieve_document
)
from modules.analytics import (
    build_integrated_dataset,
    calculate_data_quality,
    generate_analytic_features
)
from modules.cdss import (
    generate_cdss_alerts,
    generate_clinical_summary
)
from modules.security import (
    authenticate_user,
    check_authorization,
    check_consent,
    create_audit_event
)
from modules.abdm import (
    create_abdm_discharge_summary,
    validate_abdm_record
)
from modules.workflow import (
    create_workflow_steps,
    simulate_failure
)
st.set_page_config(
    page_title="INTEROP-LAB",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 INTEROP-LAB")
st.subheader("M1 → M2 → M3: Patient Data → EHR/HIS → Interoperability")

st.info(
    "Educational simulation using synthetic healthcare data. "
    "This is not a clinical diagnostic system."
)


# -----------------------------
# M1: Generate patient data
# -----------------------------

patient = create_patient()


# -----------------------------
# M2: Store data in EHR/HIS
# -----------------------------

ehr_record = create_ehr_record(patient)

summary = get_patient_summary(ehr_record)


st.markdown("## 🏥 Hospital Information System")

st.write(
    "The EHR/HIS receives and organizes information generated "
    "during the patient's healthcare encounter."
)


# -----------------------------
# M3: Interoperability Engine
# -----------------------------

validation_results = validate_patient_record(ehr_record)

identity_result = check_patient_identity(ehr_record)

routing_result = route_data(
    ehr_record,
    "Regional Health Information Exchange"
)

# -----------------------------
# M4: Terminology
# -----------------------------

terminology = generate_terminology_summary(ehr_record)

disease_classification = map_disease_classification(
    "myocardial infarction"
)

# -----------------------------
# M5: HL7 v2
# -----------------------------

hl7_message = generate_hl7_message(ehr_record)
hl7_segments = get_hl7_segments(hl7_message)
parsed_hl7 = parse_hl7_message(hl7_message)

# -----------------------------
# M6: FHIR
# -----------------------------

fhir_patient = create_patient_resource(ehr_record)
fhir_encounter = create_encounter_resource(ehr_record)
fhir_observations = create_observation_resource(ehr_record)
fhir_bundle = create_fhir_bundle(ehr_record)

# -----------------------------
# M7: DICOM + Imaging
# -----------------------------

dicom_study = create_dicom_study(ehr_record)

imaging_workflow = create_imaging_workflow(dicom_study)

# -----------------------------
# M8: HIE / IHE XDS
# -----------------------------

xds_document = create_xds_document(ehr_record)

xds_registry = register_document(xds_document)

xds_repository = store_document(xds_document)

xds_query = query_document(
    patient["patient"]["patient_id"],
    xds_registry
)

xds_retrieval = retrieve_document(
    xds_query["document_id"],
    xds_repository
)

# M9: Data Integration + Analytics

integrated_data = build_integrated_dataset(
    ehr_record,
    terminology
)

data_quality = calculate_data_quality(
    integrated_data
)

analytic_features = generate_analytic_features(
    integrated_data
)

# -----------------------------
# M10: Clinical Decision Support
# -----------------------------

cdss_alerts = generate_cdss_alerts(
    integrated_data,
    analytic_features
)

clinical_summary = generate_clinical_summary(
    integrated_data,
    cdss_alerts
)

# -----------------------------
# M11: Security, Privacy & Governance
# -----------------------------

authentication = authenticate_user(
    "doctor",
    "doctor123"
)

authorization = check_authorization(
    "doctor",
    "clinical_data"
)

consent = check_consent(
    True
)

audit_event = create_audit_event(
    "doctor",
    "Access patient clinical data",
    "clinical_data",
    "Allowed"
)

# -----------------------------
# M12: India / ABDM
# -----------------------------

abdm_record = create_abdm_discharge_summary(
    ehr_record
)

abdm_validation = validate_abdm_record(
    abdm_record
)

# -----------------------------
# M13: Integrated Workflow
# -----------------------------

workflow_steps = create_workflow_steps()

# -----------------------------
# Patient Summary
# -----------------------------

st.markdown("### Patient Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Patient ID",
        summary["Patient ID"]
    )

with col2:
    st.metric(
        "Age",
        summary["Age"]
    )

with col3:
    st.metric(
        "Symptoms",
        summary["Symptoms"]
    )

with col4:
    st.metric(
        "Medications",
        summary["Medications"]
    )


# -----------------------------
# Encounter
# -----------------------------

st.markdown("### Encounter")

st.json(ehr_record["encounter"])


# -----------------------------
# Clinical Data
# -----------------------------

st.markdown("### Clinical Observations")

st.json(ehr_record["clinical_observations"])


# -----------------------------
# Laboratory
# -----------------------------

st.markdown("### Laboratory Data")

st.json(ehr_record["laboratory"])


# -----------------------------
# Imaging
# -----------------------------

st.markdown("### Imaging")

st.json(ehr_record["imaging"])


# -----------------------------
# Medication
# -----------------------------

st.markdown("### Medication")

st.json(ehr_record["medication"])


# -----------------------------
# Device Data
# -----------------------------

st.markdown("### Device Data")

st.json(ehr_record["device_data"])


# -----------------------------
# Patient-generated data
# -----------------------------

st.markdown("### Patient-Generated Data")

st.json(ehr_record["patient_generated_data"])


# -----------------------------
# Full EHR record
# -----------------------------

with st.expander("🔎 View Complete EHR Record"):
    st.json(ehr_record)


# =====================================================
# M3: INTEROPERABILITY ENGINE
# =====================================================

st.markdown("---")

st.header("🔄 M3: Interoperability Engine")

st.write(
    "Before healthcare information is exchanged between systems, "
    "the data must be checked, the patient identified, and the "
    "information routed to the appropriate destination."
)


# -----------------------------
# Validation
# -----------------------------

st.markdown("### 1️⃣ Data Validation")

validation_cols = st.columns(len(validation_results))

for col, (field, status) in zip(
    validation_cols,
    validation_results.items()
):
    with col:
        st.metric(
            field.replace("_", " ").title(),
            status
        )


# -----------------------------
# Patient Matching
# -----------------------------

st.markdown("### 2️⃣ Patient Identification")

if identity_result["status"] == "Matched":

    st.success(
        f'Patient matched successfully: '
        f'{identity_result["patient_id"]}'
    )

else:

    st.error("Patient identification failed.")


# -----------------------------
# Routing
# -----------------------------

st.markdown("### 3️⃣ Data Routing")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**Source**")
    st.code(routing_result["source"])

with col2:
    st.write("**Destination**")
    st.code(routing_result["destination"])

with col3:
    st.write("**Status**")
    st.success(routing_result["status"])

st.markdown("---")

st.header("🧠 M4: Terminology & Semantic Interoperability")

st.write(
    "Healthcare information is mapped to standardized terminology "
    "so that different systems can interpret the clinical meaning "
    "consistently."
)


# -----------------------------
# SNOMED CT
# -----------------------------

st.markdown("### 🩺 Clinical Concepts → SNOMED CT")

for concept in terminology["clinical_concepts"]:

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("**Local term**")
        st.write(concept["display"])

    with col2:
        st.write("**Terminology**")
        st.write(concept["system"])

    with col3:
        st.write("**Code**")
        st.code(concept["code"])


# -----------------------------
# LOINC
# -----------------------------

st.markdown("### 🧪 Laboratory Tests → LOINC")

for test in terminology["laboratory_tests"]:

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("**Test**")
        st.write(test["display"])

    with col2:
        st.write("**Terminology**")
        st.write(test["system"])

    with col3:
        st.write("**Code**")
        st.code(test["code"])


# -----------------------------
# ICD
# -----------------------------

st.markdown("### 🏥 Disease Classification → ICD")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**Condition**")
    st.write("Myocardial infarction")

with col2:
    st.write("**Classification**")
    st.write(disease_classification["system"])

with col3:
    st.write("**Code**")
    st.code(disease_classification["code"])

st.markdown("---")

st.header("📡 M5: HL7 v2 Message Exchange")

st.write(
    "The EHR converts selected patient and encounter information "
    "into a structured HL7 v2-style message for system-to-system exchange."
)


# -----------------------------
# Message
# -----------------------------

st.markdown("### HL7 v2 Message")

st.code(
    hl7_message,
    language="text"
)


# -----------------------------
# Segments
# -----------------------------

st.markdown("### Message Segments")

segment_cols = st.columns(len(hl7_segments))

for col, segment in zip(segment_cols, hl7_segments):

    with col:
        st.metric(
            "Segment",
            segment
        )


# -----------------------------
# Explanation
# -----------------------------

st.markdown("### What do these segments represent?")

st.markdown("""
- **MSH** → Message Header
- **PID** → Patient Identification
- **PV1** → Patient Visit / Encounter information
""")

st.markdown("---")

st.header("🚀 M6: FHIR")

st.write(
    "FHIR represents healthcare information as modular resources "
    "that can be exchanged between healthcare systems."
)


# -----------------------------
# Resource Overview
# -----------------------------

st.markdown("### FHIR Resources")

resources = [
    fhir_patient,
    fhir_encounter,
    *fhir_observations
]

cols = st.columns(len(resources))

for col, resource in zip(cols, resources):

    with col:
        st.metric(
            "Resource",
            resource["resourceType"]
        )


# -----------------------------
# Patient Resource
# -----------------------------

st.markdown("### 👤 Patient Resource")

st.json(fhir_patient)


# -----------------------------
# Encounter Resource
# -----------------------------

st.markdown("### 🏥 Encounter Resource")

st.json(fhir_encounter)


# -----------------------------
# Observation Resources
# -----------------------------

st.markdown("### 📊 Observation Resources")

for observation in fhir_observations:

    with st.expander(
        observation["id"]
    ):
        st.json(observation)


# -----------------------------
# Bundle
# -----------------------------

st.markdown("### 📦 FHIR Bundle")

st.write(
    "A Bundle can contain multiple FHIR resources "
    "for exchange as a single package."
)

st.json(fhir_bundle)

st.markdown("---")

st.header("🩻 M7: DICOM + Imaging Workflow")

st.write(
    "Imaging data follows a specialized workflow involving "
    "the EHR/HIS, RIS, imaging modality, PACS and radiologist."
)


# -----------------------------
# DICOM Study
# -----------------------------

st.markdown("### DICOM Study")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**Patient ID**")
    st.code(dicom_study["patient_id"])

with col2:
    st.write("**Study ID**")
    st.code(dicom_study["study_id"])

with col3:
    st.write("**Modality**")
    st.write(dicom_study["modality"])


st.json(dicom_study)


# -----------------------------
# Imaging Workflow
# -----------------------------

st.markdown("### Imaging Workflow")

for step_number, step in enumerate(
    imaging_workflow,
    start=1
):

    st.markdown(
        f"**{step_number}. {step['system']}**"
    )

    st.write(
        f"{step['action']} → `{step['status']}`"
    )

st.markdown("---")

st.header("🌐 M8: Health Information Exchange")

st.write(
    "This module simulates how a clinical document can be "
    "registered, stored, discovered and retrieved across "
    "healthcare organizations."
)


# -----------------------------
# XDS Architecture
# -----------------------------

st.markdown("### IHE XDS Document Sharing")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📄 Document Source")
    st.write("INTEROP-LAB Hospital")
    st.success("Document submitted")

with col2:
    st.markdown("### 🗃️ Repository")
    st.write(xds_repository["repository"])
    st.success(xds_repository["storage_status"])

with col3:
    st.markdown("### 📋 Registry")
    st.write("XDS Registry")
    st.success(xds_registry["registry_status"])


# -----------------------------
# Document
# -----------------------------

st.markdown("### Clinical Document")

st.json(xds_document)


# -----------------------------
# Query
# -----------------------------

st.markdown("### 🔎 Document Query")

st.write(
    f"Searching for documents belonging to "
    f"patient `{patient['patient']['patient_id']}`"
)

if xds_query["status"] == "Match found":

    st.success(
        f"Document found: {xds_query['document_id']}"
    )

else:

    st.error("No matching document found.")


# -----------------------------
# Retrieval
# -----------------------------

st.markdown("### 📥 Document Retrieval")

if xds_retrieval["status"] == "Retrieved":

    st.success(
        f"Document `{xds_retrieval['document_id']}` retrieved successfully."
    )

else:

    st.error("Document retrieval failed.")

st.header("M9: Data Integration + Analytics")

st.subheader("Integrated Patient Dataset")

st.json(integrated_data)

st.subheader("Data Quality")

st.write(
    f"Completeness: "
    f"{data_quality['completeness_percent']}%"
)

st.write(
    f"Missing fields: "
    f"{data_quality['missing_count']}"
)

if data_quality["missing_fields"]:
    st.write(data_quality["missing_fields"])
else:
    st.success("No missing fields detected.")

st.subheader("Derived Analytic Features")

for feature, value in analytic_features.items():
    st.write(f"**{feature}:** {value}")

st.header("M10: Clinical Decision Support System")

st.subheader("Decision-Support Signals")

if cdss_alerts:
    for alert in cdss_alerts:
        st.info(
            f"**{alert['type']}** | "
            f"{alert['priority']} | "
            f"{alert['message']}"
        )
else:
    st.success("No demonstration signals detected.")

st.subheader("Clinical Summary")

st.write(
    f"**Patient ID:** "
    f"{clinical_summary['patient_id']}"
)

st.write(
    f"**Signals detected:** "
    f"{clinical_summary['signals_detected']}"
)

st.write(
    f"**Suggested workflow:** "
    f"{clinical_summary['recommended_action']}"
)

st.caption(
    "Educational simulation only. "
    "These signals are not clinical diagnoses or treatment recommendations."
)

st.header("M11: Security, Privacy & Governance")

st.subheader("Authentication")

if authentication["authenticated"]:
    st.success(
        f"Authenticated user: {authentication['username']}"
    )
else:
    st.error("Authentication failed.")

st.subheader("Authorization")

if authorization["authorized"]:
    st.success(
        f"Access authorized for: "
        f"{authorization['resource']}"
    )
else:
    st.error(
        f"Access denied for: "
        f"{authorization['resource']}"
    )

st.subheader("Patient Consent")

if consent["status"] == "Approved":
    st.success(consent["message"])
else:
    st.error(consent["message"])

st.subheader("Audit Log")

st.json(audit_event)

st.caption(
    "Educational simulation only. "
    "This module demonstrates security and governance concepts "
    "and is not a production security implementation."
)
st.header("M12: India / ABDM")

st.subheader("ABDM-Aligned FHIR Record")

st.json(abdm_record)

st.subheader("Record Validation")

for field, status in abdm_validation.items():
    if status == "Present":
        st.success(f"{field}: {status}")
    else:
        st.error(f"{field}: {status}")

st.caption(
    "Educational simulation only. "
    "This is not connected to the ABDM network "
    "and does not exchange real health information."
)

st.header("M13: Integrated Healthcare Workflow")

st.subheader("End-to-End Data-to-Action Pipeline")

for step in workflow_steps:
    if step["status"] == "Completed":
        st.success(
            f"Step {step['step']}: "
            f"{step['system']} → {step['action']}"
        )
    else:
        st.warning(
            f"Step {step['step']}: "
            f"{step['system']} → {step['action']}"
        )

st.subheader("Interoperability Failure Simulator")

failure_type = st.selectbox(
    "Select a failure scenario",
    [
        "Terminology Mapping Failure",
        "Patient Identity Failure",
        "FHIR Validation Failure",
        "Consent Failure"
    ]
)

if st.button("Simulate Failure"):

    failure = simulate_failure(
        failure_type
    )

    st.error(
        f"Failure: {failure['result']}"
    )

    st.write(
        f"**Affected component:** "
        f"{failure['component']}"
    )

    st.write(
        f"**Effect:** "
        f"{failure['effect']}"
    )