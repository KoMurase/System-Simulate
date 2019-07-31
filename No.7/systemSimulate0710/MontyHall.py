# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 11:26:43 2019

@author: cgub0035
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager
from random import choice

def montyhall(N, doors):
    """ モンティ・ホール問題を解いて勝利したかどうかのベクトルを返す """
    # 試行回数と同じ長さのベクトルを用意する
    arr_picked = np.zeros(N)
    arr_switch = np.zeros(N)

    for i in range(N):
        car = choice(doors) # 車が入っているドアをランダムに決める
        picked = choice(doors) # 正解だと思うドアを選ぶ

        # 司会者がヤギの入ったドアをオープンする
        goat = choice(list(set(doors) - set([picked, car])))

        # 選びなおす
        switch = choice(list(set(doors) - set([picked, goat])))

        # それぞれのベクトルの該当の位置に正解かどうかの結果を格納する
        if picked == car:
            arr_picked[i] = 1 # 選びなおさなかった場合に正解なら 1
        if switch == car:
            arr_switch[i] = 1 # 選びなおした場合に正解なら 1

    # 2 つのベクトルを返却する
    return (arr_picked, arr_switch)

def plot(N, arr_picked, arr_switch):
    """ 結果をプロットする """
    """
    # フォントを環境にあわせて指定しておくと便利
    if sys.platform == "darwin":
        font_path = "/Library/Fonts/Osaka.ttf"
    else:
        font_path = "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf"
    prop = font_manager.FontProperties(fname=font_path)
    """

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    X = np.arange(N) + 1 # 試行回数を X 軸に持ってくる
    picked_car = arr_picked.cumsum() # 累積正解数を求める
    switch_car = arr_switch.cumsum()

    ax.plot(X, picked_car, label='picked up')
    ax.plot(X, switch_car, label='switched car')
    ax.set_title('モンティホール問題の通算当たり回数')
    ax.legend(loc='best')
    plt.savefig('image.png')
    plt.show()

def main():
    N = 100000 # 10000 回シミュレーションする
    doors = np.array([1, 2, 3,4,5])

    # モンティホール問題を解く
    (arr_picked, arr_switch) = montyhall(N, doors)
    # 結果をプロットする
    plot(N, arr_picked, arr_switch)

    # 累計勝利数を算出する
    win_picked = arr_picked.sum()
    win_switch = arr_switch.sum()

    print("ドアを変更しなかった場合: %f %% (%d)" %
          (100.0 * win_picked / N, win_picked))
    print("ドアを変更した場合:      %f %% (%d)" %
          (100.0 * win_switch / N, win_switch))

if __name__ == '__main__':
    main()
