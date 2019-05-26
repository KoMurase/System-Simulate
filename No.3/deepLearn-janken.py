# https://hinaser.github.io/Machine-Learning/sample-rock-scissors-paper.html
import os
import numpy as np
import tensorflow as tf
import time
import datetime as dt
#self　インスタンス自身を示すものである

def winning_hand(self,rock,scissors,paper)->[float,float,float]:
    mx=max([rock,scissors,paper])
    if rock == mx:
        return [0,0,1]
    if scissors == mx:
        return [1,0,0]
    if paper == mx:
        retrun [0,1,0]

def get_supervised_data(self,n_data=None):
    if n_data is None:
        n_data = self.number_of_data

        #トレーニングデータ生成
        supervised_data_input = []
        supervised_data_output = []
        for i in range(n_data):
            rock_prov,scissors_prob,paper_prob = self.opponent_hand()
            input_probs = [rock_prob, scissors_prob, paper_prob]
            supervised_data_input.append(input_probs)
            supervised_data_out.append(self.winning_hand(*input_probs))
        return {'input': supervised_data_input,'output': supervised_data_output}

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string('summary-dir','/tmp/tensorflow/summary',"TensorBoard用のログを出力するディレクトリのパス")
tf.app.flags.DEFINE_integer('max-epoch',100,"最大学習エポック数")
tf.app.flags.DEFINE_integer('batch-size',10,"1回のトレーニングステップに用いる絵d－他のバッチサイズ")
tf.app.flags.DEFINE_float('learning-rate',0.07,"学習率")
tf.app.flags.DEFINE_integer('test-data',10,"学習用データの数")
tf.app.flags.DEFINE_integer('training_data',1000,"学習用データの数")
tf.app.flags.DEFINE_boolean('skip-training',False,"学習をスキップしてテストだけする場合は指定")

def train_and_test(training_data,test_data):
    if len(training_data['input']) != len(training_data['output']):
        print("トレーニングデータの入力と出力のデータの数が一致しません")
        return
    if len(test_data['input']) != (test_data['output']):
        print("テストデータの入力と出力のデータの数が一致しません")
        return

    #　ニューラルネットワークの入力部分の作成
    with　tf.name_scope('Inputs'):
        input = tf.placeholder(tf.float32,shape = [None, 3],name= 'Input')
    with tf.name_scope('Outputs'):
        true_output = tf.placeholder(tf.float32,shape = [None,3],name = 'Output')

    #ニューラルネットワークのレイヤーを作成する関数
    def hidden_layer
