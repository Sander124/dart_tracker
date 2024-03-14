import streamlit as st
import pandas as pd
import pymongo
from pymongo import MongoClient
import warnings


warnings.filterwarnings("ignore")

client = MongoClient("mongodb+srv://sandersteur2:rJDCcg502peL5JS6@clustersander.yzcdzii.mongodb.net/?tls=true")

db = client['dart_tracker']
collection = db['dart_tracker']

st.set_page_config(
    page_title="Dart Tracker",
    page_icon="⚽",
)

st.markdown(
"""
## Dart Tracker of Sander Steur for Singles Training
"""
)
df = pd.DataFrame(list(collection.find()))
c1,c2,c3 = st.columns(3)
c1.metric("Total sessions", len(df))
c2.metric("Highest score", df['score'].max())
c3.metric('Average score', df['score'].mean())

st.line_chart(df[['session', 'score']], x='session', y='score')
st.line_chart(df[['session', 'percentage']], x='session', y='percentage')


with st.expander("Add new session"):
    with st.form("my_form"):
        score = st.number_input("Score achieved")
        percentage = st.number_input("Percentage hit", format="%.2f")
        single = st.number_input("Singles hit")
        double = st.number_input("Doubles hit")
        triple = st.number_input("Triples hit")

        submitted = st.form_submit_button("Submit")
        if submitted:
            collection.insert_one({"session": int(len(list(collection.find()))),'score': int(score), 
                                'percentage': percentage, 'single': int(single), 'double': int(double), 
                                'triple': int(triple)})
            
