""""""  		  	   		 	   			  		 			     			  	 
"""MC1-P2: Optimize a portfolio.  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
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
GT ID:  903941473 (replace with your GT ID)  		  	   		 	   			  		 			     			  	 
"""  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
import datetime as dt  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	
import numpy as np  	
import pandas as pd	
import math  	   		 	   			  		 			     			  	  		  	   		 	   			  		 			     			  	 
import matplotlib.pyplot as plt  		  	   		 	   			  		 			     			  	 
import pandas as pd  		  	   		 	   			  		 			     			  	 
from util import get_data, plot_data  		
from scipy.optimize import minimize as min_1   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
# This is the function that will be tested by the autograder  		  	   		 	   			  		 			     			  	 
# The student must update this code to properly implement the functionality  		  	   		 	   			  		 			     			  	 
def optimize_portfolio(  		  	   		 	   			  		 			     			  	 
    sd=dt.datetime(2008, 1, 1),  		  	   		 	   			  		 			     			  	 
    ed=dt.datetime(2009, 1, 1),  		  	   		 	   			  		 			     			  	 
    syms=["GOOG", "AAPL", "GLD", "XOM"],  		  	   		 	   			  		 			     			  	 
    gen_plot=False,  		  	   		 	   			  		 			     			  	 
):
    def portfolio_statistics(allocs,prices):
        normalized_price=prices/prices.iloc[0]

        norm_product = normalized_price*allocs
        port_val=norm_product.sum(axis=1)

        daily_return =(port_val/port_val.shift(1))-1
        daily_return=daily_return.iloc[1:]
        #daily_return=port_val.pct_change().dropna()
        cr=(port_val[-1]/port_val[0])-1
        adr=daily_return.mean()
        sddr=daily_return.std()
        sr=(adr/sddr)*np.sqrt(252)
        return cr,adr,sddr,sr
    def neg_sr(allocs,prices):
        _,_,_,sr=portfolio_statistics(allocs,prices)
        return -sr
    
    # constrains and bounds for this allocation
    def check_allocation(allocs):
        return 1-np.sum(allocs)
      		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    This function should find the optimal allocations for a given set of stocks. You should optimize for maximum Sharpe  		  	   		 	   			  		 			     			  	 
    Ratio. The function should accept as input a list of symbols as well as start and end dates and return a list of  		  	   		 	   			  		 			     			  	 
    floats (as a one-dimensional numpy array) that represents the allocations to each of the equities. You can take  		  	   		 	   			  		 			     			  	 
    advantage of routines developed in the optional assess portfolio project to compute daily portfolio value and  		  	   		 	   			  		 			     			  	 
    statistics.  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		 	   			  		 			     			  	 
    :type sd: datetime  		  	   		 	   			  		 			     			  	 
    :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		 	   			  		 			     			  	 
    :type ed: datetime  		  	   		 	   			  		 			     			  	 
    :param syms: A list of symbols that make up the portfolio (note that your code should support any  		  	   		 	   			  		 			     			  	 
        symbol in the data directory)  		  	   		 	   			  		 			     			  	 
    :type syms: list  		  	   		 	   			  		 			     			  	 
    :param gen_plot: If True, optionally create a plot named plot.png. The autograder will always call your  		  	   		 	   			  		 			     			  	 
        code with gen_plot = False.  		  	   		 	   			  		 			     			  	 
    :type gen_plot: bool  		  	   		 	   			  		 			     			  	 
    :return: A tuple containing the portfolio allocations, cumulative return, average daily returns,  		  	   		 	   			  		 			     			  	 
        standard deviation of daily returns, and Sharpe ratio  		  	   		 	   			  		 			     			  	 
    :rtype: tuple  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    # Read in adjusted closing prices for given symbols, date range  		  	   		 	   			  		 			     			  	 
    dates = pd.date_range(sd, ed)  		  	   		 	   			  		 			     			  	 
    prices_all = get_data(syms, dates)  # automatically adds SPY  		  	   		 	   			  		 			     			  	 
    prices = prices_all[syms]  # only portfolio symbols  		  	   		 	   			  		 			     			  	 
    prices_SPY = prices_all["SPY"]  # only SPY, for comparison later 
    


  		  	   		 	   			  		 			     			  	 
    # find the allocations for the optimal portfolio  		  	   		 	   			  		 			     			  	 
    # note that the values here ARE NOT meant to be correct for a test case  		  	   		 	   			  		 			     			  	 
    #allocs = np.asarray([0.2, 0.2, 0.3, 0.2, 0.1] )  
    # add code here to find the allocations  
    len_syms = len(syms)
    allocs = np.asarray([1 / len_syms for _ in range(len_syms)])
    
    # initial guess 
    inital_guess=allocs
    #constrain_p=({'type':'eq','fun':check_allocation})
    constrain_p= ({'type': 'eq', 'fun': check_allocation})

    bounds=[(0,1)]*len(syms)
    
    result = min_1(neg_sr,inital_guess,args=(prices,),method='SLSQP',bounds=bounds, constraints=constrain_p)
    allocs=result.x



    cr, adr, sddr, sr = [  		  	   		 	   			  		 			     			  	 
        0.25,  		  	   		 	   			  		 			     			  	 
        0.001,  		  	   		 	   			  		 			     			  	 
        0.0005,  		  	   		 	   			  		 			     			  	 
        2.1,  		  	   		 	   			  		 			     			  	 
    ]  # add code here to compute stats


    
    		  	   		 	   			  		 			     			  	 





    # Get daily portfolio value  		  	   		 	   			  		 			     			  	 
    # ??????/add code here to compute daily portfolio values
    
    normalized_price=prices/prices.iloc[0]
   
    normalized_port=normalized_price*allocs
    port_val=normalized_port.sum(axis=1) # port_val which is a globle variable
    normalized_SPY=prices_SPY/prices_SPY.iloc[0]
 	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    # Compare daily portfolio value with SPY using a normalized plot  	
    	  	   		 	   			  		 			     			  	 
    if gen_plot:  		  	   		 	   			  		 			     			  	 
        # add code to plot here  		  	   		 	   			  		 			     			  	 
        df_temp = pd.concat(  		  	   		 	   			  		 			     			  	 
            [port_val, normalized_SPY], keys=["Portfolio", "SPY"], axis=1  	# price_SPY was changed to normalized_SPY	  	   		 	   			  		 			     			  	 
        )  	
        #plt.figure(figsize=(13, 6))
        df_temp.plot()
        plt.title('Normalized Daily Portfoilo Value  VS SPY')
        plt.xlabel('Date')
        plt.ylabel('Normalized Price')
        plt.savefig('images/Figure1.png')	
        #plt.show()  	   		 	   			  		 			     			  	 
        pass        

    




  		  	   		 	   			  		 			     			  	 
    return allocs, cr, adr, sddr, sr  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
