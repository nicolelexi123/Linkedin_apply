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

def calculate_sma(df, symbol,period):
    sma=df[symbol].rolling(window=period).mean()
    return sma

def calculate_Momentum(df,symbol,period):
    momentum = (df[symbol] / df[symbol].shift(period)) - 1
    return momentum

def calculate_BB(df,symbol, period):
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



def calculate_rsi(df,symbol, window=14):
    diff = df[symbol].diff()
    gain = diff.clip(lower=0)
    loss = -diff.clip(upper=0)

    avg_gain = gain.ewm(alpha=1/window, min_periods=window).mean()
    avg_loss = loss.ewm(alpha=1/window, min_periods=window).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

   

    return rsi



def run(df, symbol):
    # Assuming 'Close' is the symbol for price data in df
    # Normalize the price data for comparison
    normalized_price = df[symbol] / df[symbol].iloc[0]

    # Calculate indicators
    sma_series = calculate_sma(df, symbol, 20) / df[symbol].iloc[0]
    momentum_series = calculate_momentum(df, symbol, 14)
    bb_percentage_series = calculate_bb_percentage(df, symbol, 20)
    PPI_series = calculate_PPI_value(df, symbol, 12, 26)
    rsi_series = calculate_rsi(df, symbol, 14)

    # Plotting
    fig, axs = plt.subplots(5, 1, figsize=(10, 15), sharex=True)

    axs[0].plot(normalized_price, label='Normalized Price')
    axs[0].plot(sma_series, label='Normalized SMA', linestyle='--')
    axs[0].set_title('Price and SMA')
    axs[0].legend()

    axs[1].plot(momentum_series, label='Momentum')
    axs[1].set_title('Momentum')
    axs[1].axhline(0, color='black', linestyle='--')
    axs[1].legend()

    axs[2].plot(bb_percentage_series, label='BB Percentage')
    axs[2].set_title('Bollinger Bands Percentage')
    axs[2].legend()

    axs[3].plot(PPI_series, label='PPI')
    axs[3].set_title('PPI')
    axs[3].legend()

    axs[4].plot(rsi_series, label='RSI')
    axs[4].set_title('RSI')
    axs[4].axhline(70, color='red', linestyle='--', label='Overbought')
    axs[4].axhline(30, color='green', linestyle='--', label='Oversold')
    axs[4].legend()

    plt.xlabel('Time')
    plt.tight_layout()
    plt.show()


