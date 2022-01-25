print("맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")
print("1) 햄버거")
print("2) 치킨")
print("3) 피자")

print("1에서 3까지의 메뉴를 선택하세요.: ", end='')    

while(1): 
    
    food = str(input())

    if(food == '1' or food == '2' or food == '3'):

        if(food == '1'):
            food = '햄버거'
            print(food, "를 선택하였습니다.")

        elif(food == '2'):
            food = "치킨"
            print(food, "을 선택하였습니다.")

        elif(food == '3'):
            food = "피자"
            print(food, "를 선택하였습니다.")
        
        break

    else:
        print("메뉴를 다시 입력하세요.", end = '')    