def test_code():  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    This function WILL NOT be called by the auto grader.  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
  	#Start Date: 2008-06-01, End Date: 2009-06-01, Symbols: [‘IBM’, ‘X’, ‘GLD’, ‘JPM’].  	  	   		 	   			  		 			     			  	 
    start_date = dt.datetime(2008, 6, 1)  		  	   		 	   			  		 			     			  	 
    end_date = dt.datetime(2009, 6, 1)  		  	   		 	   			  		 			     			  	 
    symbols = ["IBM","X","GLD","JPM"]  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    # Assess the portfolio  		  	   		 	   			  		 			     			  	 
    allocations, cr, adr, sddr, sr = optimize_portfolio(  		  	   		 	   			  		 			     			  	 
        sd=start_date, ed=end_date, syms=symbols, gen_plot=True		  	   		 	   			  		 			     			  	 
    )  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    # Print statistics  		  	   		 	   			  		 			     			  	 
    print(f"Start Date: {start_date}")  		  	   		 	   			  		 			     			  	 
    print(f"End Date: {end_date}")  		  	   		 	   			  		 			     			  	 
    print(f"Symbols: {symbols}")  		  	   		 	   			  		 			     			  	 
    print(f"Allocations:{allocations}")  		  	   		 	   			  		 			     			  	 
    print(f"Sharpe Ratio: {sr}")  		  	   		 	   			  		 			     			  	 
    print(f"Volatility (stdev of daily returns): {sddr}")  		  	   		 	   			  		 			     			  	 
    print(f"Average Daily Return: {adr}")  		  	   		 	   			  		 			     			  	 
    print(f"Cumulative Return: {cr}")  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
if __name__ == "__main__":  		  	   		 	   			  		 			     			  	 
    # This code WILL NOT be called by the auto grader  		  	   		 	   			  		 			     			  	 
    # Do not assume that it will be called  		  	   		 	   			  		 			     			  	 
    test_code()  		  	   		 	   			  		 			     			  	 