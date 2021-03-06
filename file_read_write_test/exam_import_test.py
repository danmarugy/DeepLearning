import os, sys
from deep_learning_from_scratch_master.dataset.mnist import load_mnist

# 처음 한번은 몇 분 정도 걸립니다.
(x_train, t_train), (x_test, t_test) = \load_mnist(flatten=True, normalize=False)

# 각 데이터의 형상 출력
print(x_train.shape) #(60000,784)
print(t_train.shape) # (60000,)
print ( x_test.shape) # ( 10000, 784)
print ( t_test.shape) # ( 18000,)