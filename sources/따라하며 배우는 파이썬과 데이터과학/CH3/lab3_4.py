money = int(input("투입한 돈: "))
price = int(input("물건 값: "))

change = money - price

five_hund = change // 500
one_hund = (change % 500) // 100

print("거스름돈: ", change)
print("500원 동전 수: ", five_hund)
print("100원 동전 수: ", one_hund)