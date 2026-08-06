import streamlit as st

# -- Principal Title Page --
st.title("Chi Square Graph")

colunas = st.columns(2)

with colunas[0]:
    st.header("Select parameters")
    degrees_of_freedom = st.slider(
        "Degrees of Freedom",
        min_value=0,
        max_value=30,
        value=0
    )
    st.write(f"Degrees_of_freedom: {degrees_of_freedom}")


