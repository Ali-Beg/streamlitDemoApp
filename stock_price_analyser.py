import pandas as pd 
import streamlit as st
import yfinance as yf


st.write(
    """
    # Stock price analyser

    #shown are the price of apple stock
    """
)

ticker_symbol = "AAPL"
ticket_data= yf.Ticker(ticker_symbol)
ticker_df = ticket_data.history(period="1d",
                                start="2019-01-01",
                                end="2022-12-31")

st.dataframe(ticker_df) #to show data frame on the application frontend

# showing chart
st.write(
    """
    ##Daily closing price chart
    """
)
st.line_chart(ticker_df.Close)

# showing chart
st.write("""
##Daily Volume of shares traded
""")
st.line_chart(ticker_df.Volume)
