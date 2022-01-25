import random

winner_num1 = random.randint(0, 9)
winner_num2 = random.randint(0, 9)
winner_num3 = random.randint(0, 9)

goal = 0

print(winner_num1, winner_num2, winner_num3)

user_num1, user_num2, user_num3 = map(int, input("세 복권번호를 입력하세요.: ").split())

if(user_num1 == winner_num1):
    goal+=1

elif(user_num1 == winner_num2):
    goal+=1

elif(user_num1 == winner_num3):
    goal+=1

if(user_num2 == winner_num1):
    goal+=1

elif(user_num2 == winner_num2):
    goal+=1

elif(user_num2 == winner_num3):
    goal+=1

if(user_num3 == winner_num1):
    goal+=1

elif(user_num3 == winner_num2):
    goal+=1

elif(user_num3 == winner_num3):
    goal+=1


if(goal == 3): 
    print("1억원")

elif(goal == 2): 
    print("1천만원")

elif(goal == 1): 
    print("1만원")
