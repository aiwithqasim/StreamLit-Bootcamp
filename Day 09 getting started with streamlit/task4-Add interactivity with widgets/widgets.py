import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

# Add text and data
st.title("My First App")

# You can use specific text functions to add content to your app, or you can use st.write() and add your own markdown.
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

# There are other data specific functions like st.dataframe() and st.table() that you can also use for displaying data.

# You can also write to your app without calling any Streamlit methods.
# Streamlit supports “magic commands,” which means you don’t have to use st.write() at all!
# Try replacing the code above with this snippet:

"""
## Again making heading with magic command
Here's our first attempt at using data to create a table using simple pandas code:
"""

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

# You can easily add a line chart to your app with st.line_chart().
# We’ll generate a random sample using Numpy and then chart it.
"""
## Draw charts and maps
"""
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# With st.map() you can display data points on a map.
# Let’s use Numpy to generate some sample data and plot it on a map of San Francisco.

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

"""
## Add interactivity with widgets
### Use checkboxes to show/hide data
"""
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

"""
### Use a select box for options
"""

option = st.selectbox(
    'Which number do you like best?',
    df['first column'])

'You selected: ', option



 



