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

    price_stocks_df = get_data([symbol], pd.date_range(sd, ed))
    price_stocks_df.drop(columns=["SPY"], inplace=True)

    # 初始化交易DataFrame，其中'Symbol'和'Order'初始化为空字符串，'Shares'初始化为0
    df_trades = pd.DataFrame(index=price_stocks_df.index)
    df_trades['Symbol'] = ''
    df_trades['Order'] = ''
    df_trades['Shares'] = 0
    
    current_position = 0

    for i in range(len(price_stocks_df) - 1):
        current_price = price_stocks_df.iloc[i][symbol]
        next_price = price_stocks_df.iloc[i + 1][symbol]

        if next_price > current_price:
            if current_position <= 0:  # 如果当前持仓为0或持有空头仓位
                df_trades.at[df_trades.index[i], 'Symbol'] = symbol
                df_trades.at[df_trades.index[i], 'Order'] = 'BUY'
                df_trades.at[df_trades.index[i], 'Shares'] = 2000 if current_position == 0 else 1000
                current_position = 1000
        elif next_price < current_price:
            if current_position >= 0:  # 如果当前持仓为0或持有多头仓位
                df_trades.at[df_trades.index[i], 'Symbol'] = symbol
                df_trades.at[df_trades.index[i], 'Order'] = 'SELL'
                df_trades.at[df_trades.index[i], 'Shares'] = 2000 if current_position == 0 else 1000
                current_position = -1000
        else:
            # 如果价格未变，标记为"No action"
            df_trades.at[df_trades.index[i], 'Order'] = 'No action'
            df_trades.at[df_trades.index[i], 'Shares'] = 0

    # 过滤出进行了操作的天数，即Shares不为0的行
    #df_trades = df_trades[df_trades['Shares'] != 0]
    df_trades['Symbol'] = symbol  



    return df_trades
