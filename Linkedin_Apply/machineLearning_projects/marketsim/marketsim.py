""""""  		  	   		 	   			  		 			     			  	 
"""MC2-P1: Market simulator.  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		 	   			  		 			     			  	 
Atlanta, Georgia 30332  		  	   		 	   			  		 			     			  	 
All Rights Reserved  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
Template code for CS 4646/7646  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		 	   			  		 			     			  	 
works, including solutions to the projects assigned in this course. Students  		  	   		 	   			  		 			     			  	 
and other users of this template code are advised not to share it with others  		  	   		 	   			  		 			     			  	 
or to make it available on publicly viewable websites including repositories  		  	   		 	   			  		 			     			  	 
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	   			  		 			     			  	 
or edited.  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
We do grant permission to share solutions privately with non-students such  		  	   		 	   			  		 			     			  	 
as potential employers. However, sharing with other current or future  		  	   		 	   			  		 			     			  	 
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		 	   			  		 			     			  	 
GT honor code violation.  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
-----do not edit anything above this line---  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
Student Name: Xi Le (replace with your name)  		  	   		 	   			  		 			     			  	 
GT User ID: Xi6 (replace with your User ID)  		  	   		 	   			  		 			     			  	 
GT ID: 903941473 (replace with your GT ID)  		  	   		 	   			  		 			     			  	 
"""  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
import datetime as dt  		  	   		 	   			  		 			     			  	 
import os  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
import numpy as np  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
import pandas as pd  		  	   		 	   			  		 			     			  	 
from util import get_data, plot_data  

def author():  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    :return: The GT username of the student  		  	   		 	   			  		 			     			  	 
    :rtype: str  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    return "xi6"  # Change this to your user ID  	
  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
def compute_portvals(  		  	   		 	   			  		 			     			  	 
    orders_file="./orders/orders.csv",  		  	   		 	   			  		 			     			  	 
    start_val=1000000,  		  	   		 	   			  		 			     			  	 
    commission=9.95,  		  	   		 	   			  		 			     			  	 
    impact=0.01,  		  	   		 	   			  		 			     			  	 
):  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    Computes the portfolio values.  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    :param orders_file: Path of the order file or the file object  		  	   		 	   			  		 			     			  	 
    :type orders_file: str or file object  		  	   		 	   			  		 			     			  	 
    :param start_val: The starting value of the portfolio  		  	   		 	   			  		 			     			  	 
    :type start_val: int  		  	   		 	   			  		 			     			  	 
    :param commission: The fixed amount in dollars charged for each transaction (both entry and exit)  		  	   		 	   			  		 			     			  	 
    :type commission: float  		  	   		 	   			  		 			     			  	 
    :param impact: The amount the price moves against the trader compared to the historical data at each transaction  		  	   		 	   			  		 			     			  	 
    :type impact: float  		  	   		 	   			  		 			     			  	 
    :return: the result (portvals) as a single-column dataframe, containing the value of the portfolio for each trading day in the first column from start_date to end_date, inclusive.  		  	   		 	   			  		 			     			  	 
    :rtype: pandas.DataFrame  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    # this is the function the autograder will call to test your code  		  	   		 	   			  		 			     			  	 
    # NOTE: orders_file may be a string, or it may be a file object. Your  		  	   		 	   			  		 			     			  	 
    # code should work correctly with either input  		  	   		 	   			  		 			     			  	 
    # TODO: Your code here 
    	
    orders_df=pd.read_csv(orders_file,index_col='Date',parse_dates=True,na_values=['nan'])	
    orders_df.sort_index(inplace=True)
    start_date=orders_df.index[0]
    end_date=orders_df.index[-1]
    #print(orders_df)
    
    symbols_list=list(set(orders_df['Symbol'].values))
    price_stocks_df=get_data(symbols_list,pd.date_range(start_date,end_date))
    
    #print(price_stocks_df)
   # do I need to add cash? here 

    # create holding table and change to holding table
    holding_pd=pd.DataFrame(index=price_stocks_df.index,columns=symbols_list,dtype=float)
    holding_pd=holding_pd.fillna(0)
    holding_pd['Cash']=float(0)
    holding_pd['Cash'][0]=float(start_val)
    for index,row in orders_df.iterrows():
        date=row.name
        symbol=row['Symbol']
        order_type=row['Order']
        share_num=row['Shares']
        stock_price=price_stocks_df.at[date,symbol]

        if order_type=='BUY':
            holding_pd.at[date,symbol]+=share_num
            aa=holding_pd.at[date,'Cash']
            aa-=float(stock_price*(1+impact)*abs(share_num))
            pd.set_option('display.precision', 10)
            holding_pd.at[date,'Cash'] =aa
            holding_pd.at[date,'Cash']-=commission
        elif order_type=='SELL':
            holding_pd.at[date,symbol]-=share_num
            holding_pd.at[date,'Cash']+=stock_price*(1-impact)*abs(share_num)
            #print(holding_pd.head(5))
            holding_pd.at[date,'Cash']-=commission
    
    #print(holding_pd)
    
    
    holding_pd_cum=holding_pd.cumsum()
    
    holding_pd_cum['Portfolio Value']=float(0)
    for date in holding_pd_cum.index:
        shares=holding_pd_cum.loc[date,symbols_list]
        print(shares)
        prices=price_stocks_df.loc[date,symbols_list]
        print(prices)
        stock_value=shares*prices
        print(stock_value)
        total_stock_value=stock_value.sum()
        cash=holding_pd_cum.at[date,'Cash']
        holding_pd_cum.at[date,'Portfolio Value']=total_stock_value+cash
    portvals=holding_pd_cum[['Portfolio Value']]

    return portvals 

        
        
        
            


  		  	   		 	   			  		 			     			  	 
    # In the template, instead of computing the value of the portfolio, we just  		  	   		 	   			  		 			     			  	 
    # read in the value of IBM over 6 months  		  	   		 	   			  		 			     			  	 
    '''
    start_date = dt.datetime(2008, 1, 1)  		  	   		 	   			  		 			     			  	 
    end_date = dt.datetime(2008, 6, 1)  		  	   		 	   			  		 			     			  	 
    portvals = get_data(["IBM"], pd.date_range(start_date, end_date))  		  	   		 	   			  		 			     			  	 
    portvals = portvals[["IBM"]]  # remove SPY  		  	   		 	   			  		 			     			  	 
    rv = pd.DataFrame(index=portvals.index, data=portvals.values)  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    return rv  		  	   		 	   			  		 			     			  	 
    return portvals  		  	   		 	   			  		 			     			  	 
  	'''

  		  	   		 	   			  		 			     			  	 
