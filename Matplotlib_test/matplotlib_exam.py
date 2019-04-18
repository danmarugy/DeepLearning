#  matplotlib 라이브러리 import
import matplotlib.pyplot as plt
# image 모듈에서 imread 함수만 import 함
from matplotlib.image import imread
import numpy as np

# 데이터 준비
x = np.arange(0,6,0.1) #0에서 6까지 0.1간격으로 배열 생성
y1 = np.sin(x)
y2 = np.cos(x)

# 그래프 그리기
plt.plot(x, y1, )
plt.plot()