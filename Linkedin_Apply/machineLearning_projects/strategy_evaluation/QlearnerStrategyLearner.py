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
GT User ID: xi6 (replace with your User ID)  		  	   		 	   			  		 			     			  	 
GT ID: 903941473 (replace with your GT ID)  		  	   		 	   			  		 			     			  	 
"""  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 

  
import datetime as dt  
from datetime import timedelta		 		 	   			  		 			     			  	 
import random  		 
import indicators as ind 	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
import pandas as pd  	
import numpy as np  	  	   		 	   			  		 			     			  	 
import util as ut  		
import QLearner as qlt  	
import marketsimcode as mk   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
class StrategyLearner(object):  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    A strategy learner that can learn a trading policy using the same indicators used in ManualStrategy.  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    :param verbose: If “verbose” is True, your code can print out information for debugging.  		  	   		 	   			  		 			     			  	 
        If verbose = False your code should not generate ANY output.  		  	   		 	   			  		 			     			  	 
    :type verbose: bool  		  	   		 	   			  		 			     			  	 
    :param impact: The market impact of each transaction, defaults to 0.0  		  	   		 	   			  		 			     			  	 
    :type impact: float  		  	   		 	   			  		 			     			  	 
    :param commission: The commission amount charged, defaults to 0.0  		  	   		 	   			  		 			     			  	 
    :type commission: float  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    # constructor  		 
    def author(self):
        return "xi6"

    def __init__(self, verbose=False, impact=0.0, commission=0.0,step=3):  		  	   		 	   			  		 			     			  	 
        """  		  	   		 	   			  		 			     			  	 
        Constructor method  		  	   		 	   			  		 			     			  	 S
        """  		  	   		 	   			  		 			     			  	 
        self.verbose = verbose  		  	   		 	   			  		 			     			  	 
        self.impact = impact  		  	   		 	   			  		 			     			  	 
        self.commission = commission 
        self.step =step 	
        self.Slearner=qlt.QLearner(num_states=334,  num_actions=3,  alpha=0.2, gamma=0.9,  rar=0.5, radr=0.99,  dyna=0,  verbose=False)   
        
       		  	   		 	   			  		 			     			  	  		  	   		 	   			  		 			     			  	 
         	
    '''
    def discreting(self,data,step=3):
        stepize=len(data)//step
        sorted_data=np.sort(data)
        thresholds=[]
        for i in range(0,step-1):
            index=(i+1)*stepize-1
            thresholds.append(sorted_data[index])
            
        return np.array(thresholds)
    
    def map_scores_state(self, data, step):
        scores = pd.DataFrame(0, index=data.index, columns=data.columns, dtype=int)
        for col in data.columns:
            thr = self.discreting(data[col].values, step)
            # 使用pd.cut进行离散化，然后将codes属性赋值给对应的scores列
            scores[col] = pd.cut(data[col].values, bins=np.insert(thr, [0, len(thr)], [data[col].min()-1, data[col].max()]), labels=False, right=True)+1
        state = scores.iloc[:, 0] * 10 + scores.iloc[:, 1] * 1 + scores.iloc[:, 2] * 100
        #state2=state.copy('state')
        #state2.reset_index(drop=True)
        return state
     
  
    '''
    def discreting(self, data, step=4):
        # 基于max-min生成等间距的阈值
        min_val = np.min(data)
        max_val = np.max(data)
        # 使用linspace而非arange以确保包含最大值
        bins = np.linspace(min_val, max_val, step+1)
        return bins
    
    def map_scores_state(self, data, step):
        scores = pd.DataFrame(index=data.index, columns=data.columns, dtype=int)
        for col in data.columns:
            bins = self.discreting(data[col], step)
            # 使用pd.cut进行离散化，并通过在结果上加1使序号从1开始
            scores[col] = pd.cut(data[col], bins=bins, labels=False, right=True, include_lowest=True) + 1
            state = scores.iloc[:, 0]  + scores.iloc[:, 1]  + scores.iloc[:, 2] 
        
        return state
    
  

        
            
  		  	   		 	   			  		 			     			  	 
    # this method should create a QLearner, and train it for trading  		  	   		 	   			  		 			     			  	 
    def add_evidence(  		  	   		 	   			  		 			     			  	 
        self,  		  	   		 	   			  		 			     			  	 
        symbol="JPM",  		  	   		 	   			  		 			     			  	 
        sd=dt.datetime(2008, 1, 1),  		  	   		 	   			  		 			     			  	 
        ed=dt.datetime(2009, 1, 1),  		  	   		 	   			  		 			     			  	 
        sv=100000,  		  	   		 	   			  		 			     			  	 
    ):  		  	   		 	   			  		 			     			  	 
        """  		  	   		 	   			  		 			     			  	 
        Trains your strategy learner over a given time frame.  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
        :param symbol: The stock symbol to train on  		  	   		 	   			  		 			     			  	 
        :type symbol: str  		  	   		 	   			  		 			     			  	 
        :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		 	   			  		 			     			  	 
        :type sd: datetime  		  	   		 	   			  		 			     			  	 
        :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		 	   			  		 			     			  	 
        :type ed: datetime  		  	   		 	   			  		 			     			  	 
        :param sv: The starting value of the portfolio  		  	   		 	   			  		 			     			  	 
        :type sv: int  		  	   		 	   			  		 			     			  	 
        """  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
        # add your code to do learning here  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
        # example usage of the old backward compatible util function  		  	   		 	   			  		 			     			  	  		  	   		 	   			  		 			     			  	 
        dates = pd.date_range(sd, ed)   		  	   		 	   			  		 			     			  	 	
        sd_new = sd - timedelta(days=40)	  	   		 	  	   		 	   			  		 			     			  	 
        dates_new = pd.date_range(sd_new, ed)  	
        #dates=pd.date_range(sd,ed)
        price_stocks_df=ut.get_data([symbol], dates)  
        price_stocks_df.drop(columns=["SPY"], inplace=True) 	   		 	   			  		 			     			  	 
        price_stocks_new_df = ut.get_data([symbol], dates_new)  		  	   		 	   			  		 			     			  	 
        price_stocks_new_df.drop(columns=["SPY"], inplace=True)
        print(price_stocks_new_df)
        
        indicator_df=pd.DataFrame(index=price_stocks_new_df.index)
        indicator_df['ind1_sma_price']=ind.calculate_sma_price(price_stocks_new_df,symbol,period=20)
    
        indicator_df['ind2_PPI']=ind.calculate_PPI(price_stocks_new_df,symbol,12,26,9)
        indicator_df['ind3_BB']=ind.calculate_BB(price_stocks_new_df,symbol,period=20)
        indicator_df=indicator_df[sd:ed]	
        print(indicator_df)

        # calculater daily returns as reward
        daily_return=(price_stocks_new_df/price_stocks_new_df.shift(1))-1
        daily_return=daily_return[sd:ed]
        print(daily_return)
       
       # train Qlearner   
        #state_sd=self.map_scores_state(indicator_df[sd],self.step)
        states = [0 for i in range(334)]
        rewards=daily_return[symbol].values
        epochs=500
        for epoch in range(epochs):
            #state=states[0]
            states=self.map_scores_state(indicator_df, self.step) #discretize/convert indicator to state
            #print(states)
            for i in range(len(states)-1): # reward starts from the second day 
            #for i in range(dates.size-2):
                #print("HALOU", i)
                state = states[i]
                action=self.Slearner.querysetstate(state)
                if action==0:
                    reward=rewards[i]
        
                elif action==1:
                    reward=rewards[i]*(1-self.impact)    #long
            #         reward=rewards[i]
                elif action==2:
                    reward=-rewards[i]*(1+self.impact)   #short
            #         reward=-rewards[i]
                #reward=signal*daily_return[i]*(1-self.impact)-self.commission if signal!=0 else daily_return[i]
                next_state = states[i+1] if i < (len(states) - 2) else states[i]

                #position change?
                #next_state=self.map_scores_state(indicator_df, sd, i, self.step)
                self.Slearner.query(next_state,reward)
                state=next_state
    
                                                                                

  		  	   		 	   			  		 			     			  	 
         	 
    # this method should use the existing policy and test it against new data  		  	   		 	   			  		 			     			  	 
    def testPolicy(  		  	   		 	   			  		 			     			  	 
        self,  		  	   		 	   			  		 			     			  	 
        symbol="JPM",  		  	   		 	   			  		 			     			  	 
        sd=dt.datetime(2009, 1, 1),  		  	   		 	   			  		 			     			  	 
        ed=dt.datetime(2010, 1, 1),  		  	   		 	   			  		 			     			  	 
        sv=100000,  		  	   		 	   			  		 			     			  	 
    ):  		  	   		 	   			  		 			     			  	 

        days=40 	   		 	   			  		 			     			  	 
        sd_new = sd - dt.timedelta(days)   
        dates=	pd.date_range(sd, ed) 	 	  	   		 	   			  		 			     			  	 
        dates_new = pd.date_range(sd_new, ed)  	
        #dates=pd.date_range(sd,ed)
        price_stocks_df=ut.get_data([symbol], dates)   	   		 	   			  		 			     			  	 
        price_stocks_new_df = ut.get_data([symbol], dates_new)  		  	   		 	   			  		 			     			  	 
        price_stocks_new_df.drop(columns=["SPY"], inplace=True)
        #print(price_stocks_new_df)
        
        indicator_df=pd.DataFrame(index=price_stocks_new_df.index)
        indicator_df['ind1_sma_price']=ind.calculate_sma_price(price_stocks_new_df,symbol,period=20)
    
        indicator_df['ind2_PPI']=ind.calculate_PPI(price_stocks_new_df,symbol,12, 26, 9)
        indicator_df['ind3_BB']=ind.calculate_BB(price_stocks_new_df,symbol,period=20)
        indicator_df=indicator_df[sd:ed]	
        #print(indicator_df.shape)
        testing_states=self.map_scores_state(indicator_df,self.step)
        signals = pd.DataFrame(index=indicator_df.index, columns=[symbol], data=0) 
        df_trades=pd.DataFrame(index=indicator_df.index, columns=[symbol], data=0) 
        current_position=0
        
        
        
        for i in range(len(testing_states)-1):
            state=testing_states[i]
            action=self.Slearner.querysetstate(state)
            if action==1:
                signals.iloc[i]=1
                if current_position==0:
                    df_trades.iloc[i]=signals.iloc[i]*1000
                    current_position+=1000
                elif current_position==-1000:
                    df_trades.iloc[i]=signals.iloc[i]*2000
                    current_position+=2000
            elif action==2:
                signals.iloc[i]=-1
                if current_position==0:
                    df_trades.iloc[i]=signals.iloc[i]*1000
                    current_position-=1000
                elif current_position==1000:
                    df_trades.iloc[i]=signals.iloc[i]*2000
                    current_position-=2000
        #    else:
        #        signals.iloc[i]=0
        #        df_trades.iloc[i]=0
        
        return df_trades
      	  	   		 	   			  		 			     			  	 
                                                                                                                                     		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
if __name__ == "__main__":  	
    
    m= StrategyLearner()

    m.add_evidence(symbol="JPM", 
                   sd=dt.datetime(2008, 1, 1), 
                   ed=dt.datetime(2009, 12, 30), 
                   sv=100000)

    
    print("Q table")
    for i in range(3):
        for j in range(3):
            for k in range(3):
                print(i*10+j*1+k*100, m.Slearner.Q[i*10+j*1+k*100])
    
    df_trades=m.testPolicy( symbol="JPM",  		  	   		 	   			  		 			     			  	 
        sd=dt.datetime(2008, 1, 1),  		  	   		 	   			  		 			     			  	 
        ed=dt.datetime(2009, 12, 30),  		  	   		 	   			  		 			     			  	 
        sv=100000,  		)
    

    
    print(df_trades)
    

    

    

    
    start_val=100000
    commission=9.95
    impact=0.005
    
    holdings_testing_df=mk.compute_portvals(df_trades,  start_val,  commission,  impact)
    print(holdings_testing_df)
    stcs=mk.statistics(holdings_testing_df)
    print(stcs)
    
  