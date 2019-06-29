# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

d1 = 30000000
month = 0
#x = int(input('いくら'))
zandaka = []
m = []
def cal(x):
    while d1>0:
        
        d2 = d1+d1 * 0.02 / 12.0 -x
        d1 = d2
        zandaka.append(d1)
        m.append(month)
        month += 1
        print(d1)
        
        if month ==360:
            print('not clear')
            print(d1)
            break 
        return d1,x
    
print('clear')
print('month:'+str(month))
plt.plot(m,zandaka)
plt.show()

def main():
    for i in range(100000,150000,1):
        result=main(i)
        print(result)
        
        