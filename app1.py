# # import streamlit as st  
# # from db import conn,cursor

# from db import conn, cursor
# import streamlit as st

# st.title("My App Running Successfully")




# login,signup=st.tabs(
#                 ["Login","SignUp"]  
#                 )

        
    

# with login:
#     st.header("Login")
#     with st.form("Login_Form"):
#         email=st.text_input("Email")
#         password=st.text_input("Password",type="password")
#         btn=st.form_submit_button("Login")
      
     
                
      
        
# with signup:
#     st.header("SignUp")
#     with st.form("SignUp_form"):
#         name=st.text_input("Name")
#         Email=st.text_input("Email")
#         password=st.text_input("Password",type="password")
#         btn=st.form_submit_button("SignUp")
        
# st.write("databse connected successfully")


from db import conn, cursor
import streamlit as st

st.title("Media Platform")

if cursor is not None:

    cursor.execute("SHOW TABLES")

    tables = cursor.fetchall()

    st.write(tables)

else:
    st.error("Database not connected")