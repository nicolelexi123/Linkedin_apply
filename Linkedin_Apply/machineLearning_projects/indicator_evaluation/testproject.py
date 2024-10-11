from util import get_data
import pandas as pd  
import matplotlib.pyplot as plt 
import datetime as dt
import TheoreticallyOptimalStrategy as tos
import marketsimcode as msim
import numpy as np
import indicators as idt

def author():  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    :return: The GT username of the student  		  	   		 	   			  		 			     			  	 
    :rtype: str  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    return "xi6"  # Change this to your user ID 


if __name__ == "__main__":  	
     	   		 	   			  		 			     			  	 
    df_trade=tos.testPolicy(symbol="JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31), sv=100000) 
 

    portvals = msim.compute_portvals(df_trade, start_val=100000, commission=0, impact=0)
  
    
    portvals_normalized=portvals/portvals.iloc[0]
    

   
    
    df_benchmark_trade=pd.DataFrame(index=portvals.index)
    df_benchmark_trade = pd.DataFrame(index=portvals.index, columns=['Benchmark'])
    df_benchmark_trade = df_benchmark_trade.fillna(0)
    df_benchmark_trade.iloc[0] = [1000]
    

 
    # benchmark is “JPM”
    df_benchmark_JPM=df_benchmark_trade.copy()
    df_benchmark_JPM.columns=['JPM']


    benchmark_JPM=msim.compute_portvals(df_benchmark_JPM,start_val=100000,commission=0,impact=0)
    
    benchmark_normalized=benchmark_JPM/benchmark_JPM.iloc[0]
    

    
    plt.figure(figsize=(10, 5))
    plt.plot(portvals_normalized, color='red', label='Portfolio Normalized')
    plt.plot(benchmark_normalized, color='purple', label='Benchmark Normalized')
    plt.title('Portfolio and Benchmark Normalized Performance')
    plt.xlabel('Date')
    plt.ylabel('Normalized Value')
    plt.legend()
    ##plt.show()
    plt.savefig('images/Figure1.png', format='png')	
    
    
    
    # create table show statistics
    
    portvals_stats = msim.statistics(portvals)
    benchmark_stats = msim.statistics(benchmark_JPM)
    print(portvals_stats)
    print(benchmark_stats)


   
    sd = dt.datetime(2008, 1, 1)
    ed = dt.datetime(2009, 12, 31)
    symbol='JPM'
    df= get_data([symbol], pd.date_range(sd, ed))
    df.drop(columns=["SPY"], inplace=True)
   


    
    normalized_price = df[symbol] / df[symbol].iloc[0]

    # Calculate indicators
    sma_price = idt.calculate_sma_price(df, symbol, 20) 
    momentum_series = idt.calculate_Momentum(df, symbol, 14)
    bb_percentage_series = idt.calculate_BB(df, symbol, 20)
    PPI_series = idt.calculate_PPI(df, symbol, 12, 26)
    ema_price_series=idt.calculate_ema_price(df,symbol,14)
   

    sma = df[symbol].rolling(window=20).mean()
    std = df[symbol].rolling(window=20).std()
    bb_upper = sma + 2*std
    bb_lower = sma - 2*std  

    # Plotting

   
    # indicator 1 price/ sma(20)
    plt.figure(figsize=(10, 5))  
    plt.plot(normalized_price, label='Normalized Price')  
    plt.plot(sma_price, label='Price/SMA(20)')  
    plt.title('Normalized Price VS SMA(20)/Price')  
    plt.axhline(1, color='red', linestyle='--')
    plt.xlabel('Date')
    plt.legend()  
    #plt.show() 
    plt.savefig('images/Figure2.png', format='png')	

   


    # indicator 2：Momentum vs Normalized Price
    plt.figure(figsize=(10, 5))  
    plt.plot(momentum_series, label='Momentum(14)')  
    plt.plot(normalized_price, label='Normalized Price') 
    plt.title('Momentum vs Normalized Price')  
    plt.axhline(0, color='red', linestyle='--') 
    plt.xlabel('Date')
    plt.legend()
    #plt.show() 
    plt.savefig('images/Figure3.png', format='png')	  
    

    # indicator3--BB
    fig4, axs = plt.subplots(2, 1, figsize=(10, 5), sharex=True)

    
    axs[0].plot(bb_percentage_series, label='BB Percentage')
    axs[0].set_title('Bollinger Bands Percentage')
    axs[0].legend()

    axs[1].plot(bb_upper, label='BB Upper Band')
    axs[1].plot(bb_lower, label='BB Lower Band')
    axs[1].plot(df[symbol], label='Price')
    axs[1].set_title('Bollinger Bands(20)')
    axs[1].legend()
    plt.xlabel('Time')
    plt.tight_layout()
    #plt.show()
    plt.savefig('images/Figure4.png', format='png')	


    # indicator4--PPI


    fig5, axs = plt.subplots(2, 1, figsize=(10, 5), sharex=True)

    axs[0].plot(PPI_series, label='PPI')
    axs[0].set_title('PPI')
    axs[0].legend()

    axs[1].plot(normalized_price, label='Price')
    axs[1].set_title('Normalized Price')
    axs[1].axhline(0, color='red', linestyle='--')
    axs[1].legend()
    plt.xlabel('Time')
    plt.tight_layout()
    plt.savefig('images/Figure5.png', format='png')	


    # indicator5--price/ema

    plt.figure(figsize=(10, 5))  
    plt.plot(ema_price_series, label='Price/EMA-14')  
    plt.axhline(1, color='red', linestyle='--')
    plt.title('Price/EMA-14')  
    plt.xlabel('Date')
    plt.legend()  
    #plt.show() 
    plt.savefig('images/Figure6.png', format='png')	


   





    