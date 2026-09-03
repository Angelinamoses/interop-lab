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