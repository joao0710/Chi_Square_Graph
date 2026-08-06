import streamlit as st

# -- Principal Title Page --
st.title("Chi Square Graph")

degrees_of_freedom = st.slider(
    "Degrees of Freedom",
    min_value=0,
    max_value=1,
    value=0
)


