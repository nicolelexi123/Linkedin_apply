import datetime as dt  
from datetime import timedelta		 		 	   			  		 			     			  	 
import random  		 
import indicators as ind 	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
import pandas as pd  	
import numpy as np  	  	   		 	   			  		 			     			  	 
import util as ut  		
	
import RTLearner as rl
import BagLearner as bl
import marketsimcode as mk  

class StrategyLearner(object):
    def __init__(self, verbose=False, impact=0.0, commission=0.0):
        """
        Constructor method
        """
        self.leaf_size = 5
        self.impact = impact
        self.verbose = verbose
        self.commission=commission
        
        self.bag_number=2

        self.learner=bl.BagLearner(learner=rl.RTLearner,kwargs={"leaf_size":5, "verbose":False},bags=2,boost=False,verbose=False)
        #self.learner=rl.RTLearner(leaf_size=6)

    def author(self):  		  	   		 	   			  		 			     			  	 
        """  		  	   		 	   			  		 			     			  	 
        :return: The GT username of the student  		  	   		 	   			  		 			     			  	 
        :rtype: str  		  	   		 	   			  		 			     			  	 
        """  		  	   		 	   			  		 			     			  	 
        return "xi6"  # replace tb34 with your Georgia Tech username  		 

    
    def discreting(self,data,step=10):
        stepize=len(data)//step
        sorted_data=np.sort(data)
        thresholds=[]
        for i in range(0,step-1):
            index=(i+1)*stepize-1
            thresholds.append(sorted_data[index])
            
        return np.array(thresholds)
    '''
    def map_scores_state(self, data, step):
        scores = pd.DataFrame(0, index=data.index, columns=data.columns, dtype=int)
        
        for col in data.columns:
            thr = self.discreting(data[col].values, step)
            # 使用pd.cut进行离散化，然后将codes属性赋值给对应的scores列
            scores[col] = pd.cut(data[col].values, bins=np.insert(thr, [0, len(thr)], [data[col].min()-1, data[col].max()]), labels=False, right=True)+1
        #state = scores.iloc[:, 0] * 10 + scores.iloc[:, 1] * 1 + scores.iloc[:, 2] * 100
    
        return scores	   		 	   			  		 			     			  	 
    '''

    def map_scores_state(self, data, steps):
     
        scores = pd.DataFrame(0, index=data.index, columns=data.columns, dtype=int)
        for col in data.columns:
            step = steps.get(col, 10)  # 如果列名在steps字典中没有对应的step值，则默认使用10
            thr = self.discreting(data[col].values, step)
            # 使用pd.cut进行离散化，然后将codes属性赋值给对应的scores列
            scores[col] = pd.cut(data[col].values, bins=np.insert(thr, [0, len(thr)], [data[col].min()-1, data[col].max()]), labels=False, right=True) + 1
        return scores

    def add_evidence(self,
        symbol="JPM",
        sd=dt.datetime(2008, 1, 1, 0, 0),
        ed=dt.datetime(2009, 1, 1, 0, 0),
        sv=100000):

        
       
        dates = pd.date_range(sd, ed)   		  	   		 	   			  		 			     			  	 	
        sd_new = sd - timedelta(days=40)	  	   		 	  	   		 	   			  		 			     			  	 
        dates_new = pd.date_range(sd_new, ed)  	
        #dates=pd.date_range(sd,ed)
        price_stocks_df=ut.get_data([symbol], dates)  
        price_stocks_df.drop(columns=["SPY"], inplace=True) 	   		 	   			  		 			     			  	 
        price_stocks_new_df = ut.get_data([symbol], dates_new)  		  	   		 	   			  		 			     			  	 
        price_stocks_new_df.drop(columns=["SPY"], inplace=True)
        #print(price_stocks_new_df)
        
        indicator_df=pd.DataFrame(index=price_stocks_new_df.index)
        indicator_df['ind1_sma_price']=ind.calculate_sma_price(price_stocks_new_df,symbol,period=20)
    
        indicator_df['ind2_PPI']=ind.calculate_PPI(price_stocks_new_df,symbol,12,26,9)
        indicator_df['ind3_BB']=ind.calculate_BB(price_stocks_new_df,symbol,period=20)
        indicator_df=indicator_df[sd:ed]	
        #print(indicator_df)
        #steps={'ind1_sma_price':50,'ind2_PPI':80,'ind3_BB':50}
        steps={'ind1_sma_price':40,'ind2_PPI':80,'ind3_BB':40}
        indicator_score_df=self.map_scores_state(indicator_df,steps)

        #print(indicator_score_df)

        # calculater daily returns as reward
        daily_return=(price_stocks_new_df.shift(-14)/price_stocks_new_df)-1
        daily_return=daily_return[sd:ed]
        daily_return = daily_return.fillna(0)
        #print(daily_return)

        # Align indicator array and return array

        #indicators_with_return = indicator_df.copy()
        #indicators_with_return['Returns'] = daily_return
        X_train = indicator_score_df.values

        buy_threshold = 0.01+self.impact  # 例如，日收益率大于1%视为买入信号
        sell_threshold = -0.01+self.impact  # 例如，日收益率小于-1%视为卖出信号


        conditions = [(daily_return > buy_threshold),  (daily_return < sell_threshold)]
        choices = [1, -1]

        Y_train = np.select(conditions, choices, default=0).astype(int)

         # train RTlearner 
       
       
        #seed = int(903941473)
        #random.seed(seed)  
        #np.random.seed(seed) 

        self.learner = bl.BagLearner(learner=rl.RTLearner,kwargs={"leaf_size":5, "verbose":False},bags=2,boost=False,verbose=False) 
        self.learner.add_evidence(X_train, Y_train) 		


        
       
        
        


       
    def testPolicy(  		  	   		 	   			  		 			     			  	 
        self,  		  	   		 	   			  		 			     			  	 
        symbol="JPM",  		  	   		 	   			  		 			     			  	 
        sd=dt.datetime(2009, 1, 1, 0, 0),  		  	   		 	   			  		 			     			  	 
        ed=dt.datetime(2010, 1, 1, 0, 0),  		  	   		 	   			  		 			     			  	 
        sv=100000  		  	   		 	   			  		 			     			  	 
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
        #indicator_score_df=self.map_scores_state(indicator_df,step=10)
        #indicator_score_df=indicator_df.round(2)
        #steps={'ind1_sma_price':50,'ind2_PPI':80,'ind3_BB':50}
        steps={'ind1_sma_price':40,'ind2_PPI':80,'ind3_BB':40}
        indicator_score_df=self.map_scores_state(indicator_df,steps)
     
        predicted_actions = self.learner.query(indicator_score_df.values)
    
  
        df_trades = pd.DataFrame(index=indicator_score_df.index, columns=[symbol], data=0)
        current_position = 0
    
        for i in range(len(predicted_actions)):
            action = predicted_actions[i] 
            if action == 1:
                if current_position == 0:
                    df_trades.iloc[i] = 1000
                    current_position += 1000
                elif current_position == -1000:
                    df_trades.iloc[i] = 2000
                    current_position += 2000
            elif action == -1:
                if current_position == 0:
                    df_trades.iloc[i] = -1000
                    current_position -= 1000
                elif current_position == 1000:
                    df_trades.iloc[i] = -2000
                    current_position -= 2000

        
        return df_trades

if __name__ == "__main__":  	
    
    learner= StrategyLearner(commission=9.95)

    seed = 903941473 
   
    np.random.seed(seed) 
    random.seed(seed)

    learner.add_evidence(symbol="JPM", 
                   sd=dt.datetime(2008, 1, 1), 
                   ed=dt.datetime(2009, 12, 31), 
                   sv=100000)

    learner.start_val=100000
    learner.commission=9.95
    learner.impact=0.005
            
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

    
    holdings_insample_df=mk.compute_portvals(df_trades_insample,  learner.start_val, learner.commission, learner.impact)
    holdings_outsample_df=mk.compute_portvals(df_trades_outsample, learner.start_val, learner.commission, learner.impact)
    
    stcs_insample=mk.statistics(holdings_insample_df)
    stcs_outsample=mk.statistics(holdings_outsample_df)
    #print("insample",stcs_insample)  
    #print("outsample",stcs_outsample)	        






    '''
    df_trades=learner.testPolicy( symbol="JPM",  		  	   		 	   			  		 			     			  	 
        sd=dt.datetime(20, 1, 1),  		  	   		 	   			  		 			     			  	 
        ed=dt.datetime(2011, 12, 31),  		  	   		 	   			  		 			     			  	 
        sv=100000,  		)

    print(df_trades)
    trade1 = np.count_nonzero(df_trades)
    print("helloword")
    print(trade1)
    

   
    
    holdings_testing_df=mk.compute_portvals(df_trades,  start_val,  commission,  impact)
    print(holdings_testing_df)
    stcs=mk.statistics(holdings_testing_df)
    print(stcs)
    '''