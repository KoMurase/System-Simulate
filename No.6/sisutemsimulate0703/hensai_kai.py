import matplotlib.pyplot as plt
import time
def calc_money(num,c,syakkin):
    b = num
    bonus = c
    #print(b)
    y1 = syakkin
    month=0
    while month < 360:
        y2 = y1+y1 * 0.02 / 12.0 - b
        y1 = y2

        month += 1
        if month % 6 == 0:
            y2 = y1 - bonus
            y1 = y2
        if y1<=0:
            break
    return y1,month,bonus

if __name__ == '__main__':
    start = time.time()
    saiteki_kingaku =[]
    syakkin = int(input('いくらの借金をしますか?'))
    #kigen = int(input('返済期間は何か月にしますか?'))
    for c in range(100000,200000,1):
        print(c)
        for b in range(5000,15000,1):
            result = calc_money(b,c,syakkin)
            if result[0] <=0 and result[1]==360:
                #print('月'+str(b)+'円の時クリア')
                saiteki_kingaku.expend([b,c])
                #print(result[0],result[1])
                #plt.plot(result[0],result[1],marker='o')

    print(saiteki_kingaku)

    #plt.show()
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
