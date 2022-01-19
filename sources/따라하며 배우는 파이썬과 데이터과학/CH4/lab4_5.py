import imp


import random

print("동전 게임 시작")
coin = random.randrange(2)

if(coin == 0):
    print("앞면")

elif(coin == 1):
    print("뒷면")