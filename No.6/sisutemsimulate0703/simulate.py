import matplotlib.pyplot as plt
def calc_money(num,syakkin):
    b = num
    #print(b)
    y1 = syakkin
    month=0
    while month < 360:
        y2 = y1+y1 * 0.02 / 12.0 - b
        y1 = y2

        month += 1
        if y1<=0:
            break
    return y1,month

if __name__ == '__main__':
    saiteki_kingaku =[]
    syakkin = int(input('いくらの借金をしますか?'))
    for b in range(100000,115000,1):
        result = calc_money(b,syakkin)
        if result[0] <=0 and result[1]==360:
            #print('月'+str(b)+'円の時クリア')
            saiteki_kingaku.append(b)
            #print(result[0],result[1])
            plt.plot(result[0],result[1],marker='o')
    print(saiteki_kingaku)
    plt.show()
