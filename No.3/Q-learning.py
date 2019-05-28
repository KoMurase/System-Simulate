#https://qiita.com/pytry3g/items/6b4634bbb6b7f832093f
#εグリーディ法のメカニズムがまだわからない
import random
random.seed()

num_action = 3
num_state = 3
num_train = 50
alpha = 0.1
epsilon = 0.3
reward = [(0,1,-1),(-1,0,1),(1,-1,0)] #報酬
#先手がグーを出すと,(0,1,-1).仮に後手がグーなら報酬は0,パーなら+1,チョキなら-1
actions = ['Rock', 'Paper', 'Scissors']
#Rock 0, Paper 1,Scissors 2
Q = [[random.random() for _ in range(num_action)] \
                      for _ in range(num_state)]
#hand = random.choice(actions) #先手
#state = actions.index(hand)   #状態sc

def choice_action(s):
    return random_action() if random.random() < epsilon else max_action(s)

def max_action(s):
    return Q[s].index(max(Q[s]))

def random_action():
    random_value = random.random()
    if random_value < 0.33:
        return 0
    elif random_value < 0.66:
        return 1
    return 2

def update(s, a):
    return Q[s][a] + alpha * (reward[s][a] - Q[s][a])
#報酬を得るとQ値を更新.更新式は以下の通り
#Q(s,a)←Q(s,a)+α(r-Q(s,a))

def train():
    print('Initial Q_value')
    print_q_value()
    for i in range(num_train):
        print('Training {}'.format(i+1))
        hand = random.choice(actions)
        state = actions.index(hand)
        action = choice_action(state)
        Q[state][action] = update(state, action)   #update q value
        print_q_value()
def print_q_value():
    print('Rock Paper Scissors')
    for i in range(num_state):
        print("{:.3f} {:.3f} {:.3f}\t".format(*Q[i]), end= '')
    print()

def test(s):
    return Q[s].index(max(Q[s]))

if __name__ == "__main__":
    train()
    for state in [0,1,2]:
        result = test(state)
        print(actions[state],[result])
