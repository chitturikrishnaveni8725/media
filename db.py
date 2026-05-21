# import streamlit as st
# import mysql.connector

# conn = None
# cursor = None

# try:
#     conn = mysql.connector.connect(
#         host=st.secrets["MYSQL_HOST"],
#         user=st.secrets["MYSQL_USER"],
#         database=st.secrets["MYSQL_DB"],
#         password=st.secrets["MYSQL_PASSWORD"],
#         port=st.secrets["MYSQL_PORT"],
#         ssl_disabled=False
#     )

#     cursor = conn.cursor(dictionary=True)

#     st.success("Database connected successfully")

# except Exception as e:
#     st.error(f"ERROR: {e}")



import streamlit as st
import mysql.connector

conn = mysql.connector.connect(
    host=st.secrets["MYSQL_HOST"],
    user=st.secrets["MYSQL_USER"],
    password=st.secrets["MYSQL_PASSWORD"],
    database=st.secrets["MYSQL_DB"],
    port=st.secrets["MYSQL_PORT"],
    ssl_disabled=False
)

cursor = conn.cursor(dictionary=True)

st.success("Database Connected")