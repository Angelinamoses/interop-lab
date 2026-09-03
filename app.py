import streamlit as st


st.set_page_config(
    page_title="INTEROP-LAB",
    page_icon="🏥",
    layout="wide"
)


st.title("🏥 INTEROP-LAB")
st.subheader("A Live Healthcare Interoperability Simulation")

st.info(
    "Educational simulation using synthetic healthcare data. "
    "This is not a clinical diagnostic system."
)

st.markdown("""
### Patient → Data → Interoperability → Intelligence → Action

This application will demonstrate how healthcare data moves across
clinical systems using interoperability standards and technologies.
""")