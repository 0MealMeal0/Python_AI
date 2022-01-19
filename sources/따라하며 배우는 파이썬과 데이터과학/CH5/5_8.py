reverse = ''

while(True):
    
    print("정수를 입력하세요. : ", end = '')
    num = str(input())

    if(num == "-99"): # quit
        break
    
    else:
        
        for i in num: # 새로운 문자가  reverse의 앞에 붙는다.
                      # num = 134면
                      # reverse = 1 + ' '
                      # reverse = 3 + 1
                      # reverse = 4 + 3 + 1
            reverse = i + reverse

        print(reverse)

        if(num == reverse):
            print("{}는 거꾸로 정수입니다.".format(num))
        
        else:
            print("{}는 거꾸로 정수가 아닙니다.".format(num))
    
    reverse = ' ' # reverse 변수를 계속 사용하기 위해 초기화

