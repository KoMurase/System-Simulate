import matplotlib.pyplot as plt
from pprint import pprint
#def main(E,consumption):
def main(E):
    #E = int(input('積み込み量をいくらにしますか'))
    M1 = 500 + E
    height = 0
    t = 0
    g = 9.81
    v1 = 0
    V = []
    H = []
    time = []
    while height < 160000 :
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
    return height,v1
#def mk_graph():
    #fig,axes = plt.subplots(3,3,figsize=(10,10))
#    for ax, result_graph in zip(axes.ravel,set)

    fig,ax1 = plt.subplots()
    ax1.plot(V,color = 'green',label='速度',)
    #y1 = V
    #t = 横軸
    ax2 = ax1.twinx()
    ax2.plot(H,color = 'skyblue',label='高度')
    plt.axhline(y=160000,color='red')
    plt.xlabel('時間[s]')
    plt.show()

#def kikan(V,)

if __name__=='__main__':
    #set = [3000,4000,5000]
    result=main(4000)

    kikan(height,v)

    fig,ax1 = plt.subplots()
    ax1.plot(result[0],color = 'red',label='速度',)
    ax2 = ax1.twinx()
    ax2.plot(result[1],color = 'skyblue',label='高度')
    plt.axhline(y=160000,color='yellow')
    plt.xlabel('時間[s]')
    plt.show()
