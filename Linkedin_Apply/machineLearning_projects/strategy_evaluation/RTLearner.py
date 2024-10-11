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
import random	 
from scipy import stats	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
class RTLearner(object):  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    This is a Desicion Tree Learner. It is implemented correctly.  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    :param verbose: If “verbose” is True, your code can print out information for debugging.  		  	   		 	   			  		 			     			  	 
        If verbose = False your code should not generate ANY output. When we test your code, verbose will be False.  		  	   		 	   			  		 			     			  	 
    :type verbose: bool  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    def __init__(self,leaf_size=1, verbose=False):  		  	   		 	   			  		 			     			  	 
        """  	
        
        Parameters
        leaf_size (int)  - Is the maximum number of samples to be aggregated at a leaf
        verbose (bool)   - If “verbose” is True, your code can print out information for debugging.
                           If verbose = False your code should not generate ANY output. When we test your code, verbose will be False. 		  	   		 	   			  		 			     			  	 
        """  		
        self.leaf_size = leaf_size
        self.verbose = verbose  
        
        #self.file = open("outputxi8.txt", "w")	   		 	   			  		 			     			  	 
        		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    def author(self):  		  	   		 	   			  		 			     			  	 
        """  		  	   		 	   			  		 			     			  	 
        :return: The GT username of the student  		  	   		 	   			  		 			     			  	 
        :rtype: str  		  	   		 	   			  		 			     			  	 
        """  		  	   		 	   			  		 			     			  	 
        return "xi6"  # replace tb34 with your Georgia Tech username  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    def add_evidence(self, data_x, data_y):  		  	   		 	   			  		 			     			  	 
        """  		  	   		 	   			  		 			     			  	 
        Add training data to learner  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
        :param data_x: A set of feature values used to train the learner  		  	   		 	   			  		 			     			  	 
        :type data_x: numpy.ndarray  		  	   		 	   			  		 			     			  	 
        :param data_y: The value we are attempting to predict given the X data  		  	   		 	   			  		 			     			  	 
        :type data_y: numpy.ndarray  		  	   		 	   			  		 			     			  	 
        """  		  	   		 	   			  		 			     			  	 	   		 	   			  				  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
        # build and save the model  	
        self.RT_tree=self.RT_builder(data_x,data_y,self.leaf_size)	 
         	   		 	   			  		 			     			  	 
        	  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    def query(self, points):  		  	   		 	   			  		 			     			  	 
        """  		  	   		 	   			  		 			     			  	 
        Estimate a set of test points given the model we built.  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
        :param points: A numpy array with each row corresponding to a specific query.  		  	   		 	   			  		 			     			  	 
        :type points: numpy.ndarray  		  	   		 	   			  		 			     			  	 
        :return: The predicted result of the input data according to the trained model  		  	   		 	   			  		 			     			  	 
        :rtype: numpy.ndarray  		  	   		 	   			  		 			     			  	 
        """ 
        predictions=[]
        for test_point in points:
            predictions.append(self.query_test_sample(test_point,self.RT_tree))
        return np.array(predictions)    
        
        #predictions=np.array([self.query_test_sample(test_point,self.RT_tree) for test_point in points])	
       
        #return predictions 
    
    def query_test_sample(self,test_point,RT_tree):
        node_index = 0
        # query one point
        # print(self.RT_tree[node_index])

        while self.RT_tree[node_index][0]!='leaf':
        
            _, feature_index, split_value,lefttree_index, righttree_index=self.RT_tree[node_index]
             
            #feature_index, split_value,lefttree_index, righttree_index=self.RT_tree[node_index]
            if test_point[int(feature_index)]<=float(split_value):
                node_index += int(lefttree_index)
            else:
                node_index += int(righttree_index)
            
        return float(self.RT_tree[node_index][2])
    

    
    '''
    def get_split_value(self,data_x,data_y):
    
        
        bestfeature_index=random.randint(0,data_x.shape[1]-1)
        
        self.file.write(f"This is a line written to a file HALOU  {bestfeature_index}\n", )
        
        split_value=np.median(data_x[:,bestfeature_index])
        # check this split_value is valid at least one element should larger and one is less than split value 
        s_column=data_x[:,bestfeature_index] <= split_value
        if s_column.all() or not s_column.any():
            #split_value should be replaced by mean as backup value
            split_value=np.mean(data_x[:,bestfeature_index])
            s_column=data_x[:,bestfeature_index] <= split_value
                # if the mean as the second split_value still can not separate the training samples
            #if s_column.all() or not s_column.any():
                #raise ValueError("need to update split_value")

        return split_value,bestfeature_index

    '''
    def get_split_value(self, data_x, data_y):
        bestfeature_index = random.randint(0, data_x.shape[1]-1)
            # 使用众数作为分割值
        mode_result = stats.mode(data_x[:, bestfeature_index], axis=None)
        split_value = mode_result.mode[0]  # 选择第一个模式
        # 检查这个split_value是否有效
        s_column = data_x[:, bestfeature_index] <= split_value
        if not s_column.any() or s_column.all():
            split_value=int(np.mean(data_x[:,bestfeature_index]))
            s_column=data_x[:,bestfeature_index] <= split_value
                # if the mean as the second split_value still can not separate the training samples
            if s_column.all() or not s_column.any():
                split_value = data_x[0][0]
                bestfeature_index = 0

        return split_value, bestfeature_index
    
    
    
    def RT_builder(self, data_x,data_y,leaf_size):
        # Base case: create a leaf if the stopping condition is met
        #if data_x.shape[0] <= leaf_size or len(set(data_y)) == 1:
        if data_x.shape[0] <= leaf_size or len(np.unique(data_y)) == 1:
            return np.array([['leaf','NA', np.mean(data_y), 'NA', 'NA']])
    
        split_value, bestfeature_index = self.get_split_value(data_x, data_y)
        
        # Partition the data into left and right subsets
        left_column = data_x[:, bestfeature_index] <= split_value
        right_column = data_x[:, bestfeature_index] > split_value
        
        # If the split doesn't partition the data (all data on one side), create a leaf
        if np.all(left_column) or np.all(right_column):
            return np.array([['leaf','NA', np.mean(data_y), 'NA', 'NA']])
        
        # Recursively build the left and right subtrees
        left_subtree = self.RT_builder(data_x[left_column], data_y[left_column], leaf_size)
        right_subtree = self.RT_builder(data_x[right_column], data_y[right_column], leaf_size)

        root = np.array([['node', bestfeature_index, split_value, 1, 1 + len(left_subtree)]])
        
        # Concatenate the root, left subtree, and right subtree to form the whole tree
        c=np.concatenate((root, left_subtree, right_subtree))
        return np.concatenate((root, left_subtree, right_subtree))
    
    







  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
if __name__ == "__main__":  		  	   		 	   			  		 			     			  	 
    print("the secret clue is 'zzyzx'")  		  	   		 	   			  		 			     			  	 
