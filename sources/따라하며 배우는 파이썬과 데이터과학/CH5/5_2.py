##########################
#5.2.1
print("1 ~ 100 홀수 합1: ")

i = 0
sum = 0
for i in range(100):
    if(i % 2 == 1):
        sum += i

print(sum)
##########################

##########################
#5.2.2
print("1 ~ 100 짝수 합: ")

i = 0
sum = 0
for i in range(101):
    if(i % 2 == 0):
        sum += i

print(sum)
##########################

##########################
#5.2.3
print("시작정수: ", end = '')
start_num = int(input())

print("끝정수: ", end = '')
end_num = int(input())

sum = 0
for i in range(start_num, end_num + 1, 1):
    sum += i

print("{}에서 {}까지 합 = {}".format(start_num, end_num, sum))

##########################