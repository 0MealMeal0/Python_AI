max = 0
min = 0
counter = 0
while(True):

    print("정수를 입력하세요. : ", end ='')
    num = int(input())
    
    if(num == -99):
        print("{}개 중 가장 큰 정수는 {}이고, 가장 작은 정수는 {} 입니다.".format(counter, max, min))    
        break

    else:
        counter += 1

        if(max <= num):
            max = num
        
        if(min == 0):
            min = num
        
        elif(min >= num) :
            min = num