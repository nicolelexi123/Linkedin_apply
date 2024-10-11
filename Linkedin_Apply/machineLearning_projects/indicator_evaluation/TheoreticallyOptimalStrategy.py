import pandas as pd
import matplotlib.pyplot as plt 
import datetime as dt
from util import get_data

def author():  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    :return: The GT username of the student  		  	   		 	   			  		 			     			  	 
    :rtype: str  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    return "xi6"  # Change this to your user ID 



def testPolicy(symbol, sd, ed, sv):

    """
    Code implementing a TheoreticallyOptimalStrategy. It should implement testPolicy(), which returns a trades Pandas.DataFrame

    Parameters
        symbol    - the stock symbol to act on
        sd        - A DateTime object that represents the start date
        ed        - A DateTime object that represents the end date
        sv        - Start value of the portfolio

    Returns
        A single column data frame, indexed by date, whose values represent trades for each trading day 
       (from the start date to the end date of a given period). Legal values are +1000.0 indicating a BUY 
       of 1000 shares, -1000.0 indicating a SELL of 1000 shares, and 0.0 indicating NOTHING. Values of +2000 
       and -2000 for trades are also legal so long as net holdings are constrained to -1000, 0, and 1000. 
       Note: The format of this data frame differs from the one developed in a prior project.   

    Return Type
        pandas.DataFrame
    """
    '''
    price_stocks_df=get_data([symbol],pd.date_range(sd,ed))
    price_stocks_df.drop(columns=["SPY"], inplace=True)
    print (price_stocks_df)

    # initialize an empty dataframe for trades and then assume before the price reaches the highest point, you did not sell ; before the price touch the lowest point, you did not buy.
    df_trades=pd.DataFrame(index=price_stocks_df.index,data=0.0,columns=[symbol])
    current_position=0
    print(df_trades)

    for i in range(len(price_stocks_df)-1):
        if price_stocks_df.iloc[i+1][symbol]>price_stocks_df.iloc[i][symbol]:
            if current_position<=0: # short 
                df_trades.loc[df_trades.index[i], symbol] = 2000
                current_position=1000

        elif price_stocks_df.iloc[i+1][symbol]<price_stocks_df.iloc[i][symbol]:
            if current_position>=0: # long
                df_trades.loc[df_trades.index[i], symbol] = -2000
                print(df_trades)
                current_position=-1000
        
        #df_trades.iloc[i]=0 was inital to 0 at the beginning    

    return df_trades
    '''
    price_stocks_df = get_data([symbol], pd.date_range(sd, ed))
    price_stocks_df.drop(columns=["SPY"], inplace=True)
    print(price_stocks_df)

    df_trades = pd.DataFrame(index=price_stocks_df.index, data=0.0, columns=[symbol])
    current_position = 0

    print(df_trades)

    for i in range(len(price_stocks_df) - 1):
        if price_stocks_df.iloc[i + 1][symbol] > price_stocks_df.iloc[i][symbol]:
            if current_position == 0:  # 没有持仓时,只能买入1000股
                df_trades.loc[df_trades.index[i], symbol] = 1000
                current_position = 1000
            elif current_position == -1000:  # 已持有空头头寸,需要先平仓再买入
                df_trades.loc[df_trades.index[i], symbol] = 2000
                current_position = 1000
        elif price_stocks_df.iloc[i + 1][symbol] < price_stocks_df.iloc[i][symbol]:
            if current_position == 0:  # 没有持仓时,只能卖出1000股
                df_trades.loc[df_trades.index[i], symbol] = -1000
                current_position = -1000
            elif current_position == 1000:  # 已持有多头头寸,需要先平仓再卖出
                df_trades.loc[df_trades.index[i], symbol] = -2000
                current_position = -1000

    print(df_trades)
    return df_trades

        
