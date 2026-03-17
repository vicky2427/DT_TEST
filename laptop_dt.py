import streamlit as st
import time

st.set_page_config(page_title="Laptop Digital Twin", layout="wide")

st.title("💻 Laptop Digital Twin Dashboard")
st.markdown("---")

# Layout: Two columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("Physical Entity Data")
    cpu_plot = st.empty()
    mem_plot = st.empty()

with col2:
    st.subheader("Virtual Twin Status")
    status_box = st.empty()
    battery_gauge = st.empty()

# Real-time Loop
while True:
    # 1. Capture Data
    data = {
        "cpu": psutil.cpu_percent(),
        "mem": psutil.virtual_memory().percent,
        "batt": psutil.sensors_battery().percent if psutil.sensors_battery() else 0
    }
    
    # 2. Logic (Thresholding)
    status = "OPTIMAL"
    color = "green"
    if data['cpu'] > 80: 
        status = "CRITICAL: HIGH CPU LOAD"
        color = "red"
    
    # 3. Update Visuals
    cpu_plot.metric("CPU Usage", f"{data['cpu']}%")
    mem_plot.metric("Memory Usage", f"{data['mem']}%")
    battery_gauge.progress(data['batt'] / 100)
    status_box.markdown(f"### Current State: :{color}[{status}]")
    
    time.sleep(1) # Synchronize every second
