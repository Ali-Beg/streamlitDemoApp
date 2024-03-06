import pandas as pd 
import streamlit as st
import yfinance as yf
import datetime

st.write(
    """
    # Stock price analyser

    ## shown are the price of stocks
    """
)

# ticker_symbol = "AAPL"
ticker_symbol = st.text_input(
                    "Enter stock symbol",
                    "AAPL",
                    key="placeholder"
)

col1,col2 = st.columns(2)    # layouts and container

with col1:
    start_date=st.date_input("Enter start date",
                datetime.date(2019,1,1))
with col2:
    end_date=st.date_input("Enter end date",
                datetime.date(2022,12,31))

# ticker_symbol = "AAPL"

st.write(f"""
## {ticker_symbol}'s EOD prices
""")

ticket_data= yf.Ticker(ticker_symbol)
ticker_df = ticket_data.history(period="1d",
                                start=f"{start_date}",
                                end=f"{end_date}")

st.dataframe(ticker_df) #to show data frame on the application frontend



# showing chart
st.write(
    """
    ## Daily closing price chart
    """
)
st.line_chart(ticker_df.Close)

# showing chart
st.write("""
## Daily Volume of shares traded
""")
st.line_chart(ticker_df.Volume)
