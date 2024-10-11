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
  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
class BagLearner(object):  	  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    This is a Bootstrap Aggregataion Learner (BagLearner). You will need to properly implement this class as necessary.	  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    Parameters
        learner (learner) - Points to any arbitrary learner class that will be used in the BagLearner.
        kwargs            - Keyword arguments that are passed on to the learner’s constructor and they can vary according to the learner
        bags (int)        - The number of learners you should train using Bootstrap Aggregation. 
                            If boost is true, then you should implement boosting (optional implementation).
        verbose (bool)    - If “verbose” is True, your code can print out information for debugging.
                            If verbose = False your code should not generate ANY output. When we test your code, verbose will be False. 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    def __init__(self, learner, kwargs = {"argument1":1, "argument2":2}, bags = 20, boost = False, verbose = False):	  	   		 	   			  		 			     			  	 
        """  		  	   		 	   			  		 			     			  	 
        Constructor method  		  	   		 	   			  		 			     			  	 
        """  	
        self.learner = learner
        self.kwargs = kwargs	
        self.bags = bags
        self.boost = boost
        self.verbose = verbose  
        self.learners = [learner (**kwargs) for _ in range(bags)] 		 	   			  		 			     			  	 
        #pass  # move along, these aren't the drones you're looking for  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    def author(self):  		  	   		 	   			  		 			     			  	 
        """  		  	   		 	   			  		 			     			  	 
        :return: The GT username of the student  		  	   		 	   			  		 			     			  	 
        :rtype: str  		  	   		 	   			  		 			     			  	 
        """  		  	   		 	   			  		 			     			  	 
        return "xi6"  # replace tb34 with your Georgia Tech username  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 

            
    def get_bag(self, data_x, data_y):
        num_items = int(data_x.shape[0] * 0.6) # 60% of samples
        data_x_subset, data_y_subset = [], []
        for _ in range(num_items):
            i = np.random.randint(0, data_x.shape[0])
            data_x_subset.append(data_x[i,:])
            data_y_subset.append(data_y[i])
        return np.array(data_x_subset), np.array(data_y_subset)

        '''
        index_s = np.random.choice(data_x.shape[0], sample_size, replace=True)
        data_x_subset=data_x[index_s]
        data_y_subset=data_y[index_s]
        return np.array(data_x_subset), np.array(data_y_subset)
        '''
            
    def add_evidence(self, data_x, data_y):  		  	   		 	   			  		 			     			  	 
        """  		  	   		 	   			  		 			     			  	 
        Add training data to learner  	
        Parameters
            data_x (numpy.ndarray) – A set of feature values used to train the learner
            data_y (numpy.ndarray) – The value we are attempting to predict given the X data	  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
        :param data_x: A set of feature values used to train the learner  		  	   		 	   			  		 			     			  	 
        :type data_x: numpy.ndarray  		  	   		 	   			  		 			     			  	 
        :param data_y: The value we are attempting to predict given the X data  		  	   		 	   			  		 			     			  	 
        :type data_y: numpy.ndarray  		  	   		 	   			  		 			     			  	 
        """  
        n = data_x.shape[0]
        sample_size=int(data_x.shape[0]*0.6) # we set 60% as the trainning sample size
        for i in range(self.bags):
            data_x_subset, data_y_subset = self.get_bag(data_x, data_y)

            # training the ramdom choice data in learner
            #new_learner = self.learner(**self.kwargs)
            #print(i, len(data_x_subset), data_x_subset[1])
            #print(i, len(data_y_subset), data_y_subset[1])
            self.learners[i].add_evidence(data_x_subset, data_y_subset)
            
           		 	   			  		 			     			  	 

  		  	   		 	   			  		 			     			  	 
    def query(self, points):  		  	   		 	   			  		 			     			  	 
        """  		  	   		 	   			  		 			     			  	 
        Estimate a set of test points given the model we built.  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
        :param points: A numpy array with each row corresponding to a specific query.  		  	   		 	   			  		 			     			  	 
        :type points: numpy.ndarray  		  	   		 	   			  		 			     			  	 
        :return: The predicted result of the input data according to the trained model  		  	   		 	   			  		 			     			  	 
        :rtype: numpy.ndarray  		  	   		 	   			  		 			     			  	 
        """  	
        predictions=[]	  	   		 	   			  		 			     			  	 
        for learner in self.learners:
            pred_number=learner.query(points)
            predictions.append(pred_number)
        return np.mean(np.array(predictions),axis=0)

  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
if __name__ == "__main__":  		  	   		 	   			  		 			     			  	 
    print("the secret clue is 'zzyzx'")  		  	   		 	   			  		 			     			  	 
