""""""  		  	   		 	   			  		 			     			  	 
"""  		  	   		 	   			  		 			     			  	 
Template for implementing StrategyLearner  (c) 2016 Tucker Balch  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
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
import random  	
from datetime import timedelta		
import matplotlib.pyplot as plt		   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
import pandas as pd  		  	   		 	   			  		 			     			  	 
import util as ut  	

import indicators as ind   #import calculate_sma_price	
import marketsimcode as mk
import numpy as np



	

  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
class ManualStrategy(object):  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    A strategy learner that can learn a trading policy using the same indicators used in P6.  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    :param verbose: If “verbose” is True, your code can print out information for debugging.  		  	   		 	   			  		 			     			  	 
        If verbose = False your code should not generate ANY output.  		  	   		 	   			  		 			     			  	 
    :type verbose: bool  		  	   		 	   			  		 			     			  	 
    :param impact: The market impact of each transaction, defaults to 0.0  		  	   		 	   			  		 			     			  	 
    :type impact: float  		  	   		 	   			  		 			     			  	 
    :param commission: The commission amount charged, defaults to 0.0  		  	   		 	   			  		 			     			  	 
    :type commission: float  		  	   		 	   			  		 			     			  	 
    """  
    def author(self):
        return "xi6"

    # constructor  		  	   		 	   			  		 			     			  	 
    def __init__(self, verbose=False, impact=0.0, commission=0.0):	  	   		 	   			  		 			     			  	 
        """  		  	   		 	   			  		 			     			  	 
        Constructor method  		  	   		 	   			  		 			     			  	 
        """  		  	   		 	   			  		 			     			  	 
        self.verbose = verbose  		  	   		 	   			  		 			     			  	 
        self.impact = impact  		  	   		 	   			  		 			     			  	 
        self.commission = commission 


        #self.file = open("output_indic2.txt", "w")	   	

    def add_evidence(self, symbol="JPM", sd=dt.datetime(2008, 1, 1, 0, 0), ed=dt.datetime(2009, 1, 1, 0, 0), sv=100000):
        pass

    def testPolicy(self, symbol="JPM", sd=dt.datetime(2009, 1, 1, 0, 0), ed=dt.datetime(2010, 1, 1, 0, 0), sv=100000):

        days_forward = 40
        dates = pd.date_range(sd, ed,days_forward)   		  	   		 	   			  		 			     			  	 	
        sd_new = sd - timedelta(days_forward)	  	   		 	  	   		 	   			  		 			     			  	 
        dates_new = pd.date_range(sd_new, ed)  	
        #dates=pd.date_range(sd,ed)
        price_stocks_df=ut.get_data([symbol], dates)  
        price_stocks_df.drop(columns=["SPY"], inplace=True) 	   		 	   			  		 			     			  	 
        price_stocks_new_df = ut.get_data([symbol], dates_new)  		  	   		 	   			  		 			     			  	 
        price_stocks_new_df.drop(columns=["SPY"], inplace=True)
        indicator_df=pd.DataFrame(index=price_stocks_new_df.index)
        indicator_df['ind1_sma_price']=ind.calculate_sma_price(price_stocks_new_df,symbol,period=20)

    
        indicator_df['ind2_PPI']=ind.calculate_PPI(price_stocks_new_df,symbol,12,26,9)
        indicator_df['ind3_BB']=ind.calculate_BB(price_stocks_new_df,symbol,period=20)
        indicator_df['ind4_Mom']=ind.calculate_Momentum(price_stocks_new_df,symbol,period=14)
        indicator_df['closingprice']=price_stocks_new_df
        indicator_df['price-change']=price_stocks_new_df.shift(-1)-price_stocks_new_df
        indicator_df=indicator_df[sd:ed]
        
        '''
        print(indicator_df)
        aa = indicator_df[indicator_df['price-change']>0]
        print(indicator_df[indicator_df['price-change']>0])
        print(indicator_df[indicator_df['price-change']<0])
        bb=indicator_df[indicator_df['price-change']<0]
       # self.file.write(f"long \n")
        
       # self.file.write(aa.to_string(index=True))

       # self.file.write(f"short \n")
        
       # self.file.write(bb.to_string(index=True))
        '''

        
       
       
        # using 3 indicator to decide buy and sell or do nothing . 
        condition1 = indicator_df['ind1_sma_price'] > 1.15
        condition2 = indicator_df['ind2_PPI'] > 0
        condition3 = indicator_df['ind3_BB'] <15.0
        
        condition4= indicator_df['ind1_sma_price'] <0.8
        condition5= indicator_df['ind2_PPI'] < 0.0
        condition6 = indicator_df['ind3_BB'] >68


        #condition_combine1=((condition1 & condition2) | (condition1 & condition3) | (condition2 & condition3))
        #condition_combine2=((condition4 & condition5) | (condition4 & condition6) | (condition5 & condition6))
       
        
        indicator_df['factor']=0
        indicator_df['shares']=0
      
        indicator_df.loc[condition3|condition1,'factor']=1
        indicator_df.loc[condition6|condition5,'factor']=-1   
       
        indicator_df.loc
        

        #print(indicator_df)

        current_position=0
       

        for index,row in indicator_df.iterrows():
            factor=row['factor']
            shares = 0
            if current_position==0:
                if factor==1:
                    shares=1000
                  
                elif factor==-1:
                    shares=-1000
                  
            elif current_position==1000:
                if factor==-1:
                    shares=-2000
                    
            else:
                if factor==1:
                    shares=2000
                    
            indicator_df.at[index, 'shares'] = shares
            current_position+=shares
        
        trade_df=indicator_df[['shares']].copy()
        trade_df.rename(columns={'shares': symbol}, inplace=True)
        #trade_df=trade_df.shift(1).fillna(0)
        return trade_df
            			  			  	   		 	   			  		 			     			  	 
    '''
    def stati_result( self, df_trade ,symbol, sv=100000):  
     
        port_val_strategy_manual=mk.compute_portvals(trade,sv,commission=9.5,impact=0.005)
        print(port_val_strategy_manual)
        stat_strategy1=mk.statistics(port_val_strategy_manual)

        
        benchmark= pd.DataFrame(index=trade.index, data=0.0, columns=[symbol])
        benchmark[symbol][0]=1000
        benchmark[symbol][-1]=-1000
        port_val_benchmark=mk.compute_portvals(benchmark,sv,commission=9.5,impact=0.005)
        print(port_val_benchmark)
        stat_benchmark=mk.statistics(port_val_benchmark)
    
        return stat_strategy1, stat_benchmark
    '''

    def record_entry(self, trade_df, symbol):
        long_entries = []
        short_entries = []

        #previous_shares = 0
        for index, row in trade_df.iterrows():
            current_shares = row[symbol]
            # Check for long entry conditions
            if current_shares > 0: #(previous_shares == 0 or previous_shares == -1000) and current_shares == 1000:
                long_entries.append(index)
            # Check for short entry conditions
            elif current_shares < 0: #(previous_shares == 0 or previous_shares == 1000) and current_shares == -1000:
                short_entries.append(index)
            #previous_shares = current_shares
        
        return long_entries, short_entries



  

  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
