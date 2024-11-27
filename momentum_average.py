import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, date

st.set_page_config(page_title='Momentum Portfolio', layout='wide')
st.title('Momentum Portfolio')

# Input widgets
start_date = st.date_input('Start Date', value=date( 2020, 1, 1 ))
end_date = st.date_input('End Date', value=date( 2023, 12, 31 ))
tickers = st.text_input('Enter 5 Tickers (comma-separated)', value='AAPL, MSFT, GOOGL, AMZN, META')

def get_data( start_date, end_date, tickers ):
    ticker_list = [ ticker.strip() for ticker in tickers.split(',') ]
    all_data = {}
    
    for ticker in ticker_list:
        # Download more data to calculate 5-month growth
        df = yf.download( ticker, start=start_date, end=end_date )
        
        # Calculate 5-month growth using the full dataset
        growth = df['Close'].pct_change(periods=110) * 100
        
        # Get the last 5 days of data and add growth
        last_5_days = df[['Open', 'High', 'Low', 'Close']].tail(5)
        last_5_days['5M Growth'] = growth.tail(5)
        
        all_data[ticker] = last_5_days
    
    return all_data

if tickers:
    # Get data for each ticker
    ticker_data = get_data( start_date, end_date, tickers )
    
    # Create 5 columns
    cols = st.columns(5)
    
    # Display each ticker's data in its own column
    for idx, (ticker, data) in enumerate(ticker_data.items()):
        with cols[idx]:
            st.subheader(ticker)
            st.dataframe(data.round(2))
