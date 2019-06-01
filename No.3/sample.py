import random
import matplotlib.pyplot as plt
win=0
lose=0
draw=0
trial=0
num=[]
win_rate=[]
print('じゃんけんしましょ')
print('最初はグー！じゃんけんほいっ')

while trial<100:
    com=random.randint(1,3)
    try:
        you=int(input('1:グー 2:パー 3:チョキ'))
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
        elif you==3:
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
            print('win_rate:'+str(win_rate)+'%\n')
        else:
            print('You Lose...')
            lose+=1.0
            trial+=1.0
            num.append(trial)
            rate=round(win/trial*100,)
            win_rate.append(rate)
            print('lose:'+str(lose)+'   trial'+str(trial))
            print('num:'+str(num))
            print('win_rate:'+str(win_rate)+'%\n')

    except:
        print('グーチョキパー以外は認めぬ！！')
        print('もう一回や！！！！')

plt.plot(num,win_rate)
plt.show()
