import streamlit as st

st.title("🐄 Add Cow")

cow_id = st.text_input("Cow ID")

cow_name = st.text_input(
"Cow Name"
)

breed = st.selectbox(
"Breed",
[
"Jersey",
"Holstein",
"Gir"
]
)

age = st.number_input(
"Age",
1,20
)

health = st.selectbox(
"Health Status",
[
"Healthy",
"Sick"
]
)

if st.button(
"Save Cow"
):

    st.success(
    "Cow Added Successfully"
    )
