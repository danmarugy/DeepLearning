import sys, os
sys.path.append(os.pardir)
import numpy as np
from deep_learning_from_scratch_master.dataset.mnist import load_mnist
from PIL import Image

# 처음 한 번은 몇 분 정도 걸린다.
# x_train : 훈련 레이블 t_train : 훈련 레이블), (x_test : 시험 이미지 t_test : 시험 레이블)
# 인수 normalize, flatten, one_hot_label
# normalize : 입력 이미지의 픽셀값을 0.0~1.0 사이의 값으로 정규화할지를 정함 False로 설정하면 이미지의 픽셀값은 원래 값인 0~255 사이의 값을 유지
# flatten : 입력 이미지를 평탄하게 즉 1차원 배열로 만들지 정한다. False로 설정하면 입력 이미지를 1*28*28의 3차원 배열로, True로 입력시 784개의 원소로 이뤄진 1차원 배열로 저장
# one_hot_label : 원 핫 인코딩 형태로 저장할지 정한다. 예를 들어 [0, 0, 1, 0, 0, 0, 0, 0, 0]처럼 정답인 원소만 1이고 나머지는 0인 배열
# one_hot_label이 False일 경우 7,2와 같이 숫자 형태의 레이블을 저장
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

# 각 데이터의 형상 출력
print(x_train.shape) # (60000, 784)
print(t_train.shape) # (60000,)
print(x_test.shape) # (10000, 784)
print(t_test.shape) # (10000,)

print(len(x_train))


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

img = x_train[0]
label = t_train[0]
print(label) # 5

print(img.shape) # (784,)
img = img.reshape(28,28)
print(img.shape) # (28, 28)

img_show(img)