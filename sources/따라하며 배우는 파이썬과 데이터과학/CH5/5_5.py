depth = 30
day = 1
location = 0

while(location <= 30): 

    for day in range(1, 14):
        location += location + 2
        print("day :  {} 달팽이의 위치 : {} 미터".format(day, location))