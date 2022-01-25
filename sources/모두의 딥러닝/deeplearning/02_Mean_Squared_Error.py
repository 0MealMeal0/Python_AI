import numpy as np

#오차를 계산하기 위한 임의의 기울기 a, y 절편 b
fake_a_b = [3, 76]

#x, y 값
data = [[2, 81], [4, 93], [6, 91], [8, 97]]
x = [i[0] for i in data]
y = [i[1] for i in data]
# y = ax + b 의 결과 출력
def predict(x) :
    return fake_a_b[0] * x + fake_a_b[1]

# MSE
def mse(y, y_hat) :
    return ((y - y_hat) ** 2). mean()

# MSE함수를 y값에 대입해 최종 값 구하는 함수
def mse_val(y, predict_result) :
    return mse(np.array(y), np.array(predict_result))

predict_result = []

for i in range(len(x)) :
    predict_result.append(predict(x[i]))
    print("공부 시간 = %.f, 실제 점수 = %.f, 예측 점수 = %.f" % (x[i], y[i], predict(x[i])))

# 최종
print("MSE 최종: " + str(mse_val(y, predict_result)))