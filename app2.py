import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np

judul = st.title("Login Form")
username = st.text_input("Username")
password = st.text_input("Password")

if st.button("Login"):
    if username == "eko" and password == "jati" :
        st.write("Welcome %s" %username)
    else:
        st.write("Hallo")

components.iframe("https://apilogy.id")