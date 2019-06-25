import matplotlib.pyplot as plt
def main():
    E = int(input('積み込み量をいくらにしますか'))
    M1 = 500 + E
    height = 0
    t = 0
    g = 9.81
    v1 = 0
    V = []
    H = []
    time = []
    while height < 160000:
        #syohi = int(input('消費量はいくらにしますか(max:10 kg/s)'))
        syohi = 10.0
        M2 = M1 - syohi*4
        M = 0.5*(M1+M2)
        F = 300 * 9.81 *4*syohi - M*g
        a = F/M
        M1 = M2


        print('M:'+str(M))
        v2 = v1+a
        print('v2:'+str(v2))
        height += 0.5*(v1+v2)
        v1 = v2

        E -= 0.5*syohi*4
        print('E:'+str(E))
        if E <= 0 :
            print('燃料なくなりました')
            break
        t += 1
        V.append(v2)
        H.append(height)
        time.append(t)

        #確認
        print('height:'+str(height))
        print('v2:'+str(v2))
        print(str(t)+'s')

    Y = [V,H]
    fig = plt.figure()
    ax1 = fig.add_subplot()
    #y1 = V
    #t = 横軸
    ln1 = ax1.plot(time,V,)

    for i in Y:
        plt.plot(time,i)
    plt.show()


if __name__=='__main__':
    main()

    """
    消費燃料Xkgとすると
    F = 4*300*9.81*X   #1s間の推力
    trueF = F - trueM*g
    運動方程式 ma = Fより
    trueM*a = trueF
    count=0
    M=540   #ロケットの燃料なしでの重量
    g=9.81
    engine = 300*9.81
    a = 0
    v=0
    x=0
    m=500 #燃料
    height=0
    suiryoku = 4*300*9.81 #消費燃料Xkgあたり
    """
