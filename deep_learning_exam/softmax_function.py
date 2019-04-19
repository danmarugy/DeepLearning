import numpy as np

# 소프트 맥스 함수
# 분류에 사용된다.
# 예를 들어 데이터가 어느 클래스에 속하느냐는 문제
# 예)사진 속 인물의 성별을 분류하는 문제

# 지수 함수의 어려운점
# 지수는 수치가 크기 때문에 오버플로우 문제가 발생할 확률이 높다
# 지수 함수의 특징은 어떤 정수를 더해도 (혹은 빼도) 결과는 바뀌지 않는다.
# 보통 최대값을 빼준다.

# 소프트 함수의 출력은 0에서 1사이의 실수이며 또 소프트 맥스 함수의 출력의 총합은 1이된다.
class softmax:

    # 오버플로우가 발생할 확률이 높은 함수
    # def softmax(self, a):
    #     exp_a = np.exp(a) #지수 함수
    #
    #     sum_exp_a = np.sum(exp_a) #지수 함수의 합
    #     y = exp_a / sum_exp_a

        # return y

    # 수정된 함수
    def softmax(self, a):
        c = np.max(a)
        exp_a = np.exp(a-c) # 오버플로우 대책
        sum_exp_a = np.sum(exp_a)
        y = exp_a / sum_exp_a

        return y