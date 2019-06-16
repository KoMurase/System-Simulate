import random

END_TIME = 1000
P1 = 0.1 #到着間隔10s
P2 = 0.3 #処理時平均5s

def main():
    total_queue=0
    queue = 0
    time=0
    while time<END_TIME:
        if queue != 0:
            if random.random()/END_TIME < P2:
                queue-=1
        if random.random()/END_TIME < P1:
            queue+=1

        time+=1
        total_queue += queue

    print('average = '+str(total_queue/time))

if __name__=='__main__':
    main()
