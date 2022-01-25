def is_prime(n) :
    for i in range(2, (n - 1)) :
        if(n % i == 0) :
            return False
    
    return True

print("소수 검사 수 입력: ", end = '')
num = int(input())
print("소수인가요?: ", end='')
print(is_prime(num))


