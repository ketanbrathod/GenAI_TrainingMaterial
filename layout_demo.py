import streamlit as st
import numpy as np

st.title("Layout Demo")

# Sidebar
st.header("Sidebar Elements")
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

st.write(f"Contact method: {add_selectbox}")
st.write(f"Selected range: {add_slider}")

# Columns
st.header("Columns Layout")
left_column, right_column = st.columns(2)

# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin")
    )
    st.write(f"You are in {chosen} house!")

# Three columns example
st.header("Three Columns Example")
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Column 1")
    st.write("This is column 1")
    st.metric("Temperature", "70°F", "1.2°F")

with col2:
    st.header("Column 2")
    st.write("This is column 2")
    st.metric("Humidity", "60%", "-2%")

with col3:
    st.header("Column 3")
    st.write("This is column 3")
    st.metric("Pressure", "1013 hPa", "0.5 hPa")

# Expandable sections
st.header("Expandable Sections")
with st.expander("See explanation"):
    st.write("""
        This is some content that can be expanded or collapsed.
        You can put any Streamlit elements inside an expander!
    """)
    
    chart_data = np.random.randn(20, 3)
    st.line_chart(chart_data)

# Container
st.header("Container Example")
container = st.container()
container.write("This is written to a container")

# You can add elements to container later
st.write("This is outside the container")

# Add more to the container
container.write("This is also in the container")