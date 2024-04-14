from dotenv import load_dotenv
load_dotenv() ##load all env variables from .env file

import os
import streamlit as st
import sqlite3

import google.generativeai as genai

# configure Genai key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## funvtion to load gemini model
def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question])
    return response.text

## function to retrieve query from database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

##define your prompt
prompt = [
    """
You are an expert in converting English questions to SQL query!
The SQL database has the name student and has the following columns: NAME , CLASS, SECTION 
\n\nFor example, \nExample 1 - How many enteries of records are present?,
the SQL command will be something like this SELECT COUNT(*) FROM student;
\nExample 2 - Tell me all students studying in science class?,
the SQL command will be something like this SELECT COUNT(*) FROM student 
where CLASS="science";
also the sql code should not have ''' in the beginning or end and sql word in output
"""
]

## streamlit App

st.set_page_config(page_title="SQL Converter", page_icon=":computer:")
st.header("SQL Converter App")

question = st.text_input("Input: ",key="input")
submit = st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question, prompt)
    response=read_sql_query(response,"student.db")
    st.subheader("The response is")
    for row in response:
        print(row)
        st.header(row)









