import streamlit as st
from tools.data_validation_tool import validate_event_log

st.set_page_config(page_title="PM AI AGENT MVP", layout="wide")

st.title("PM AI AGENT MVP")
st.subheader("Process Mining AI Agent - Version 1")

st.write("Upload an event log CSV file to validate and summarize the process data.")

uploaded_file = st.file_uploader("Upload your event log CSV", type=["csv"])

if uploaded_file is not None:
    st.success("File uploaded successfully.")

    if st.button("Analyze Event Log"):
        result = validate_event_log(uploaded_file)

        if result["valid"]:
            st.subheader("Event Log Summary")

            col1, col2, col3 = st.columns(3)

            col1.metric("Total Events", result["total_events"])
            col2.metric("Total Cases", result["total_cases"])
            col3.metric("Total Activities", result["total_activities"])

            st.write("**Start Time:**", result["start_time"])
            st.write("**End Time:**", result["end_time"])

            st.subheader("Activities")
            st.write(result["activities"])

            st.subheader("Missing Values")
            st.write(result["missing_values"])

        else:
            st.error(result["error"])