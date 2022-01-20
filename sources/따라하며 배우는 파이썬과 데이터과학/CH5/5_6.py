from sympy import fu


fuel = 500

while(1):

    print("충전 또는 사용한 연료를 +/- 기호와 함께 입력하세요.: ", end = '')
    gas_value = int(input())    

    fuel = fuel + gas_value
    print("현재 탱크양은 {}입니다.".format(fuel))

    if(fuel < (500 * 0.1)):
        print("경고 : 연로가 10%미만이니 충전하세요!")
        break