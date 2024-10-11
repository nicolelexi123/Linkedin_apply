import datetime as dt  
from datetime import timedelta		 		 	   			  		 			     			  	 
import random  		 
import indicators as ind 	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
import pandas as pd  	
import numpy as np  	  	   		 	   			  		 			     			  	 
import util as ut  			
import marketsimcode as mk  	
import matplotlib.pyplot as plt	
import ManualStrategy as ms	
import StrategyLearner as sl

def author(self):
    return 'xi6'


def experiment1():
    learner_manual=ms.ManualStrategy()
    learner_strategy=sl.StrategyLearner(commission=9.95)
    # train learner 
    seed = 903941473 
    np.random.seed(seed)  		  	   		 	   			  		 			     			  	 
    random.seed(seed)
    learner_strategy.add_evidence(symbol="JPM", 
                   sd=dt.datetime(2008, 1, 1), 
                   ed=dt.datetime(2009, 12, 31), 
                   sv=100000)

    # in sample result 2008,1,1-2009,12,31
    symbol="JPM"		  	   		 	   			  		 			     			  	 
    sv=100000
    start_val=sv
    commission=9.95
    impact=0.005
   


    df_trades_strategy_insample=learner_strategy.testPolicy( symbol="JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31), sv=100000)

    df_trades_manual_insample=learner_manual.testPolicy(symbol="JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31) )
    
    df_benchmark_insample= pd.DataFrame(index=df_trades_manual_insample.index, data=0.0, columns=[symbol])
    df_benchmark_insample[symbol][0]=1000
    df_benchmark_insample[symbol][-1]=-1000

    

    holding_strategy_insample=mk.compute_portvals(df_trades_strategy_insample,sv,commission,impact)
    holding_manual_insample=mk.compute_portvals(df_trades_manual_insample, sv,commission,impact)
    holding_benchmark_insample=mk.compute_portvals(df_benchmark_insample, sv,commission,impact)
    
    holding_strategy_insample_normalized=holding_strategy_insample/holding_strategy_insample.iloc[0]
    holding_manual_insample_normalized=holding_manual_insample/holding_manual_insample.iloc[0]
    holding_benchmark_insample_normalized=holding_benchmark_insample/holding_benchmark_insample.iloc[0]

    
    # in sample chart
    plt.figure(figsize=(10,8))
    plt.plot(holding_strategy_insample_normalized,label='strategy',color='green')
    plt.plot(holding_manual_insample_normalized,label='manual',color='blue')
    plt.plot(holding_benchmark_insample_normalized,label='benchmark',linestyle='--', color='red')
    plt.title("In Sample Normlized Portfolio Value")
    plt.xlabel("In Sample Date")
    plt.ylabel("Normlized Value")

    plt.legend()
    #plt.show()
    plt.savefig('images/figure4.png', format='png')

   # out sample 

    df_trades_strategy_outsample=learner_strategy.testPolicy( symbol="JPM", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011, 12, 31), sv=100000)

    df_trades_manual_outsample=learner_manual.testPolicy(symbol="JPM", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011, 12, 31) )
    
    df_benchmark_outsample= pd.DataFrame(index=df_trades_manual_outsample.index, data=0.0, columns=[symbol])
    df_benchmark_outsample[symbol][0]=1000
    df_benchmark_outsample[symbol][-1]=-1000

    holding_strategy_outsample=mk.compute_portvals(df_trades_strategy_outsample,sv,commission,impact)
    holding_manual_outsample=mk.compute_portvals(df_trades_manual_outsample, sv,commission,impact)
    holding_benchmark_outsample=mk.compute_portvals(df_benchmark_outsample, sv,commission,impact)
    
    holding_strategy_outsample_normalized=holding_strategy_outsample/holding_strategy_outsample.iloc[0]
    holding_manual_outsample_normalized=holding_manual_outsample/holding_manual_outsample.iloc[0]
    holding_benchmark_outsample_normalized=holding_benchmark_outsample/holding_benchmark_outsample.iloc[0]
    
    # out sample chart

    plt.figure(figsize=(10,8))
    plt.plot(holding_strategy_outsample_normalized,label='strategy',color='red')
    plt.plot(holding_manual_outsample_normalized,label='manual',color='green')
    plt.plot(holding_benchmark_outsample_normalized,label='benchmark',linestyle='--', color='orange')
    plt.title("Out Sample Normlized Portfolio Value")
    plt.xlabel("Out Sample Date")
    plt.ylabel("Normlized Value")

    plt.legend()
    #plt.show()
    plt.savefig('images/figure5.png', format='png')

    
if __name__ == "__main__":	
    experiment1()

