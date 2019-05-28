import random
import time
import matplotlib.pyplot as plt
from statistics import mode

win=0
lose=0
draw=0
trial=0
num=[]
win_rate=[]
user_hand = []
How_times=int(input('何回じゃんけんしますか？？'))

def choiced_hand(max_prop):
    #self.max_prop=max_prop
    if max_prop == 1:
        return 2
    elif max_prop == 2:
        return 3
    else:
        return 1



while trial<How_times:
    print('じゃんけん')
    #print("Let's play rock-paper-scissors")
    #print("Rock,Paper,Scissors! 1.2.3!!!\n")

    #CPの手を決める　じゃんけんの回数が10回以下ならランダム
    #それ以上ならchoiced_hand関数から手を選択
    if trial < 10:
        com = random.randint(1,3)
    else:
        print('学習モードに入ります')
        print(str(mode(user_hand)))
        com = choiced_hand(mode(user_hand))
        # .most_common()メソッドは出現回数順に並べたリストを返すリスト
        #(要素,出現回数)というタプルになっている

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
    user_hand.append(you)
    print(type(user_hand))
    print('user_hand'+str(user_hand))
    print('\n')

if rate < 50:
    print('じゃんけん弱いですね~')
elif rate == 50:
    print('気が合いますね!')
else:
    print('じゃんけん強いですね')

plt.plot(num,win_rate)
plt.show()
