import numpy as np
def main():
    count=0
    M=540   #ロケットの燃料なしでの重量
    gravity=9.81
    engine = 300*9.81
    a = 0
    v=0
    m=0 #燃料
    height=0
    for m in np.arange(0.0,100.0,0.01):
        for X in np.arange(0.0,100.0,0.01):

            for dt in np.arange(0.0,1000.0,0.01):
                a += (engine*4*X-(m+M-X*dt)*gravity)/(m+M-X)
                height += 0.5*a*dt**2
                #v=v*dt+0.5*a*dt**2
                v += 0.5*a*dt**2
                #count+=1
                print(str(count))
                m+=0.01
                print('m:'+str(m))
                print('height:'+str(height))
                print('v:'+str(v)+'\n')
                if height>160.0 and v>7.90:
                    print('m:'+str(m))
                    print('height:'+str(height))
                    print('v:'+str(v))
                    break





if __name__ =='__main__':
    main()
