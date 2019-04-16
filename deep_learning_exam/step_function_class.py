import numpy as np
import matplotlib.pylab as plt
class step_function_class:

    # 부동소수점(실수)만 받아들이는 함수
    # def step_function(self, x):
    #     if x > 0:
    #         return  1
    #     else:
    #         return 0

    # 넘파이 배열도 받아들이는 함수
    def  step_function(self,x):
        y = x > 0
        
        # y는 불린형 값
        print('y : ',y)
        # 블린값을 1과 0으로 변환
        print(y.astype(np.int))

        return y.astype(np.int)

sfc = step_function_class()
x = np.arange(-5.0, 5.0, 0.1)
y = sfc.step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()