import numpy as np
import matplotlib.pyplot as plt

"""
def result_train(self,rock,sci,pa):
    self.rock = rock
    self.sci = sci
    self.pa = pa
    # 出す手ごとの勝てる確率
    OBVERSE_PROP = np.array([rock, sci, pa])"""

OBVERSE_PROP = np.array([0.3, 0.5, 0.2])

TRIAL_NUMBER = 2000
# 勝負したときの勝敗 { 0 or 1 }
RESULT_DATA = np.array(
    [np.random.binomial(1, p, TRIAL_NUMBER)for p in OBVERSE_PROP])

HAND = range(3)

class Greedy(object):
    def __init__(self):
        self.rewards = dict()
        self.cnt = 0
        self.result = np.zeros(TRIAL_NUMBER)
        self.choiced_hands = np.array([])

    def get_reward(self, hand):
        return RESULT_DATA[hand][self.cnt]

    def estimate_q(self, hand):

        reward = self.rewards.get(hand)
        q = sum(reward) / float(len(reward)) if reward else 0
        return q

    def choice_hand(self):
        choiced_hand = np.argmax(
            [self.estimate_q(hand) for hand in HAND])
        return choiced_hand

    def first_throw(self):
        choiced_hand = np.random.choice(
            list(set(HAND) - set(self.rewards.keys())))
        self.rewards[choiced_hand] = [self.get_reward(choiced_hand)]
        self.cnt += 1

    def throw(self):
        choiced_hand = self.choice_hand()
        self.choiced_hands = np.append(self.choiced_hands, choiced_hand)
        reward = self.get_reward(choiced_hand)
        self.rewards[choiced_hand].append(reward)
        self.result[self.cnt] = reward
        self.cnt += 1

    def execute(self):
        print('execute')
        [self.first_throw() if i < len(HAND) else self. throw()
         for i in range(TRIAL_NUMBER)]

class EpsilonGreedy(Greedy):
    def __init__(self, epsilon):
        self.epsilon = epsilon
        super(EpsilonGreedy, self).__init__()

    def choice_hand(self):
        is_random = np.random.choice(
            2, 1, p=[1 - self.epsilon, self.epsilon])[0]
        choiced_hand = (np.random.choice(HAND) if is_random else
                        np.argmax([self.estimate_q(hand) for hand in HAND]))
        return choiced_hand

def verification(alg, title):
    print('choiced_hands: %s' % alg.choiced_hands)
    print('グーを出した回数: %s' % alg.choiced_hands[alg.choiced_hands==0].size)
    print('チョキを出した回数: %s' % alg.choiced_hands[alg.choiced_hands==1].size)
    print('パーを出した回数: %s' % alg.choiced_hands[alg.choiced_hands==2].size)
    plt.plot(np.cumsum(alg.result) / np.arange(1, TRIAL_NUMBER+1),label=title)
    plt.legend(loc='lower right')
    plt.axhline(y=0.7, color='gray')
    plt.xlabel('play count')
    plt.ylabel('rate')
    plt.ylim(0, 0.8)
    plt.show


epsilons = [0, 0.1, 0.2, 0.3, 0.4]
epsilon_greedy_list = [EpsilonGreedy(epsilon) for epsilon in epsilons]
[eg.execute() for eg in epsilon_greedy_list]
[verification(eg, 'epsilon='+str(eg.epsilon)) for eg in epsilon_greedy_list]
