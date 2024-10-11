import datetime as dt  		  	   		 	   			  		 			     			  	 
import os  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
import numpy as np  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
import pandas as pd  	
import TheoreticallyOptimalStrategy as tos	  	   		 	   			  		 			     			  	 
from util import get_data, plot_data  

def author():  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    :return: The GT username of the student  		  	   		 	   			  		 			     			  	 
    :rtype: str  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    return "xi6"  # Change this to your user ID 

def compute_portvals(
    trades_df,  
    start_val,  
    commission,  # Fixed commission for each trade
    impact,  # Impact of trade on stock price
): 
    start_date = trades_df.index[0]
    end_date = trades_df.index[-1]
    
    # Assuming there is only one symbol
    symbol = trades_df.columns[0]
    symbols_list = [symbol]
    
    # Get stock data
    price_stocks_df = get_data(symbols_list, pd.date_range(start_date, end_date))
    price_stocks_df.fillna(method='ffill', inplace=True)  # Forward-fill any missing data
    #price_stocks_df.fillna(method='bfill', inplace=True)
    price_stocks_df.drop(columns=['SPY'], inplace=True)
    
    # Create holding table and change to holding table
    holding_pd = pd.DataFrame(index=price_stocks_df.index, columns=symbols_list, dtype=float)
    holding_pd = holding_pd.fillna(0)
    holding_pd['Cash'] = 0 #start_val  # Initialize cash column to starting value
    holding_pd['Cash'][0] = start_val
    for date, trade in trades_df.iterrows():
        trade_val = trade[symbol]
        stock_price = price_stocks_df.at[date, symbol]
        shares = trade_val
        transaction_cost = commission + (abs(shares) * stock_price * impact)
        
       
        holding_pd.at[date, symbol] += shares
        holding_pd.at[date, 'Cash'] -= shares * stock_price + transaction_cost if shares != 0 else 0
    
 
    holding_pd_cum = holding_pd.cumsum()
    
    
    holding_pd_cum['Portfolio Value'] = holding_pd_cum[symbol] * price_stocks_df[symbol] + holding_pd_cum['Cash']
    
    portvals=holding_pd_cum[['Portfolio Value']]
    
    return portvals








def statistics(df):
    daily_return=(df/df.shift(1))-1
    daily_return=daily_return.iloc[1:]
    cr=(df['Portfolio Value'].iloc[-1] / df['Portfolio Value'].iloc[0]) - 1
    adr=daily_return.values.mean()
    sddr=daily_return.values.std()
    rfr=0
    sr=((adr-rfr)/sddr)*np.sqrt(252)	
    results = {
        'Cumulative Return': cr,
        'Average Daily Return': adr,
        'Standard Deviation of Daily Return': sddr,
        'Sharpe Ratio': sr
    }

    # Convert the dictionary to a Series
    #results_series = pd.Series(results)

    return results


   
   