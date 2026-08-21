import yfinance as yf
from google import genai
from google.genai import types
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

def backgroud(ticker):
    ticker = yf.Ticker(ticker)
    info = ticker.info
    

st.set_page_config(page_title='AI trader')

st.title('AI Trader')

ticker = st.text_area('Enter ticker symbol: ')

if st.button("Find info"):
    ticker = yf.Ticker(ticker.strip())
    info = ticker.info

    # Display clean, structured UI components
    st.subheader(info.get("longName"))

    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Sector:** {info.get('sector', 'N/A')}")
        st.write(f"**Industry:** {info.get('industry', 'N/A')}")
    with col2:
        st.write(f"**Headquarters:** {info.get('city')}, {info.get('state')}")
        st.write(f"**Website:** {info.get('website')}")

    st.markdown("**Business Summary:**")
    st.write(info.get("longBusinessSummary", "No summary available."))