def test_code():  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    Helper function to test code  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    # this is a helper function you can use to test your code  		  	   		 	   			  		 			     			  	 
    # note that during autograding his function will not be called.  		  	   		 	   			  		 			     			  	 
    # Define input parameters  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    of = "./orders/orders-10.csv"  		  	   		 	   			  		 			     			  	 
    sv = 1000000  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    # Process orders  		  	   		 	   			  		 			     			  	 
    portvals = compute_portvals(orders_file=of, start_val=sv)  		  	   		 	   			  		 			     			  	 
    if isinstance(portvals, pd.DataFrame):  		  	   		 	   			  		 			     			  	 
        portvals = portvals[portvals.columns[0]]  # just get the first column  		  	   		 	   			  		 			     			  	 
    else:  		  	   		 	   			  		 			     			  	 
        "warning, code did not return a DataFrame"  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    # Get portfolio stats  		  	   		 	   			  		 			     			  	 
    # Here we just fake the data. you should use your code from previous assignments.  		  	   		 	   			  		 			     			  	 
    start_date = dt.datetime(2008, 1, 1)  		  	   		 	   			  		 			     			  	 
    end_date = dt.datetime(2008, 6, 1)  		  	   		 	   			  		 			     			  	 
    cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = [  		  	   		 	   			  		 			     			  	 
        0.2,  		  	   		 	   			  		 			     			  	 
        0.01,  		  	   		 	   			  		 			     			  	 
        0.02,  		  	   		 	   			  		 			     			  	 
        1.5,  		  	   		 	   			  		 			     			  	 
    ]  		  	   		 	   			  		 			     			  	 
    cum_ret_SPY, avg_daily_ret_SPY, std_daily_ret_SPY, sharpe_ratio_SPY = [  		  	   		 	   			  		 			     			  	 
        0.2,  		  	   		 	   			  		 			     			  	 
        0.01,  		  	   		 	   			  		 			     			  	 
        0.02,  		  	   		 	   			  		 			     			  	 
        1.5,  		  	   		 	   			  		 			     			  	 
    ]  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    # Compare portfolio against $SPX  		  	   		 	   			  		 			     			  	 
    print(f"Date Range: {start_date} to {end_date}")  		  	   		 	   			  		 			     			  	 
    print()  		  	   		 	   			  		 			     			  	 
    print(f"Sharpe Ratio of Fund: {sharpe_ratio}")  		  	   		 	   			  		 			     			  	 
    print(f"Sharpe Ratio of SPY : {sharpe_ratio_SPY}")  		  	   		 	   			  		 			     			  	 
    print()  		  	   		 	   			  		 			     			  	 
    print(f"Cumulative Return of Fund: {cum_ret}")  		  	   		 	   			  		 			     			  	 
    print(f"Cumulative Return of SPY : {cum_ret_SPY}")  		  	   		 	   			  		 			     			  	 
    print()  		  	   		 	   			  		 			     			  	 
    print(f"Standard Deviation of Fund: {std_daily_ret}")  		  	   		 	   			  		 			     			  	 
    print(f"Standard Deviation of SPY : {std_daily_ret_SPY}")  		  	   		 	   			  		 			     			  	 
    print()  		  	   		 	   			  		 			     			  	 
    print(f"Average Daily Return of Fund: {avg_daily_ret}")  		  	   		 	   			  		 			     			  	 
    print(f"Average Daily Return of SPY : {avg_daily_ret_SPY}")  		  	   		 	   			  		 			     			  	 
    print()  		  	   		 	   			  		 			     			  	 
    print(f"Final Portfolio Value: {portvals[-1]}")  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
if __name__ == "__main__":  		  	   		 	   			  		 			     			  	 
    test_code()  		  	   		 	   			  		 			     			  	 
