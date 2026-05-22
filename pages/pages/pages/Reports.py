import streamlit as st
import pandas as pd

st.title(
"📊 Reports"
)

data = {
"Cow":[
"C01",
"C02",
"C03"
],

"Milk":[
10,
12,
15
]
}

df = pd.DataFrame(
data
)

st.bar_chart(
df.set_index(
"Cow"
)
)
