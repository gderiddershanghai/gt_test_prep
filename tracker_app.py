import streamlit as st
import pandas as pd
from datetime import datetime
import os

# CSV file path
CSV_FILE = "entry_log.csv"

# Ensure the CSV file exists with headers
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=["timestamp", "building", "direction", "count"])
    df.to_csv(CSV_FILE, index=False)

# Function to log entry
def log_event(building, direction):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_row = {"timestamp": timestamp, "building": building, "direction": direction, "count": 1}
    df = pd.DataFrame([new_row])
    df.to_csv(CSV_FILE, mode='a', header=False, index=False)
    st.success(f"{direction} recorded for {building} at {timestamp}")

# Streamlit UI
st.title("Building Entry/Exit Tracker")

st.header("Building Close")
col1, col2 = st.columns(2)
with col1:
    if st.button("Go In (Close)"):
        log_event("close", "in")
with col2:
    if st.button("Go Out (Close)"):
        log_event("close", "out")

st.header("Building Far")
col3, col4 = st.columns(2)
with col3:
    if st.button("Go In (Far)"):
        log_event("far", "in")
with col4:
    if st.button("Go Out (Far)"):
        log_event("far", "out")

# Optional: Display the log
if st.checkbox("Show Log"):
    df = pd.read_csv(CSV_FILE)
    st.dataframe(df)
