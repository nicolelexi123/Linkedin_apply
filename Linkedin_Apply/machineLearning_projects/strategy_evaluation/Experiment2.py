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

def experiment2():
    # test1 impact=0.00
    
    learner_strategy1=sl.StrategyLearner(impact=0.00,commission=0)
    seed = 903941473 
    np.random.seed(seed)  		  	   		 	   			  		 			     			  	 
    random.seed(seed)
    learner_strategy1.add_evidence(symbol="JPM", 
                   sd=dt.datetime(2008, 1, 1), 
                   ed=dt.datetime(2009, 12, 31), 
                   sv=100000) 
  

    # test2 impact=0.005
    
    learner_strategy2=sl.StrategyLearner(impact=0.005,commission=0)
    seed = 903941473 
    np.random.seed(seed)  		  	   		 	   			  		 			     			  	 
    random.seed(seed)
    learner_strategy2.add_evidence(symbol="JPM", 
                   sd=dt.datetime(2008, 1, 1), 
                   ed=dt.datetime(2009, 12, 31), 
                   sv=100000)


    # test3 impact=0.2
    
    learner_strategy3=sl.StrategyLearner(impact=0.2,commission=0)
    seed = 903941473 
    np.random.seed(seed)  		  	   		 	   			  		 			     			  	 
    random.seed(seed)
    learner_strategy3.add_evidence(symbol="JPM", 
                   sd=dt.datetime(2008, 1, 1), 
                   ed=dt.datetime(2009, 12, 31), 
                   sv=100000)


    # test4 impact=-0.01
    
    learner_strategy4=sl.StrategyLearner(impact=-0.01,commission=0)
    seed = 903941473 
    np.random.seed(seed)  		  	   		 	   			  		 			     			  	 
    random.seed(seed)
    learner_strategy4.add_evidence(symbol="JPM", 
                   sd=dt.datetime(2008, 1, 1), 
                   ed=dt.datetime(2009, 12, 31), 
                   sv=100000)

    df_trades_strategy1_insample=learner_strategy1.testPolicy( symbol="JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31), sv=100000)
    df_trades_strategy2_insample=learner_strategy2.testPolicy( symbol="JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31), sv=100000)
    df_trades_strategy3_insample=learner_strategy3.testPolicy( symbol="JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31), sv=100000)
    df_trades_strategy4_insample=learner_strategy4.testPolicy( symbol="JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31), sv=100000)

    trade1 = np.count_nonzero(df_trades_strategy1_insample)
    trade2= np.count_nonzero(df_trades_strategy2_insample)
    trade3= np.count_nonzero(df_trades_strategy3_insample)
    trade4= np.count_nonzero(df_trades_strategy4_insample)
    #print(trade1)
    #print(trade2)
    #print(trade3)
    #print(trade4)
    
    trading_frequency=[trade1,trade2,trade3,trade4]
    labels=['test1-0','test2-0.005','test3-0.2','test4-(-0.01)']
    positions=range(len(trading_frequency))
    plt.bar(positions,trading_frequency,color='blue',alpha=0.7)
    plt.xticks(positions,labels)
    plt.title('Frequency Numbers')
    plt.ylabel('trading frequency')
    plt.savefig('images/figure6.png')
    #plt.show()
   

    sv=100000
    commission=0

    holding_strategy1=mk.compute_portvals(df_trades_strategy1_insample,sv,commission,0)
    holding_strategy2=mk.compute_portvals(df_trades_strategy1_insample,sv,commission,0.005)
    holding_strategy3=mk.compute_portvals(df_trades_strategy1_insample,sv,commission,0.2)
    holding_strategy4=mk.compute_portvals(df_trades_strategy1_insample,sv,commission,-0.01)


    str1_insample_result=mk.statistics(holding_strategy1)
    str2_insample_result=mk.statistics(holding_strategy2)
    str3_insample_result=mk.statistics(holding_strategy3)
    str4_insample_result=mk.statistics(holding_strategy4)

    print("test1",str1_insample_result)
    print("test2",str2_insample_result)
    print("test3",str3_insample_result)
    print("test4",str4_insample_result)
    
    '''
    holding_strategy1_norm=holding_strategy1/holding_strategy1.iloc[0]
    holding_strategy2_norm=holding_strategy1/holding_strategy2.iloc[0]
    holding_strategy3_norm=holding_strategy1/holding_strategy3.iloc[0]
    holding_strategy4_norm=holding_strategy1/holding_strategy4.iloc[0]
    '''

    plt.figure(figsize=(10,8))
    plt.plot(holding_strategy1,label='strategy1-impact 0.00',color='red')
    plt.plot(holding_strategy2,label='strategy2-impact 0.005',color='blue')
    plt.plot(holding_strategy3,label='strategy3-impact 0.02',color='green')
    plt.plot(holding_strategy4,label='strategy4-impact -0.01',color='purple')
    plt.title('Impact on portfoilo value-insample')
    plt.ylabel('value')
    plt.legend()
    plt.savefig('images/figure7.png')
    #plt.show()
    plt.gcf().clear()

    

if __name__ == "__main__":	
    experiment2()
