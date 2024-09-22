import mysql.connector
import streamlit as st


#establishing connection

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Abel3418!@",
    database = "project"
)
mycursor = mydb.cursor()
print("Connection established")