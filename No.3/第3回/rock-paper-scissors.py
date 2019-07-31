import random
import time

win=0
lose=0
draw=0
num=0
while num<101:
    
    print("Let's play rock-paper-scissors")
    print("Rock,Paper,Scissors! 1.2.3!!!")
    you=int(input('1:Rock 2:Paper 3:Scissors'))
    com=random.randint(1,3)
    
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    if com==1:
        print('CPはグー')
    elif com==2:
        print('CPはパー')
    else com==3:
        print('CPはチョキ')
        
    result=(com-you+3)%3
    
    num+=1
