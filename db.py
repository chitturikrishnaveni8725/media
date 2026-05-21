import streamlit as st
import mysql.connector
conn=mysql.connector.connect(
    
    
    host=st.secrets["MYSQL_HOST"],
    user=st.secrets["MYSQL_USER"],
    database=st.secrets["MYSQL_DB"],
    password=st.secrets["MYSQL_PASSWORD"],
    port=st.secrets["MYSQL_PORT"]
    
)


cursor=conn.cursor(dictionary=True)
if conn.is_connected():
    st.success("Database Connected Successfully")
    
cursor.execute("""
               create table if not exists  users(
                   id int primary key auto_increment,
                   name varchar(50) not null,
                   email varchar(50) unique,
                   password varchar(50) not null
               )
               
               """)



cursor.execute("""
               create table if not exists files(
                   id int primary key auto_increment,
                   user_id int,
                   file_name varchar(255),
                   file_type varchar(100),
                   file_url text,
                   upload_date timestamp default current_timestamp,
                   foreign key(user_id) references users(id)
               )
               
               """)
conn.commit()
cursor.execute("SHOW TABLES") 
print(cursor.fetchall()) 
cursor.execute("DESC users")   # here desc is used to show the structure of  table
print(cursor.fetchall())

print("table created successfully")