if __name__ == "__main__":  
   
    # in sample 
    ms_learner=ManualStrategy()
    ms_trade_insample=ms_learner.testPolicy(symbol="JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31))	
   
    symbol="JPM"
    sv=100000
    commission=9.95
    impact=0.005
    
    long_entries_insample, short_entries_insample = ms_learner.record_entry(ms_trade_insample, symbol)
    #print(long_entries_insample)
    #print(short_entries_insample)
   
   
    df_benchmark_insample= pd.DataFrame(index=ms_trade_insample.index, data=0.0, columns=[symbol])
    df_benchmark_insample[symbol][0]=1000
    df_benchmark_insample[symbol][-1]=-1000

    
    holding_manual_insample=mk.compute_portvals(ms_trade_insample, sv,commission,impact)
    holding_benchmark_insample=mk.compute_portvals(df_benchmark_insample, sv,commission,impact)

    ms_insample_result=mk.statistics(holding_manual_insample)
    benchmark_insample_result=mk.statistics(holding_benchmark_insample)

    holding_manual_insample /= holding_manual_insample.iloc[0]
    holding_benchmark_insample /= holding_benchmark_insample.iloc[0]

    
    #print(ms_trade_insample)
    

    print("manual-insample",ms_insample_result)  # Manual Strategy result in sample
    print("benchmark-insample",benchmark_insample_result)

    #ploting for insample period
    plt.figure(figsize=(14, 7))
    plt.plot(holding_manual_insample.index, holding_manual_insample, 'r', label='Manual Strategy')
    plt.plot(holding_benchmark_insample.index, holding_benchmark_insample, 'purple', label='Benchmark')
    
    for date in long_entries_insample:
        plt.axvline(x=date, color='blue', linestyle='--', alpha=0.7)
    for date in short_entries_insample:
        plt.axvline(x=date, color='red', linestyle='--', alpha=0.7)

    plt.title('In-Sample Period: Manual Strategy vs. Benchmark')
    plt.xlabel('Date')
    plt.ylabel('Normalized Portfolio Value')
    plt.legend()
   # plt.show()
    plt.savefig('images/figure1.png', format='png')



    
    # out sample 
    ms_learner=ManualStrategy()
    ms_trade_out=ms_learner.testPolicy(symbol="JPM", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011, 12, 31))	
   
    long_entries_outsample, short_entries_outsample = ms_learner.record_entry(ms_trade_out, "JPM")
 
    df_benchmark_outsample= pd.DataFrame(index=ms_trade_out.index, data=0.0, columns=[symbol])
    df_benchmark_outsample[symbol][0]=1000
    df_benchmark_outsample[symbol][-1]=-1000

    
    holding_manual_outsample=mk.compute_portvals(ms_trade_out, sv,commission,impact)
    holding_benchmark_outsample=mk.compute_portvals(df_benchmark_outsample, sv,commission,impact)
    
    ms_outsample_result=mk.statistics(holding_manual_outsample)
    benchmark_outsample_result=mk.statistics(holding_benchmark_outsample)

    holding_manual_outsample /= holding_manual_outsample.iloc[0]
    holding_benchmark_outsample /= holding_benchmark_outsample.iloc[0]

    print("manual-outsample",ms_outsample_result)
    print("benchmark-outsample",benchmark_outsample_result)

    plt.figure(figsize=(14, 7))
    plt.plot(holding_manual_outsample.index, holding_manual_outsample, 'r', label='Manual Strategy')
    plt.plot(holding_benchmark_outsample.index, holding_benchmark_outsample, 'purple', label='Benchmark')
    
    for date in long_entries_outsample:
        plt.axvline(x=date, color='blue', linestyle='--', alpha=0.7)
    for date in short_entries_outsample:
        plt.axvline(x=date, color='black', linestyle='--', alpha=0.7)

    plt.title('Out-Sample Period: Manual Strategy vs. Benchmark')
    plt.xlabel('Date')
    plt.ylabel('Normalized Portfolio Value')
    plt.legend()
   # plt.show()
    plt.savefig('images/figure2.png', format='png')



    


   
   
     	   		 	   			  		 			     			  	 
    	  	   		 	   			  		 			     			  	 
