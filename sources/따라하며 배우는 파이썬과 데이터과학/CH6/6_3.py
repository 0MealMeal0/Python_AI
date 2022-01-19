def max(n1, n2, n3) :
    if(n1 > n2) and (n1 > n3) :
        return n1
    
    elif(n2 > n1) and (n2 > n3):
        return n2
    
    else : 
        return n3
        
def min(n1, n2, n3) :
    if(n1 < n2) and (n1 < n3) :
        return n1
    
    elif(n2 < n1) and (n2 < n3):
        return n2
    
    else : 
        return n3

print("세 수 입력: ", end='')
a, b, c = map(int, input().split())

print("가장 큰 수 : {}".format(max(a, b, c)))
print("가장 작은 수 : {}".format(min(a, b, c)))


