import numpy as np
#AX=B‚Ìs—ñŒvZ‚ğ‚·‚é
#A(2X2),B=(1X1)
def num():
    print("a,b,c,d,e,f‚Ì‡‚Å“ü—Í‚µ‚Ä‚­‚¾‚³‚¢")
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
