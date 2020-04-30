# coding: utf-8

import numpy as np

from .deep_convnet import DeepConvNet

from ..common.functions import softmax

class DL:
    def __init__(self,filepath):
        self.filepath = filepath
        pass
    
    def predict(self,x_test):

        network = DeepConvNet()
        # 加载已被训练好的参数
        network.load_params(self.filepath)
        print("calcualting test accuracy...")

        # 预测
        y = network.predict(x_test,train_flg=False)
        softmax_resutl = softmax(y)
        y = np.argmax(y , axis=1)

        return y,softmax_resutl