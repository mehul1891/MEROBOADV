#!/usr/bin/env python
# This module is written by Mehul Oswal. 
# This module will be called to action in stock_pull.py script 

# ChangeLog
# 05-22-2016: For now, this module just reads a text file of sample tickers and returns an array.
# Eventually, this module will call another module to return an active list of tickers as an array


def retrieve_tickers(stocks):
	tickers = [];	
	if stocks == 'sp500':		
		with open('/Users/mehuloswal/meroboadv/tickers/current_sp500.dat','r+') as f:
			for line in f:
				tickers.append(line.rstrip())
			f.close()		
		return tickers	
	elif stocks == 'nyse':
		with open('/Users/mehuloswal/meroboadv/tickers/current_nyse.dat','r+') as f:
			for line in f:
				tickers.append(line.rstrip())
			f.close()		
		return tickers
	elif stocks == 'nasdaq':
		with open('/Users/mehuloswal/meroboadv/tickers/current_nasdaq.dat','r+') as f:
			for line in f:
				tickers.append(line.rstrip())
			f.close()		
		return tickers
	else:
		print "The input listing doesn't exist. No tickers retrieved. Please abort"
		exit()
# Below piece of code makes this module executable through the terminal window
if __name__ == "__main__":
    import sys
    retrieve_tickers(str(sys.argv[1]))			
		