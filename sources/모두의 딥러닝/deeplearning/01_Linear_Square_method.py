import numpy as np

# x, y값
x = [2, 4, 6 ,8]
y = [81, 93, 91, 97]
# x, y 평균
mx = np.mean(x)
my = np.mean(y)
print("x 평균: ", mx)
print("y 평균: ", my)
#기울기분모, (x평균 - x[i]) 의 제곱의 합들을 구한다.
divisor = sum([(mx - i)**2 for i in x])

def top(x, mx, y, my) :
    d = 0
    for i in range(len(x)) :
        d += (x[i] - mx) * (y[i] - my)
    return d
dividend = top(x, mx, y, my)

print("분모: ", divisor)
print("분자: ", dividend)

# 기울기와 절편
a = dividend / divisor
b = my - (mx * a)

print("기울기 a = ", a)
print("y 절편 b = ", b)

