km = float(input("평균 시속(km/h)을 입력하세요.: "))
h = float(input("이동 시간(h)을 입력하세요.: "))

hour = int(h // 1)
minute = int((h - (hour)) * 60)
second = int(((h - (h // 1)) * 60 - minute) * 60)
print("평균 시속: ", km, " km/h")
print("이동 거리: ", hour, "시간 ", minute, "분", second, ' 초')
print("이동 거리: ", km * h, 'km')

# 참고: https://www.calculatorsoup.com/calculators/time/decimal-to-time-calculator.php