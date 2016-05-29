#!/usr/bin/env python

# Created by Mehul Oswal on May 21st - 22nd 2016

# Purpose
	# 1. Access Yahoo Finance API
	# 2. Retrieve stock data
	# 3. Run at a set time every day

# Import relevant libraries

	# This is to manipulate the data structure
import pandas as pd 

	# This is to call the API to get the data
from pandas_datareader.data import DataReader 

	# This is to specify the date of snapshot
import datetime 

	# This is to call the list of active tickers in different exchanges (S&P500, NYSE and NASDAQ) 
import retrieve_tickers

# import matplotlib.pyplot as plt

# 1. Access Yahoo Finance API
portfolio_equities = ['AMZN','TSLA','SMDV']
num_shares = [1, 1, 1]

# Moving date window of 2 weeks
mov_dt_window = datetime.timedelta(days=14)
end_date = datetime.date.today()
start_date = end_date - mov_dt_window

port_trend = []
port_close = []
port = []
#def port_perf(portfolio_equities, start_date, end_date):
#stocks_list = 'sp500'
#tickers = retrieve_tickers.retrieve_tickers(stocks_list)
#td = datetime.datetime.now().strftime('%Y-%m-%d')


# Write 2 DataFrames
for i in portfolio_equities:
	port =  DataReader(i, "yahoo", start_date, end_date)
	#port['Date'] = port.index
	port['Symbol'] = i
	port_close.append(port.tail(1))
print port_close['Symbol']

#port = DataReader(portfolio_equities, "yahoo", start_date, end_date)	
#print port.to_frame()


# 2. Retrieve stock data








# 3. Run at a set time every day