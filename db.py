import streamlit as st
import mysql.connector

conn = None
cursor = None

try:
    conn = mysql.connector.connect(
        host=st.secrets["MYSQL_HOST"],
        user=st.secrets["MYSQL_USER"],
        password=st.secrets["MYSQL_PASSWORD"],
        database=st.secrets["MYSQL_DB"],
        port=st.secrets["MYSQL_PORT"],
        auth_plugin='mysql_native_password',
        ssl_disabled=False
    )

    cursor = conn.cursor(dictionary=True)

    st.success("Database Connected Successfully")

except Exception as e:
    st.error(f"REAL ERROR: {e}")