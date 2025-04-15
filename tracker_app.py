import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import pandas as pd

# Authenticate using secrets
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]
creds = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=scope
)
client = gspread.authorize(creds)

# Open the Google Sheet by name
sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1nHXbWjyq4crK10V2VWH79DDhrUW-AuYbgiJMgrZQJS0/edit").sheet1


# Function to log entry
def log_event(building, direction):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [timestamp, building, direction, 1]
    sheet.append_row(row)
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
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    st.dataframe(df)
