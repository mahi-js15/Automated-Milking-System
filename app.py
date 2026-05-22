import streamlit as st
import time

st.set_page_config(
    page_title="Automated Milking System",
    page_icon="🐄",
    layout="wide"
)

st.title("🐄 Automated Milking System")
st.subheader("Smart Dairy Automation Dashboard")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/1998/1998610.png",
        width=250
    )

with col2:
    st.markdown("""
### Project Features
✅ Cow Detection System  
✅ Automatic Milking Process  
✅ Milk Tank Monitoring  
✅ LED & Buzzer Alerts  
✅ Servo Motor Automation  
""")

st.markdown("---")

st.header("System Control Panel")

cow = st.selectbox(
    "Cow Detection Status",
    ["No Cow Detected", "Cow Detected"]
)

start = st.button("▶ Start Milking Process")

if start:

    if cow == "No Cow Detected":
        st.warning("⚠ No cow detected")
        st.stop()

    st.success("🐄 Cow Detected")

    progress = st.progress(0)

    status = st.empty()

    status.info("Checking system...")
    progress.progress(20)
    time.sleep(1)

    status.info("Activating Servo Motor...")
    progress.progress(40)
    time.sleep(1)

    status.info("Starting Milk Collection...")
    progress.progress(60)
    time.sleep(1)

    status.info("Filling Milk Tank...")
    progress.progress(80)
    time.sleep(1)

    status.success("✅ Milking Completed Successfully")
    progress.progress(100)

    st.balloons()

st.markdown("---")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Milk Collected",
        "15 L"
    )

with c2:
    st.metric(
        "System Status",
        "ACTIVE"
    )

with c3:
    st.metric(
        "Tank Level",
        "80%"
    )

st.markdown("---")

st.subheader("Project Team")
st.write("Mini Project : Automated Milking System")
