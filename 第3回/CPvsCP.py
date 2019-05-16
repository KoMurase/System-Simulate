import random
import time
import matplotlib.pyplot as plt
win=0
lose=0
draw=0
trial=0
num=[]
win_rate=[]
while trial<3:
    print('じゃんけん')
    print("Let's play rock-paper-scissors")
    print("Rock,Paper,Scissors! 1.2.3!!!")
    you=random.randint(1,3)
    #you=int(input('1:Rock 2:Paper 3:Scissors'))
    com=random.randint(1,3)


    if com==1:
        print('CPはグー')
    elif com==2:
        print('CPはパー')
    else:
        print('CPはチョキ')

    if you==1:
        print('あなたはグー')
    elif you==2:
        print('あなたはパー')
    else:
        print('あなたはチョキ')

    result=(com-you+3)%3
    if result == 0:
        print('draw')
    elif result==2:
        print('You Win!!')
        win+=1.0
        trial+=1.0
        num.append(trial)
        rate=round(win/trial*100,5)
        win_rate.append(rate)
        print('win:'+str(win)+'   trial'+str(trial))
        print('num:'+str(num))
        print('rate'+str(rate))
        print('win_rate:'+str(win_rate)+'%')
    else:
        print('You Lose...')
        lose+=1.0
        trial+=1.0
        num.append(trial)
        rate=round(win/trial*100,5)
        win_rate.append(rate)
        print('lose:'+str(lose)+'   trial'+str(trial))
        print('num:'+str(num))
plt.plot(num,win_rate)
plt.show()
#要素数の最後の数で割ればよくね？？？by岩崎
