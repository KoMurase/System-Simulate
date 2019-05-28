import random
import time
import matplotlib.pyplot as plt
win=0
lose=0
draw=0
trial=0
num=[]
win_rate=[]
How_times=int(input('何回じゃんけんしますか？？'))

while trial<How_times:
    print('じゃんけん')
    #print("Let's play rock-paper-scissors")
    #print("Rock,Paper,Scissors! 1.2.3!!!\n")
    com=random.randint(1,3)
    you=int(input("グー:1 パー:2 チョキ:3 \n1,2,3のいずれかをタイプしてください>>>   "))

    if you==1:
        print('あなたはグー')
    elif you==2:
        print('あなたはパー')
    elif you==3:
        print('あなたはチョキ')
    else:
        print('1,2,3を入力してください（#^ω^）')
        continue

    if com==1:
        print('CPはグー')
    elif com==2:
        print('CPはパー')
    else:
        print('CPはチョキ')

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
        #print('win:'+str(win)+'   trial'+str(trial))
        #print('num:'+str(num))
        print('勝率: '+str(rate))
        #print('win_rate:'+str(win_rate)+'%')
    else:
        print('You Lose...')
        lose+=1.0
        trial+=1.0
        num.append(trial)
        rate=round(win/trial*100,5)
        win_rate.append(rate)
        #print('lose:'+str(lose)+'   trial'+str(trial))
        #print('num:'+str(num))
        print('勝率: '+str(rate))
    print('\n')
if rate < 50:
    print('じゃんけん弱いですね~')
elif rate == 50:
    print('気が合いますね!')
else:
    print('じゃんけん強いですね')

plt.plot(num,win_rate)
plt.show()
