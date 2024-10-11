""""""  		  	   		 	   			  		 			     			  	 
"""Assess a betting strategy.  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
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
  		  	   		 	   			  		 			     			  	 
Student Name: Tucker Balch (replace with your name)  		  	   		 	   			  		 			     			  	 
GT User ID: tb34 (replace with your User ID)  		  	   		 	   			  		 			     			  	 
GT ID: 900897987 (replace with your GT ID)  		  	   		 	   			  		 			     			  	 
"""  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
import numpy as np 
import matplotlib.pyplot as plt
import random
from typing import List
import os
os.environ['PYDEVD_WARN_SLOW_RESOLVE_TIMEOUT'] = '3.0'  # Sets the timeout to 2 seconds

 		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
def author():  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    :return: The GT username of the student  		  	   		 	   			  		 			     			  	 
    :rtype: str  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    return "xi6"  # replace tb34 with your Georgia Tech username.  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
def gtid():  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    :return: The GT ID of the student  		  	   		 	   			  		 			     			  	 
    :rtype: int  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    return 903941473  # replace with your GT ID number 
   		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
def get_spin_result(win_prob):  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    :param win_prob: The probability of winning  		  	   		 	   			  		 			     			  	 
    :type win_prob: float  		  	   		 	   			  		 			     			  	 
    :return: The result of the spin.  		  	   		 	   			  		 			     			  	 
    :rtype: bool  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    result = False  		  	   		 	   			  		 			     			  	 
    if np.random.random() <= win_prob:  		  	   		 	   			  		 			     			  	 
        result = True  		  	   		 	   			  		 			     			  	 
    return result  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 

def one_time_gamble(win_prob:float,max_spin:int) -> List[float]:
    nums_spin=0
    episode_winnings=0
    history_winning=[]
    while episode_winnings < 80 and nums_spin<max_spin:
        won=False
        bet_amount =1
        
        while not won and nums_spin<max_spin:
            won=get_spin_result(win_prob)
            nums_spin+=1
            #print("round %d won %d episode_winnings %d history_winning %d", nums_spin, won, episode_winnings, history_winning )
            if won:
                episode_winnings += bet_amount
            else:
                episode_winnings -= bet_amount
                bet_amount *=2
            history_winning.append(episode_winnings)
            if episode_winnings >=80:
                history_winning=history_winning+[80]*(max_spin-len(history_winning))
                break
    return history_winning


def one_time_gamble_limitation(win_prob:float,max_spin:int) -> List[float]:
    
    nums_spin = 0
    episode_winnings = 0
    history_winning = []
    bankroll = 256  # Gambler's initial bankroll
    bet_amount = 1

    while nums_spin < max_spin and episode_winnings < 80:
        won = get_spin_result(win_prob)  
        nums_spin += 1

        bet_amount = min(bet_amount, bankroll + episode_winnings)

        if won:
            episode_winnings += bet_amount
        else:
            episode_winnings -= bet_amount
            bet_amount *= 2 

        history_winning.append(episode_winnings)

        # Check if the gambler runs out of money
        if episode_winnings <= -256:
            break

    # Fill the rest of the history with the final state of winnings
    fill = 80 if episode_winnings >= 80 else -256
    history_winning=history_winning + [fill] * (max_spin - len(history_winning))
    
    return history_winning

       
         		  	   		 	   			  		 			     			  	 
