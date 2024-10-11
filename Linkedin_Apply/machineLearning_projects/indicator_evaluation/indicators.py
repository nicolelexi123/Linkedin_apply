from util import get_data
import pandas as pd  
import matplotlib.pyplot as plt 
import datetime as dt

def author():  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    :return: The GßT username of the student  		  	   		 	   			  		 			     			  	 
    :rtype: str  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    return "xi6"  # Change this to your user ID 

def calculate_sma_price(df,symbol,period=20):
    sma=df[symbol].rolling(window=period).mean()
    dif=df[symbol]/sma
    return dif

def calculate_Momentum(df,symbol,period=14):
    momentum = (df[symbol] / df[symbol].shift(period)) - 1
    return momentum

def calculate_BB(df,symbol, period=20):
    sma=df[symbol].rolling(window=period).mean()
    std=df[symbol].rolling(window=period).std()
    bb_upper = sma + (std * 2)
    bb_lower = sma - (std * 2)
    bb_percentage = ((df[symbol] - bb_lower) / (bb_upper - bb_lower)) * 100
   
    bb_value=(df[symbol]-sma)/(2*std)
    return bb_percentage

# percentage price indicator

def calculate_PPI(df, symbol,short_period=12, long_period=26, signal_period=9):

    short_ema = df[symbol].ewm(span=short_period, adjust=False).mean()
    long_ema = df[symbol].ewm(span=long_period, adjust=False).mean()

    # Calculate the PPI
    ppi = ((short_ema - long_ema) / long_ema) * 100

    # Calculate the signal line
    #df['PPI_Signal'] = df['PPI'].ewm(span=signal_period, adjust=False).mean()

    # Optionally, calculate the histogram
    #df['PPI_Histogram'] = df['PPI'] - df['PPI_Signal']
    
    return ppi


'''
def calculate_rsi(df,symbol, window=14):
    diff = df[symbol].diff()
    gain = diff.clip(lower=0)
    loss = -diff.clip(upper=0)

    avg_gain = gain.ewm(alpha=1/window, min_periods=window).mean()
    avg_loss = loss.ewm(alpha=1/window, min_periods=window).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    
    # 平滑StochRSI以获取K线值，然后将其缩放到0-100范围
   
    
    return rsi

'''

def calculate_ema_price(df, symbol, window=14):
   
   
    alpha = 2 / (window + 1)
    
    ema = df[symbol].ewm(alpha=alpha, adjust=False).mean()
    price_ema=df[symbol]/ema

    return price_ema



