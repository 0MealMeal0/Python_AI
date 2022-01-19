print("숫자 입력: ", end = '')

num = int(input())

for i in range(num):

    for j in range(num - i):
        print(' ', end = '')        
    
    for k in range(i + 1):
        print('*', end = '')
    
    print()   