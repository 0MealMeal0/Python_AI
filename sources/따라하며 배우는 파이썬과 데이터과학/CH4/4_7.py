import random

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

print(num1, ' + ', num2, ' = ')
result = int(input())

if(result == (num1 + num2)) : 
    print("Great!")

else :
    print("The answer is ", num1 + num2 )