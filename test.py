# Import python packages
from snowflake.snowpark import Session
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError
import streamlit as st
from snowflake.snowpark.context import get_active_session
from pathlib import Path
import base64

# if 'layout_preference' not in st.session_state:
#     st.session_state['layout_preference'] = 'wide'
#     st.set_page_config(page_title="Web Application", page_icon=":bulb:", layout=st.session_state['layout_preference'])

def create_session():
    return Session.builder.configs(st.secrets["snowflake"]).create()

session = create_session()

# Write directly to the app
# def img_to_bytes(img_path):
#     img_bytes = Path(img_path).read_bytes()
#     encoded = base64.b64encode(img_bytes).decode()
#     return encoded

st.image("logo.png")
#st.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=200 height=100>]'''.format(img_to_bytes("logo.png")), unsafe_allow_html=True)
st.header("Team : Saama Thunder's") 
st.title("Welcome to Streamlit in Snowflake")

status = st.radio("Select One of the Stage: ", ('Internal Stage', 'External Stage(S3)','Named Stage'))

# conditional statement to print 
if (status == 'Internal Stage'):
    st.success("You have selected Internal Stage")
elif (status=='External Stage(S3)'):
    st.success("You have selected External Stage(S3)")
elif(status=='Named Stage'):
    st.success("You have selected Named Stage")
else:
    st.info("You haven't selected anything")

if status == "Internal Stage":
    st.subheader("There are no files in Internal Stage")

if status == "Named Stage":
    st.subheader("There are no files in Named Stage")

if status == "External Stage(S3)":
    st.subheader("External Stage Files:")

df = session.sql("LIST @STORE_DB.ATLAS.AWS_S3_STG")



