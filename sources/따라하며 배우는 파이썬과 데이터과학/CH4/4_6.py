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

print("You choose", food)
