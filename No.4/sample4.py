import random
import numpy as np
from datetime import datetime
print('ただ今の時刻'+datetime.now().strftime("%Y/%m/%d %H:%M:%S")+'\n')


seat = np.array([[0],[0 for j in range(10)]],
        [[1],[0 for j in range(10)]],
        [[2],[0 for j in range(10)]],
        [[3],[0 for j in range(10)]],
        [[4],[0 for j in range(10)]],
        [[5],[0 for j in range(10)]],
        [[6],[0 for j in range(10)]],
        [[7],[0 for j in range(10)]],)#[[座席番号0~8][0~7200s]]
seat = np.array(seat)

print(len(seat))
print(seat.shape)
print(seat)
print(seat(2,2))
"""
person =[]
time = []
number_of_people = random.randint(3,11)
print('人の割合'+str(number_of_people))
for i in range(6):
    for j in range(number_of_people):
        r=random.randint(600*i,600*(i+1))
        person.append(r)

print(person)
person.sort()
print(person)
print(len(person))


for i in range(7200): #時間を進める
    for j in range(6*number_of_people):#用意したpersonの長さ
        if i==person[j]:
            print('修正前'+str(person[j]))
            person[j]+=random.randint(600,1440)

            for check in range(8):
                print(check)
                if seat[[check],:]==0:
                    seat[[check],:]=1
                    break
                elif seat[[check],:]==1 :
                    seat[[check+1],:]+=1
                elif seat[[check],:]==1 and seat[[check+1],:]==1:
                    person[j]+=17


                    #person[num]+=17
                    break
            print('修正後'+str(person[j]))
            print(seat)
"""
