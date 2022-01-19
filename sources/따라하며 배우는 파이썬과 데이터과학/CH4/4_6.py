print("---메뉴---")
print("햄버거(B)")
print("Chicken(C)")
print("Pizza(P)")

print("Choose menu...: ")
food = str(input())

if(food == 'b' and 'B'):
    food = '햄버거'

elif(food == 'c' and 'C'):
    food = "Chicken"

elif(food == 'p' and 'P'):
    food = "Pizza"

else :
    print("선택한 메뉴가 없습니다.")

print("You choose", food)
