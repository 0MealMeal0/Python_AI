def max_and_min(n1, n2, n3) :
    if(n1 > n2) and (n1 > n3) :
        if(n2 > n3) :
            return n1, n3
            #print("가장 큰 수 : {}".format(n1))
            #print("가장 작은 수 : {}".format(n3))
        else :
            return n1, n2
            #print("가장 큰 수 : {}".format(n1))
            #print("가장 작은 수 : {}".format(n2))
    
    elif(n2 > n1) and (n2 > n3):
            if(n1 > n3) :
                return n2, n3
            
            else :
                return n2, n1

    elif(n3 > n1) and (n3 > n2):
            if(n1 > n2) :
                return n3, n2
            
            else :
                return n3, n1

print("3 수를 입력하시오.: ", end='')
a, b, c = map(int, input().split())

max_num, min_num = max_and_min(a, b, c)

print("가장 큰 수 : {}".format(max_num))
print("가장 작은 수 : {}".format(min_num))


