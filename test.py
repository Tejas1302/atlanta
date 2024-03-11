# import python packages
from snowflake.snowpark import Session
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError
import streamlit as st 
from snowflake.snowpark.context import get_active_session

def create_session():
    return Session.builder.configs(st.secrets['snowflake']).create()

session = create_session()

# write directly to the app
st.title("Welcome to Streamlit in Snwoflake")
st.header("Saama Thunder's")
status = st.radio("Select One of the Stage: ",("Internal Stage", "External Stage(S3)","Named Stage"))

# conditional statement to print

if status == "Internal Stage":
    st.success("You have selected Internal Stage")
elif status == "External Stage(S3)":
    st.success("You have selected External Stage(S3)")
elif status == "Named Stage":
    st.success("You have selected Named Stage")
else:
    st.info("You haven't selected anything")

    