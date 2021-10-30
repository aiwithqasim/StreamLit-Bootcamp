import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

# Add text and data
st.title("My First Task on Streamlit")

# You can use specific text functions to add content to your app, or you can use st.write() and add your own markdown.
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

# There are other data specific functions like st.dataframe() and st.table() that you can also use for displaying data.

