import simpy , random
import numpy as np
random.seed(1)
env = simpy.Environment() #シミュレーション環境
queue = []
intime = []

#到着イベント
def arrive():
    while True:
        yield env.timeout(random.expovariate(1.0 / 5)) #平均到着率
        env.process(into_queue())

#待ち行列に並ぶ
def into_queue():
    global queue
    queue.append(env.now)
    if len(queue) > 1:
        return
    while len(queue) > 0:
        yield env.timeout(random.expovariate(1.0 / 3)) #平均サービス律 1/3
        tm, queue = queue[0],queue[1:]
        intime.append(env.now - tm)

# 実行
env.process(arrive())
env.run(1000000)
print('total = %d clients, w = %.2f' % (len(intime), np.average(intime)))
