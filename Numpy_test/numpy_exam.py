# Numpy 라이브러리 import
import numpy as np

# Numpy 배열 생성
# 1차원 배열(벡터) 생성하기
x1 = np.array([1.0, 2.0, 3.0])
y1 = np.array([5.0, 10.0, 15.0])


# 2차원 배열(행렬) 생성하기
x2 = np.array([[1.0, 2.0], [3.0, 4.0]])
y2 = np.array([[5.0, 10.0], [15.0, 20.0]])

# numpy 배열 원소 접근
print('x1[0]의 값 : ', x1[0])
print('x2[1][0]의 값 : ', x2[1][0])

# 행렬의 형상 shape
print('x1의 형상 : ', x1.shape)

#Numpy 배열 연산하기
print('x1 + y1 : ', str(x1 + y1))
print('x1 - y1 : ', (x1 - y1))
print('x2 + y2 : ', (x2 + y2))
print('x2 * y2 : ', (x2 * y2))