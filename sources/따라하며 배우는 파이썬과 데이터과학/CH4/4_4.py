num = int(input("정수: "))

if (num % 2 == 0):
    print(num, "은 2로 나누어 집니다.")
else:
    print(num, "은 2로 나누어 지지 않습니다.")

if (num % 3 == 0):
    print(num, "은 3으로 나누어 집니다.")
else:
    print(num, "은 3으로 나누어 지지 않습니다.")

if (num % 2 == 0) and (num % 3 == 0):
    print(num, "은 2와 3으로 나누어 집니다.")
else:
    print(num, "은 2와 3으로 나누어 지지 않습니다.")

