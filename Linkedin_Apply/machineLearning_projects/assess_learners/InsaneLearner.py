""""""  		  	   		 	   			  		 			     			  	 
"""  		  	   		 	   			  		 			     			  	 
A simple wrapper for linear regression.  (c) 2015 Tucker Balch  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
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
  		  	   		 	   			  		 			     			  	 
import numpy as np  	
from BagLearner import BagLearner
from LinRegLearner import LinRegLearner	  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	   		  	   		 	   			  		 			     			  	 
class InsaneLearner(object):  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    This is a Insane Learner (InsaneLearner). You will need to properly implement this class as necessary.	 	   			  		 			     			  	 
  		Parameters
        verbose (bool)    - If “verbose” is True, your code can print out information for debugging.
                            If verbose = False your code should not generate ANY output. When we test your code, verbose will be False. 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    def __init__(self,verbose = False):  		  	   		 	   			  		 			     			  	 
        self.verbose = verbose  
        self.learners=[BagLearner(learner=LinRegLearner, kwargs={}, bags=20, boost=False, verbose=verbose) for _ in range(20)]
          	   		 	   			  		 			     			  	    		 	   			  		 			     			  	 
    def author(self):  		  	   		 	   			  		 			     			  	 	  	   		 	   			  		 			     			  	 
        return "xi6"  	

    def add_evidence(self, data_x, data_y):  		  	   		 	   			  		 			     			  	 
        for learner in self.learners:
            learner.add_evidence(data_x,data_y)
	  	   		 	   			  		 			     			  	 
    def query(self, points):  		  	   		 	   			  		 			     			  	 
     
        predictions=np.array([new_learner.query(points) for new_learner in self.learners])
        return np.mean(predictions,axis=0)
		  	   		 	   			  		 			     			  	   		  	   		 	   			  		 			     			  	 
if __name__ == "__main__":  		  	   		 	   			  		 			     			  	 
   print("the secret clue is 'zzyzx'")  		  	   		 	   			  		 			     			  	 
 