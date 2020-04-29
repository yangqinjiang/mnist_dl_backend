# coding: utf-8
import sys,os
sys.path.append(os.pardir)
import numpy as np

from .deep_convnet import DeepConvNet
from dataset.mnist import load_mnist


class DL:
    def __init__():
        pass
    
    def predict():

        (x_train, t_train), (x_test, t_test) = load_mnist(flatten=False)

        network = DeepConvNet()
        network.load_params('ch08/deep_convnet_params.pkl')
        print("calcualting test accuracy...")

        sampled = 1000
        x_test = x_test[:sampled]
        t_test = t_test[:sampled]

        classified_ids = []

        acc = 0.0
        batch_size = 100
        # 计算测试集的得分
        for i in range(int(x_test.shape[0] / batch_size)):
            tx = x_test[i*batch_size:(i+1)*batch_size]
            tt = t_test[i*batch_size:(i+1)*batch_size]
            y = network.predict(tx,train_flg=False)
            y = np.argmax(y , axis=1)
            classified_ids.append(y)
            acc += np.sum(y == tt)

        acc = acc / x_test.shape[0]
        print("test accuracy: " + str(acc))