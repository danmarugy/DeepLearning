import numpy as np

class sigmoid:

    # 시그모이드 함수
    def sigmoid(self, x):

        return 1 / (1 + np.exp(-x))