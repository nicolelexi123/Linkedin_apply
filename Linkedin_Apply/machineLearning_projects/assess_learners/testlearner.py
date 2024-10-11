""""""  		  	   		 	   			  		 			     			  	 
"""  		  	   		 	   			  		 			     			  	 
Test a learner.  (c) 2015 Tucker Balch  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
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
"""  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
import math  		  	   		 	   			  		 			     			  	 
import sys  
import pandas as pd		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
import numpy as np 
import random 		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
import LinRegLearner as lrl  	
import DTLearner as dt 
import RTLearner as rt 
import BagLearner as bl 
import InsaneLearner as it 
import matplotlib.pyplot as plt	
		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
if __name__ == "__main__":  		  	   		 	   			  		 			     			  	 
    
    if len(sys.argv) != 2:  		  	   		 	   			  		 			     			  	 
        print("Usage: python testlearner.py <filename>")  		  	   		 	   			  		 			     			  	 
        sys.exit(1) 
    filename =sys.argv[1] 	

    
    # pandas recognize the header as default
    # remove 'date' columns

    '''
    df = pd.read_csv(filename)
    df = df.drop(columns=['date'])
    data = df.values # data becomes a Numpyarray excluding the header as the first column.
    '''

    inf = open(sys.argv[1])  		  	   		 	   			  		 			     			  	 
    data = np.array(  		  	   		 	   			  		 			     			  	 
        [list(map(float, s.strip().split(",")[1:])) for s in inf.readlines()[1:]]  		  	   		 	   			  		 			     			  	 
    )  		  	   		 	   			  		 			     			  	 
    
              
    
    #random select training and testing  data set. 
    np.random.seed(903941473)
    np.random.shuffle(data)

    train_rows=int(0.6*data.shape[0])
    
    train_data=data[:train_rows]
    test_data=data[train_rows:]
      	   		 	   			  		 			     			  	 
    # separate out training and testing data  		  	   		 	   			  		 			     			  	 
    train_x=train_data[:, :-1]
    train_y=train_data[:,-1]
    test_x=test_data[:,:-1]
    test_y=test_data[:,-1]	  	 

    '''  		 	   			  		 			     			  	 
    train_rows = int(0.6 * data.shape[0])  		  	   		 	   			  		 			     			  	 
    test_rows = data.shape[0] - train_rows  		  	   		 	   			  		 			     			  	 

      	   		 	   			  		 			     			  	 
    # separate out training and testing data  		  	   		 	   			  		 			     			  	 
    train_x = data[:train_rows, 0:-1]  		  	   		 	   			  		 			     			  	 
    train_y = data[:train_rows, -1]  		  	   		 	   			  		 			     			  	 
    test_x = data[train_rows:, 0:-1]  		  	   		 	   			  		 			     			  	 
    test_y = data[train_rows:, -1]  	
    '''	  	   		 	   			  		 			     			  	  	   		
   	


    print(f"{test_x.shape}")  		  	   		 	   			  		 			     			  	 
    print(f"{test_y.shape}")  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    # create a learner and train it  		  	   		 	   			  		 			     			  	 
    learner = lrl.LinRegLearner(verbose=True)  # create a LinRegLearner  		  	   		 	   			  		 			     			  	 
    learner.add_evidence(train_x, train_y)  # train it  		  	   		 	   			  		 			     			  	 
    print(learner.author())  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    # evaluate in sample  		  	   		 	   			  		 			     			  	 
    pred_y = learner.query(train_x)  # get the predictions  		  	   		 	   			  		 			     			  	 
    rmse = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])  		  	   		 	   			  		 			     			  	 
    print()  		  	   		 	   			  		 			     			  	 
    print("In sample results")  		  	   		 	   			  		 			     			  	 
    print(f"RMSE: {rmse}")  		  	   		 	   			  		 			     			  	 
    c = np.corrcoef(pred_y, y=train_y)  		  	   		 	   			  		 			     			  	 
    print(f"corr: {c[0,1]}")  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    # evaluate out of sample  		  	   		 	   			  		 			     			  	 
    pred_y = learner.query(test_x)  # get the predictions  		  	   		 	   			  		 			     			  	 
    rmse = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])  		  	   		 	   			  		 			     			  	 
    print()  		  	   		 	   			  		 			     			  	 
    print("Out of sample results")  		  	   		 	   			  		 			     			  	 
    print(f"RMSE: {rmse}")  		  	   		 	   			  		 			     			  	 
    c = np.corrcoef(pred_y, y=test_y)  		  	   		 	   			  		 			     			  	 
    print(f"corr: {c[0,1]}")  		

    def mean_absolute_error(true_values,predicted_values):
        absoult_errors=abs(true_values-predicted_values)#for t_values,p_values in zip(true_values,predicted_values)]
        mae=sum(absoult_errors)/len(absoult_errors)  
        return mae

    def r_squared(true_values,predicted_values):
        mean_true_values = sum(true_values) / len(true_values)
    
        # (TSS)
        total_sum_of_squares = sum((true_val - mean_true_values) ** 2 for true_val in true_values)
    
        # Residual sum of squares (RSS)
        residual_sum_of_squares = sum((true_val - pred_val) ** 2 for true_val, pred_val in zip(true_values, predicted_values))
    
        # R-squared
        rsv = 1 - (residual_sum_of_squares / total_sum_of_squares)
    
        return rsv

    
    
    
    # Experiment1 
    leaf_sizes=range(1,20)  
    train_rmses=[]
    test_rmses=[]
    for dt_leaf_size in leaf_sizes:
        learner=dt.DTLearner(leaf_size=dt_leaf_size,verbose=False)
        learner.add_evidence(train_x,train_y)

        #in sample evaluation
        pred_y = learner.query(train_x)  # get the predictions  		  	   		 	   			  		 			     			  	 
        rmse = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])  
        train_rmses.append(rmse)

        # out sample evaluation
        pred_y = learner.query(test_x)
        rmse = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0]) 
        test_rmses.append(rmse)
    
    plt.figure(figsize=(12,6))
    plt.plot(leaf_sizes,train_rmses,label="Training RMSE")
    plt.plot(leaf_sizes,test_rmses,label="Testing RMSE")
    plt.xlabel('Leaf Size')
    plt.ylabel('RMSE')
    plt.title('Trainning vs Testing RMSE regarding to Leaf Size')
    plt.legend()
    #plt.show()
    plt.savefig('images/Figure1.png')
    
    
    
   

    
    
    
    # Experiment2
    bag_number=20
    leaf_sizes=range(1,20)
    bag_train_rmses=[]
    bag_test_rmses=[]
    for BagLearner_leaf_size in leaf_sizes:
       
        
        #bag_learner =bl.BagLearner(learner=learner_dt,kwargs={"leaf_size":BagLearner_leaf_size, "verbose":False},bags=bag_number,boost=False,verbose=False)
        bag_learner =bl.BagLearner(learner=dt.DTLearner,kwargs={"leaf_size":BagLearner_leaf_size, "verbose":False},bags=bag_number,boost=False,verbose=False)
        bag_learner.add_evidence(train_x,train_y)
        

        #in sample evaluation
        baglearner_pred_y = bag_learner.query(train_x)  # get the predictions  		  	   		 	   			  		 			     			  	 
        rmse = math.sqrt(((train_y - baglearner_pred_y) ** 2).sum() / train_y.shape[0])  
        bag_train_rmses.append(rmse)

        # out sample evaluation
        baglearner_pred_y = bag_learner.query(test_x)
        rmse = math.sqrt(((test_y - baglearner_pred_y) ** 2).sum() / test_y.shape[0]) 
        bag_test_rmses.append(rmse)
    
    
    plt.figure(figsize=(12,6))
    plt.plot(leaf_sizes,bag_train_rmses,label="Training RMSE")
    plt.plot(leaf_sizes,bag_test_rmses,label="Testing RMSE")
    plt.xlabel('Leaf Size')
    plt.ylabel('RMSE')
    plt.title('BagLearner_Trainning vs Testing RMSE regarding to Leaf Size')
    plt.legend()
    #plt.show()
    plt.savefig('images/Figure2.png')

    
    
    
    # Experiment3
    #Metrics1 Mean Absolute Error(MAE) and Metrics2 using R square
    
    leaf_sizes=range(1,15)
    dt_train_mae =[]
    dt_test_mae=[]
    rt_train_mae=[]
    rt_test_mae=[]
    dt_train_r2 =[]
    dt_test_r2=[]
    rt_train_r2=[]
    rt_test_r2=[]

    for compare_leaf_size in leaf_sizes:
        # train DT and RT learner 
        learner_dt=dt.DTLearner(leaf_size=compare_leaf_size,verbose=False)
        learner_dt.add_evidence(train_x,train_y)
        learner_rt=rt.RTLearner(leaf_size=compare_leaf_size,verbose=False)
        learner_rt.add_evidence(train_x,train_y)
        
        # in sample
        dt_pred_train_y = learner_dt.query(train_x)
        rt_pred_train_y = learner_rt.query(train_x)
        dt_train_mae.append(mean_absolute_error(train_y, dt_pred_train_y))
        rt_train_mae.append(mean_absolute_error(train_y, rt_pred_train_y))
        dt_train_r2.append(r_squared(train_y, dt_pred_train_y))
        rt_train_r2.append(r_squared(train_y, rt_pred_train_y))


        # out sample
        dt_pred_test_y = learner_dt.query(test_x)
        rt_pred_test_y = learner_rt.query(test_x)
        dt_test_mae.append(mean_absolute_error(test_y, dt_pred_test_y))
        rt_test_mae.append(mean_absolute_error(test_y, rt_pred_test_y))
        dt_test_r2.append(r_squared(test_y, dt_pred_test_y))
        rt_test_r2.append(r_squared(test_y, rt_pred_test_y))

    plt.figure(figsize=(12, 6))
    plt.plot(leaf_sizes, dt_train_mae, label='DT Learner - Training MAE', color='blue')
    plt.plot(leaf_sizes, dt_test_mae, label='DT Learner - Testing MAE', color='red')
    plt.plot(leaf_sizes, rt_train_mae, label='RT Learner - Training MAE', color='green')
    plt.plot(leaf_sizes, rt_test_mae, label='RT Learner - Testing MAE', color='purple')
    plt.xlabel('Leaf Size')
    plt.ylabel('MAE')
    plt.legend()
    plt.title('Effect of Leaf Size on MAE for DT Learner and RT Learner')
    #plt.show()
    plt.savefig('images/Figure3.png')

    plt.figure(figsize=(12, 6))
    plt.plot(leaf_sizes, dt_train_r2, label='DT Learner - Training R-Square', color='blue')
    plt.plot(leaf_sizes, dt_test_r2, label='DT Learner - Testing R-Square', color='red')
    plt.plot(leaf_sizes, rt_train_r2, label='RT Learner - Training R-Square', color='green')
    plt.plot(leaf_sizes, rt_test_r2, label='RT Learner - Testing R-Square', color='purple')
    plt.xlabel('Leaf Size')
    plt.ylabel('R-Square')
    plt.legend()
    plt.title('Effect of Leaf Size on R-Square for DT Learner and RT Learner')
    #plt.show()
    plt.savefig('images/Figure4')
    

    
    
    


        
    




    


    

