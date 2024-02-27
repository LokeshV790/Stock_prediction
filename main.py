import streamlit as st
from datetime import date

import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

st.title('Stock Price Prediction')


# Data fetching
START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

stocks = ('SBIN.NS', 'TCS.NS', 'TECHM.NS', 'LT.NS', 'DMART.NS')
selected_stock = st.selectbox('Select dataset for prediction', stocks)

n_years = st.slider('Years of prediction:', 1, 10)
period = n_years * 365 

def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

data_load_state = st.text('Loading')
data = load_data(selected_stock)
data_load_state.text('Done..!')

