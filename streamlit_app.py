import streamlit as st
import json
from app.prompt import PROMPT_TEMPLATE
from app.llm_service import safe_generate
from app.coverage import calculate_coverage
from app.exporter import export_to_csv_string

st.set_page_config(page_title="LLM Test Case Generator", layout="wide")

st.title("🧪 LLM-Based Test Case Generator")
st.write("Convert functional requirements into structured test cases with coverage analysis.")

# Input
requirement = st.text_area(
    "Enter Functional Requirement",
    height=150,
    placeholder="Example: User can upload profile image up to 2MB"
)

generate_button = st.button("Generate Test Cases")

if generate_button and not requirement.strip():
    st.warning("Please enter a requirement.")

if generate_button and requirement:
    try:
        with st.spinner("Generating test cases..."):
            prompt = PROMPT_TEMPLATE.format(requirement=requirement)
            validated = safe_generate(prompt)
            coverage = calculate_coverage(validated.test_cases, validated.edge_cases)

            st.session_state["data"] = validated
            st.session_state["coverage"] = coverage

        st.success("Test cases generated successfully!")

    except Exception as e:
        st.error(f"Generation failed: {e}")

# Display results
if "data" in st.session_state:
    data = st.session_state["data"]
    coverage = st.session_state["coverage"]

    st.subheader("📊 Coverage Summary")
    st.json(coverage)

    st.subheader("🧾 Generated Test Cases")
    st.json(data.dict())

    # JSON download
    json_str = json.dumps(data.dict(), indent=2)
    st.download_button(
        label="⬇️ Download JSON",
        data=json_str,
        file_name="test_cases.json",
        mime="application/json"
    )

    # CSV download (in-memory)
    csv_data = export_to_csv_string(data)
    st.download_button(
        label="⬇️ Download CSV",
        data=csv_data,
        file_name="test_cases.csv",
        mime="text/csv"
    )
