""""""  		  	   		 	   			  		 			     			  	 
"""  		  	   		 	   			  		 			     			  	 	  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
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
  		  	   		 	   			  		 			     			  	 
Student Name: Tucker Balch (replace with your name)  		  	   		 	   			  		 			     			  	 
GT User ID: tb34 (replace with your User ID)  		  	   		 	   			  		 			     			  	 
GT ID: 900897987 (replace with your GT ID)  		  	   		 	   			  		 			     			  	 
"""  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
import math  		  	   		 	   			  		 			     			  	 
import random		  	   		 	   			  		 			     			  	 
import time  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
import datetime as dt  	
from datetime import timedelta		
import matplotlib.pyplot as plt		   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
import pandas as pd  		  	   		 	   			  		 			     			  	 
import util as ut  	

import indicators as ind   #import calculate_sma_price	
import marketsimcode as mk
import numpy as np	  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
from ManualStrategy import ManualStrategy	  	   		 	   			  		 			     			  	 
from StrategyLearner import StrategyLearner
import experiment1
import experiment2


def author(self):  		  	   		 	   			  		 			     			  	 
                                                                                
    return "xi6"  	

def test_experiment1(verbose=False):
    experiment1.experiment1()

def test_experiment2(verbose=False):
    experiment2.experiment2()

def test_strategy(verbose=False):


    
    
    learner= StrategyLearner(commission=9.95)
    start_val=100000
    commission=9.95
    impact=0.005
    
    seed = 903941473 
    np.random.seed(seed)  		  	   		 	   			  		 			     			  	 
    random.seed(seed)



            
    learner.add_evidence(symbol="JPM", 
                   sd=dt.datetime(2008, 1, 1), 
                   ed=dt.datetime(2009, 12, 31), 
                   sv=100000)

  
    df_trades_insample=learner.testPolicy( symbol="JPM",  		  	   		 	   			  		 			     			  	 
        sd=dt.datetime(2008, 1, 1),  		  	   		 	   			  		 			     			  	 
        ed=dt.datetime(2009, 12, 31),  		  	   		 	   			  		 			     			  	 
        sv=100000,  		)

    df_trades_outsample=learner.testPolicy(symbol="JPM",  		  	   		 	   			  		 			     			  	 
        sd=dt.datetime(2010, 1, 1),  		  	   		 	   			  		 			     			  	 
        ed=dt.datetime(2011, 12, 31),  		  	   		 	   			  		 			     			  	 
        sv=100000,  )

    
    holdings_insample_df=mk.compute_portvals(df_trades_insample,  start_val, commission, impact)
    holdings_outsample_df=mk.compute_portvals(df_trades_outsample,start_val,commission,impact)
    
    stcs_insample=mk.statistics(holdings_insample_df)
    stcs_outsample=mk.statistics(holdings_outsample_df)
    print("SL-insample",stcs_insample)  
    print("SL-outsample",stcs_outsample)	                                                                                 	  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
def test_manual(verbose=False):  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    function to test manual strategy code  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
		  	   		 	   			  		 			     			  	 
    """  
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
    

    print("ms_insample_result",ms_insample_result)  # Manual Strategy result in sample
    print("benchmark_insample_result",benchmark_insample_result)

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
    #plt.show()
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

    print("ms_out_result",ms_outsample_result)
    print("benchmark_out_result",benchmark_outsample_result)

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
    #plt.show()
    plt.savefig('images/figure2.png', format='png')


   		 	   			  		 			     			  			  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
# run the code to test a learner  		  	   		 	   			  		 			     			  	 
def test_code():  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    verbose = False  # print lots of debug stuff if True  		
      	   		 	   			  		 			     			  	  		  	   		 	   			  		 			     			  	 		  	   		 	   			  		 			     					  	   		 	   			  		 			     				  	   		 	   			  		 			     			  	 
    seed = int(903941473)
    random.seed(seed)  
    np.random.seed(seed) 		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    ######## run manual test ######## 
    test_experiment2(verbose)
    test_experiment1(verbose)
    
    test_manual(verbose)
    test_strategy(verbose)		  	   		 	   			  		 			     			  	 
	  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
if __name__ == "__main__":  		  	   		 	   			  		 			     			  	 
    test_code() 

