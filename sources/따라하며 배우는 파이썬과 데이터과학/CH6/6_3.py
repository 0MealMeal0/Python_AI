def max3(n1, n2, n3) :
    if(n1 > n2) and (n1 > n3) :
        return n1
    
    elif(n2 > n1) and (n2 > n3):
        return n2
    
    else : 
        return n3
        
def min3(n1, n2, n3) :
    if(n1 < n2) and (n1 < n3) :
        return n1
    
    elif(n2 < n1) and (n2 < n3):
        return n2
    
    else : 
        return n3

print("3 수를 입력하시오.: ", end='')
a, b, c = map(int, input().split())

print("가장 큰 수 : {}".format(max3(a, b, c)))
print("가장 작은 수 : {}".format(min3(a, b, c)))


