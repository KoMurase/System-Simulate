import numpy as np
#AX=Bの行列計算をする
#A(2X2),B=(1X1)
def num():
    print("a,b,c,d,e,fの順で入力してください")
    a=input()
    b=input()
    c=input()
    d=input()
    e=input()
    f=input()
    return main(a,b,c,d,e,f)

def main(a,b,c,d,e,f):
    A=np.array([[a,b],
               [c,d]])
    B=np.array([e,f])
    
    X=np.linalg.solve(A,B)
    
    print("X=\n"+str(X))
