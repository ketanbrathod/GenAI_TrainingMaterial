import streamlit as st
import time
import numpy as np

st.title("Progress Bar Demo")

st.header("Basic Progress Bar")
if st.button("Start Long Computation"):
    st.write('Starting a long computation...')
    
    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)
    
    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.05)  # Reduced sleep time for demo
    
    st.write('...and now we\'re done!')
    st.success("Computation completed!")

st.header("Progress with Data Processing")
if st.button("Process Data"):
    data = []
    progress_text = 'Processing data...'
    my_bar = st.progress(0, text=progress_text)
    
    for percent_complete in range(100):
        time.sleep(0.02)
        # Simulate data processing
        data.append(np.random.randn())
        my_bar.progress(percent_complete + 1, text=f'Processing... {percent_complete + 1}%')
    
    my_bar.empty()  # Remove progress bar
    
    st.success("Data processing complete!")
    st.line_chart(data)

st.header("Spinner Demo")
if st.button("Show Spinner"):
    with st.spinner('Wait for it...'):
        time.sleep(2)
    st.success('Done!')

st.header("Status Messages")
status_col1, status_col2, status_col3 = st.columns(3)

with status_col1:
    if st.button("Success"):
        st.success("This is a success message!")

with status_col2:
    if st.button("Warning"):
        st.warning("This is a warning message!")

with status_col3:
    if st.button("Error"):
        st.error("This is an error message!")

if st.button("Info"):
    st.info("This is an info message!")

# Balloons and snow for celebration
st.header("Celebration Effects")
celebration_col1, celebration_col2 = st.columns(2)

with celebration_col1:
    if st.button("🎈 Balloons"):
        st.balloons()

with celebration_col2:
    if st.button("❄️ Snow"):
        st.snow()