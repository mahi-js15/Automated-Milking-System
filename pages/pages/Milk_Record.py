import streamlit as st

st.title("🥛 Milk Record")

cow_id = st.text_input("Cow ID")

milk = st.number_input(
    "Milk Quantity (Liters)",
    min_value=0.0
)

if st.button("Save Record"):
    st.success(
        f"Milk record saved: {milk} L from {cow_id}"
    )
