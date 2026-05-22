import streamlit as st

st.title(
"🥛 Milk Record"
)

cow = st.text_input(
"Cow ID"
)

morning = st.number_input(
"Morning Milk (L)"
)

evening = st.number_input(
"Evening Milk (L)"
)

total = morning + evening

st.write(
"Total Milk:",
total,
"L"
)

if st.button(
"Save Record"
):

    st.success(
    "Saved"
    )
