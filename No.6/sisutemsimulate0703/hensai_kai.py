# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt


class life:
    def __init__(self):
        self.d1 = d1
        self.month = 0
        self.maituki = maituki
        self.bonus =bonus

    def cal_money(self,d1,maituki,bonus):
        zandaka = []
        m = []
        month = 0
        while d1 > 0:
            d2 = d1+d1 * 0.02 / 12.0 - maituki 

            d1 = d2
            month += 1
            #mk_graph(month,d1)

            print(d1)
            print(month)

            zandaka.append(d1)
            m.append(month)

            if month % 6 == 0:
                d2 = d1 - bonus
                d1 = d2

        return month,self.maituki,self.bonus





if __name__ == '__main__':
    print('人生設計のシミュレーションをします\n')

    #d1 = int(input('いくらの借金をしますか??'))
    print('3000万の借金をするとします')
    d1 = 30000000
    #print(str(d1)+'円の借金をしました')
    #maituki = int(input('月々いくら払う予定ですか?'))
    #bonus = int(input('ボーナス払いはいくらにしますか?'))

    #d1 = 30000000
    #maituki = 78000
    #bonus = 200000
    data = []
    for i in range(100000,300000):
        for j in range(100000,300000,1000):
            maituki=i
            bonus=j
            simulate = life()
            result = simulate.cal_money(d1,maituki,bonus)
            data.append(result)
    print(data)

    #インスタンスの参照
    print(simulate.d1)
    print(simulate.maituki)
    print(simulate.bonus)

    if result[0] <= 360:
        print(result[1])
        print('clear')
    else:
        print('not clear')
