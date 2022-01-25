#딥러닝 구동을 위한 케라스 함수 호출
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
# 필요한 라이브러리 가져오기
import numpy as np
import tensorflow as tf
import time
#실행 시 같은 결과를 출력하기 위한 부분
start = time.time()
np.random.seed(3)
tf.random.set_seed(3)
# 준비된 수술 환자 데이터 불러오기
Data_set = np.loadtxt("dataset/ThoraricSurgery.csv", delimiter=",")
# 환자 기록과 수술 결과를 X, Y로 구분해 저장
X = Data_set[: ,0:17]
Y = Data_set[: ,17]
# 딥러닝 구조 결정 - 모델 결정하고 실행
model = Sequential()
model.add(Dense(30, input_dim=17, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
#딥러닝 실행
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, Y, epochs=100, batch_size=5)
# epochs: 반복횟수, batch_size: 몇 개씩 학습할 것 인지

print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간