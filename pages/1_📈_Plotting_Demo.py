import streamlit as st
import time
import numpy as np

# ----------------   THREE HEADERS ---------------------
st.set_page_config(page_title="Plotting Lab A", page_icon="📈")
st.markdown("# Plotting Lab B")
st.sidebar.header("Plotting Lab C")

st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

# ----------------   Setup Controls ---------------------
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()      # Later update with % complete
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

# ----------------   Setup Chart ---------------------
for i in range(1, 101):   # Create 500 numbers random
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
