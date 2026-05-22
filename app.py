import streamlit as st
import time

st.set_page_config(
    page_title="Automated Milking System",
    page_icon="🐄"
)

st.title("🐄 Automated Milking System")
st.subheader("Mini Project Simulation")

st.write("System checks cow detection and starts automatic milking process.")

cow = st.selectbox(
    "Cow Detected?",
    ["No", "Yes"]
)

if cow == "Yes":
    st.success("Cow detected successfully")

    if st.button("Start Milking"):

        st.write("Step 1: Checking cow position...")
        time.sleep(2)

        progress = st.progress(25)

        st.write("Step 2: Servo Motor Activated")
        time.sleep(2)
        progress.progress(50)

        st.write("Step 3: Milk Collection Started")
        time.sleep(2)
        progress.progress(75)

        st.success("Milking Completed")
        progress.progress(100)

else:
    st.warning("No cow detected")
