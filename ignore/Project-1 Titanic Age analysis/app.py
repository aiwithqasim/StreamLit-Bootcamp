import streamlit as st
import pandas as pd 

st.write(
'''    # My First App
    Hello *world!* ''' 
)

df = pd.read_csv("./train_and_test2.csv")
st.line_chart(df.Age)