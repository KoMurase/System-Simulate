# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 11:37:57 2019

@author: cgub0035
"""
import random
import matplotlib.pyplot as plt

def MontyHall(N):
    correct = 0
    correct_par = []
    trial = 0
    trial_data =[]
    for i in range(N):
        doors = [1,2,3]
        atari = random.choice(doors)
        player =int(input('箱1,2,3どれを選びますか?'))
        print(atari)
        if player == atari:
            print('正解')
            
        else:
            print('不正解')
        choice = int(input('選ぶ手を変えますか'))
            
    plt.plot(X,choice_chage)
     plt.plot(X,choice_hold)
    plt.show()

if __name__=='__main__':
    N=int(input('試行回数'))
    MontyHall(N)
    