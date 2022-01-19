depth = 30
day = 1
location = 0

while(True): 

    if location == 0 :
        location = 7

    else :
        location = location + ((7 - 5))
    
    print("day :  {} 달팽이의 위치 : {} 미터".format(day, location))
    
    if(location >= 30) : 
        print("축하합니다. 우물 탈출했습니다.")
        print("우물 탈출에 {}일 걸렸습니다.".format(day))
        break
    
    else:
        day += 1

