# coding: utf-8
import os
import numpy as np
import random
from .deep_convnet import DeepConvNet
from ..dataset.mnist import load_mnist
from ..common.functions import softmax

class DL:
    def __init__(self):
        pass
    
    def predict(self):

        (x_train, t_train), (x_test, t_test) = load_mnist(flatten=False)

        network = DeepConvNet()
        # 加载已被训练好的参数
        network.load_params(os.path.split(os.path.realpath(__file__))[0]+'\deep_convnet_params.pkl')
        print("calcualting test accuracy...")
        sampled = random.randint(1, 1000)
        x_test = x_test[sampled:sampled+1]
        # 预测
        y = network.predict(x_test,train_flg=False)
        softmax_resutl = softmax(y)
        y = np.argmax(y , axis=1)

        return y,softmax_resutl