import numpy as np	
import random
import math	  
  		 	   			  		 			     			  	 
seed=5  	   			  		 			     			  	 
number_sample=np.random.randint(10,1001)	
number_features=np.random.randint(2,11)	  
x=np.random.rand(number_sample,number_features)*200
coefficients=np.random.rand(number_features)*5
intercept=np.random.rand()*10
y=(x@coefficients)+intercept	   		 	   			  		 			     			  	 
		  	   		 	 
print(y.shape)
print(len(y))
print(x.shape)
		  	   		 	   			  		 			     			  	 
 		  	   		 	   			  		 		