def max2(m ,n) :
    if(m > n) :
        return m
    else:
        return n

def min2(m, n) :
    if(m > n) :
        return n

    else :
        return m

print("100 과 200중 큰 수는 : {}".format(max(100, 200)))
print("100 과 200중 작은 수는 : {}".format(min(100, 200)))
