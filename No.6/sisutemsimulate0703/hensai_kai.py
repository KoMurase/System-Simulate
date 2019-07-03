# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt


class life:
    def __init__(self):
        d1 = self.d1
        month = 0
        x = self.x
        bonus =self.bonus
        
    def cal_money(self,d1,x,bonus):
        zandaka = []
        m = []
    
        while d1 > 0:
            d2 = d1+d1 * 0.02 / 12.0-x
        
            d1 = d2
            month += 1
            mk_graph(month,d1)
            
            print(d1)
            print(month)
            
            zandaka.append(d1)
            m.append(month)
            
            if month % 6 == 0:
                d2 = d1 - bonus
                d1 = d2
                
        return month,d1
        
    
    


if __name__ == '__main__':
    print('人生設計のシミュレーションをします\n')
    
    d1 = int(input('いくらの借金をしますか??')) 
    print(str(d1)+'円の借金をしました')
    x = int(input('月々いくら払う予定ですか?'))
    bonus = int(input('ボーナス払いはいくらにしますか?'))
    
    result=life.cal_money(d1,x,bonus)
    
    if result[0] < 360:
        print('clear')
    else:
        print('not clear')
    
    