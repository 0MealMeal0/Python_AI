from sympy import E


print("---메뉴---")
print("햄버거(B)")
print("Chicken(C)")
print("Pizza(P)")

while(1): 
    print("Choose menu...: ", end='')    
    food = str(input())

    if(food == 'b' and 'B'):
        food = '햄버거'
        print("You choose", food)

    elif(food == 'c' and 'C'):
        food = "Chicken"
        print("You choose", food)

    elif(food == 'p' and 'P'):
        food = "Pizza"
        print("You choose", food)
    
    elif(food == 'q'):
        exit()

    else:
        print("다시 입력하세요.")    
    
    
