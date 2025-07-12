import streamlit as st
import numpy as np
import pandas as pd

st.title("Data Display Methods Demo")

# Using st.write()
st.header("Using st.write()")
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

# Using st.dataframe() with random data
st.header("Interactive Dataframe with st.dataframe()")
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

# Using styled dataframe
st.header("Styled Dataframe")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20))
)
st.dataframe(dataframe.style.highlight_max(axis=0))

# Using st.table() for static table
st.header("Static Table with st.table()")
static_dataframe = pd.DataFrame(
    np.random.randn(5, 10),
    columns=('col %d' % i for i in range(10))
)
st.table(static_dataframe)