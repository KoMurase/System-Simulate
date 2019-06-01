import simpy
def myrun(env):
    while True:
        print(env.now)
        yield env.timeout(2)

env = simpy.Environment() #simpyの環境を作成.
#ここにイテレータmyrunをこの環境のプロセスに追加してenv.run関数でシミュレートする
env.process(myrun(env)) #env環境にプロセスを追加
env.run(until = 10) #10単位分だけenv環境の時間を進める
