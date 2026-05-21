import streamlit as st  
# from db import conn,cursor
# import cloudinary
# import cloudinary.uploader


# cloudinary.config(
#     cloud_name=st.secrets["cloud_name"],
#     api_key=st.secrets["api_key"],
#     api_secret=st.secrets["api_secrets"]
# )


st.title("Media Platform")

login,signup=st.tabs(
                ["Login","SignUp"]  
                )
# if "user" not in st.session_state:
#     st.session_state.user=None
# def dashboard():
#     st.sidebar.sucess("welcome user") 
   
#     opt=st.sidebar.selectbox("choose:--)",["uploadFiles","viewfiles","Logout"] )
#     st.header("dashboard")
#     if opt == "uploadFiles":
#         st.header("upload yr files here")
#         choosedFile=st.file_uploader("choose file",type=["pdf","jpg","jpeg","png","mp3","mp4"]) 

#         if choosedFile: 
#             st.write(choosedFile.name)
#             st.write(choosedFile.type)
#         if "image" in choosedFile.type:
#             st.image(choosedFile)
#         elif "video" in choosedFile.type:
#             st.video(choosedFile)
#         elif "audio" in choosedFile.type:
#             st.audio(choosedFile)  
#         if st.button("upload file to cloudinary"):
#             uploaded_dict_obj=cloudinary.uploader.upload(choosedFile,resource_type="auto") 
#             url=uploaded_dict_obj["secure_url"]             
#             st.write(url)
#             st.write("file uploaded to cloudinary")         
#     elif opt == "Logout":
#         st.session_state.user=None
#         st.success("logout successfully...")
#         st.rerun()        
    
        
    

with login:
    st.header("Login")
    with st.form("Login_Form"):
        email=st.text_input("Email")
        password=st.text_input("Password",type="password")
        btn=st.form_submit_button("Login")
      
        # if btn:
        #     query="select * from users where email=%s and password=%s"
        #     values=(email,password)
        #     cursor.execute(query,values)
        #     loggedin_user=cursor.fetchone()
        #     st.session_state.user=loggedin_user
        #     st.write("loggedin successfully")
        #     st.rerun()
     
                
      
        
with signup:
    st.header("SignUp")
    with st.form("SignUp_form"):
        name=st.text_input("Name")
        Email=st.text_input("Email")
        password=st.text_input("Password",type="password")
        btn=st.form_submit_button("SignUp")
     
        # if btn:
        #     query="insert into users(name,Email,password) values=(%s,%s,%s)"
        #     values=(name,Email,password)
        #     cursor.execute(query,values)
        #     conn.commit()
        #     st.write("student added successfully ")
     
# if st.session_state.user==None:
#     login,signup=st.tabs(
#                 ["Login","SignUp"]  
#                 )
#     with signup:
#         signup_function()
#     with login:
#         login_function()   
        
        
# else:
#     dashboard()    
               
