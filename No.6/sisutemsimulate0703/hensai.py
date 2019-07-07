# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
print('人生設計のシミュレーションをします\n')
d1 = int(input('いくらの借金をしますか??'))
month = 0
print(str(d1)+'円の借金をしました')
x = int(input('月々いくら払う予定ですか?'))
bonus = int(input('ボーナス払いはいくらにしますか?'))
zandaka = []
m = []
while d1 > 0:
    d2 = d1+d1 * 0.02 / 12.0-x
    d1 = d2
    #zandaka.append(d1)
    #m.append(month)
    month += 1
    #print(d1)
    #print(month)
    if month % 6 == 0:
        d2 = d1 - bonus
        d1 = d2
if month == 360:
    print('clear')
else:
    print('not clear')
plt.plot(m,zandaka)
plt.show()
