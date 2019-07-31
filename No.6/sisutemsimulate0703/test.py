import matplotlib.pyplot as plt
import time
def calc_money(num,c,syakkin):
    b = num
    bonus = c
    y1 = syakkin
    month=0
    while month < 360:
        y2 = y1+y1 * 0.02 / 12.0 - b
        y1 = y2

        month += 1
        if month % 6 == 0:
            y2 = y1 - bonus
            y1 = y2
        if y1 <= 0:
            break
    return y1,month

if __name__ == '__main__':
    start = time.time()
    saiteki_kingaku =[]
    syakkin = int(input('いくらの借金をしますか?'))

    for c in range(100000,150000,5000):
        for b in range(5000,110000,1):
            result = calc_money(b,c,syakkin)
            if result[0] <=0 and result[1]==360:
                saiteki_kingaku.append({b,c})
                #print(result[0],result[1])
                #plt.plot(result[0],result[1],marker='o')
    print(saiteki_kingaku)
    #plt.show()
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
