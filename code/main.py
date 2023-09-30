
from datetime import date as dt
import yfinance as yf
from plotly import graph_objs as go

import stramlit as st
from fbprophet import Prophet
from fbprophet.plot import plt_plotly

# Global varables
START = '2015-01-01'
END = dt.today().strftime("%Y-%m-%d")

st.title('Stocke Prediction App')

stocks=('PFE','AMD','DIS','HSY','NKE','JD')
selected_stocks= st.selectbox("Select Dataset for Prediciton",stocks)

n_years= st.slider('Years of Prediction:',1,4)
period = n_years * 365
