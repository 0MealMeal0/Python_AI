num = int(input("세 자리 정수를 입력하시오.: "))

ooo = num // 100 # num 나누기 100의 몫
oo = (num - (100 * ooo)) // 10 # 100의 자리와 100을 곱하고 원래 숫자랑 빼서 10으로 나눈 몫
o = (num % 100) % 10 # 원본에서 100을 나눈 나머지(두자리수가 나온다)에서 10을 나눈 나머지 

print(o)
print(oo)
print(ooo)

#3.8.2
reverse_num = (o * 100) + (oo * 10) + ooo

print(reverse_num)