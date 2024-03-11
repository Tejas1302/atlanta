# import python packages
from snowflake.snowpark import session
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError
import streamlit as st 
from snowflake.snowpark.context import get_active_session

def create_session():
    return session.builder.configs(st.secrets['snowflake']).create()

session = create_session()

#write directly to the app
st.title("Welcome to Streamlit in Snwoflake")