def test_code(): 
    
     		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    Method to test your code  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    win_prob = 18/38  # set appropriately to the probability of a win  		  	   		 	   			  		 			     			  	 
    np.random.seed(gtid())  # do this only once  		  	   		 	   			  		 			     			  	 
    #(get_spin_result(win_prob))  # test the roulette spin  		  	   		 	   			  		 			     			  	 
    # add your code here to implement the experiments
    episode_winnings = 0
    
    
    #Experiment 1
    
    win_prob = 18/38  
    max_spin =1000
    #print(get_spin_result(win_prob))
    
    #Figure1 simulate 10 episodes
    times=10
    episodes_10=np.array([one_time_gamble(win_prob,max_spin)for _ in range(times)])
    
    
    plt.figure(figsize=(12,6))
    for result in episodes_10:
        plt.plot(result)
    plt.title("Figure1: American Wheel Episodes Winnings")
    #plt.title("American Wheel Episodes Winnings")
    plt.xlabel("Random Spin")
    plt.ylabel("Episode Winnings($)")
    plt.ylim(-256,100)
    plt.xlim(0,300)
    plt.savefig('images/figure1.png', format='png')
    #plt.show()

    
   
    
    

    #Figure2 simulate 1000 times and get  Mean Winnings
    times=1000
    max_spin=1000
    win_prob=18/38
    
    episodes_array =[np.array(one_time_gamble(win_prob,max_spin)) for _ in range(times)]

    episodes_1000 = np.array(episodes_array)
    
    successful_episodes = np.sum(np.max(episodes_1000, axis=1) >= 80)
    #print(successful_episodes)
        

    mean_winnings = np.mean(episodes_1000, axis=0)
    std_dev_winnings = np.std(episodes_1000, axis=0)

    plt.figure(figsize=(12, 6))
    plt.plot(mean_winnings, label='Mean Winnings($)')
    #plt.fill_between(range(len(mean_winnings)), mean_winnings - std_dev_winnings, mean_winnings + std_dev_winnings, color='gray', alpha=0.5)
    upper_line=mean_winnings + std_dev_winnings
    lower_line=mean_winnings - std_dev_winnings
    
    plt.plot(upper_line,label='mean+stdv')
    plt.plot(lower_line,label='mean-stdv')
    plt.title("Figure 2: Mean Winnings Across 1000 Episodes")
    #plt.title("Mean Winnings Across 1000 Episodes")
    plt.xlabel("Random Spin")
    plt.ylabel("Mean Winnings($)")
    plt.ylim(-256, 100)
    plt.xlim(0,300)
    plt.legend()
    plt.savefig('images/figure2.png', format='png')
    #plt.show()

    # Figure 3: Median Winnings
    median_winnings = np.median(episodes_1000, axis=0)

    plt.figure(figsize=(12, 6))

    #plt.fill_between(range(len(median_winnings)), median_winnings - std_dev_winnings, median_winnings + std_dev_winnings, color='gray', alpha=0.5)
    upper_line=median_winnings + std_dev_winnings
    lower_line=median_winnings - std_dev_winnings
    plt.plot(median_winnings, label='Median Winnings Across 1000 Episodes')
    plt.plot(upper_line,label='median+stdv')
    plt.plot(lower_line,label='median-stdv')
    
    
    plt.title("Figure 3: Median Winnings Across 1000 Episodes")
    #plt.title("Median Winnings Across 1000 Episodes")
    plt.xlabel("Random Spin")
    plt.ylabel("Median Winnings($)")
    plt.ylim(-256, 100)
    plt.xlim(0,300)
    plt.legend()
    #plt.show()
    plt.savefig('images/figure3.png', format='png')
    
    
    # Experiment 2 
    times=1000
    max_spin=1000
    win_prob=18/38
    
    episodes_array_limitation =[np.array(one_time_gamble_limitation(win_prob,max_spin)) for _ in range(times)]

    episodes_limitation_1000 = np.array(episodes_array_limitation)     

    mean_winnings = np.mean(episodes_limitation_1000, axis=0)
   
    std_dev_winnings = np.std(episodes_limitation_1000, axis=0)
    
    # Figure 4
    plt.figure(figsize=(12, 6))
    upper_line=mean_winnings + std_dev_winnings
    lower_line=mean_winnings - std_dev_winnings
    plt.plot(mean_winnings, label='Mean Winnings($)')
    plt.plot(upper_line,label='mean+stdv')
    plt.plot(lower_line,label='mean-stdv')
    #plt.title("Mean Winnings Across 1000 Episodes With Limitation")
    plt.title("Figure 4: Mean Winnings Across 1000 Episodes With Limitation")
    plt.xlabel("Random Spin")
    plt.ylabel("Mean Winnings($)")
    plt.ylim(-256, 100)
    plt.xlim(0,300)
    plt.legend()
    #plt.show()
    plt.savefig('images/figure4.png', format='png')
    
    # Figure 5
   
    
    median_winnings =np.median(episodes_limitation_1000, axis=0)

    plt.figure(figsize=(12, 6))
   
    #plt.fill_between(range(len(median_winnings)), median_winnings - std_dev_winnings, median_winnings + std_dev_winnings, color='gray', alpha=0.5)
    upper_line=median_winnings + std_dev_winnings
    lower_line=median_winnings - std_dev_winnings
    plt.plot(median_winnings, label='Median Winnings Across 1000 Episodes With Limitation')
    plt.plot(upper_line,label='median+stdv')
    plt.plot(lower_line,label='median-stdv')
    plt.title("Figure 5: Median Winnings Across 1000 Episodes With Limitation")
    #plt.title("Median Winnings Across 1000 Episodes With Limitation")
    plt.xlabel("Random Spin")
    plt.ylabel("Median Winnings($)")
    plt.ylim(-256, 100)
    plt.xlim(0,300)
    plt.legend()
    plt.savefig('images/figure5.png', format='png')
    #plt.show()


    '''
   # Experiment 3
    times=1000
    max_spin=1000
    win_prob=18/38
    
    episodes_array =[np.array(one_time_gamble_limitation(win_prob,max_spin)) for _ in range(times)]

    episodes_1000 = np.array(episodes_array)
    
    
    final_winnings = episodes_1000[:, -1]
    count_80=np.sum(final_winnings == 80)
    print(count_80)
    
    final_episodes_winning, counts = np.unique(episodes_1000[:,-1], return_counts=True)  
    probabilities = counts / np.sum(counts)
    plt.figure(figsize=(12, 6))
    plt.bar(final_episodes_winning, probabilities, color='skyblue')
    #plt.title("Figure8: Probability Distribution of Episode Winnings")
    plt.title("Probability Distribution of Episode Winnings")
    plt.xlabel("Winnings at End of Episode")
    plt.ylabel("Probability")
    plt.grid(True)
    plt.ylim(0, 1)
    plt.xlim(-300,100)
   #plt.show()
    
    for result in episodes_1000:
         plt.plot(result)
    
    #plt.title("Figure7: American Wheel Episodes Winnings with Limitation over 1000 times ")
    plt.title("American Wheel Episodes Winnings with Limitation over 1000 times ")
    plt.xlabel("Random Spin")
    plt.ylabel("Episode Winnings($)")
    plt.ylim(-256,100)
    plt.xlim(0,300)
   #plt.show()

    '''

    
    
    return

    
         	
    	  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
if __name__ == "__main__":  		  	   		 	   			  		 			     			  	 
    test_code()  		  	   		 	   			  		 			     			  	 
