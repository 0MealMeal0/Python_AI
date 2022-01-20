print("문자를 입력하세요.: ", end = '')
word = str(input())
result = ' '
for i in range(len(word)) :
    result += word[i]
    print(result)

for j in range(len(word)):
    print(result[0:(len(word) - j)])

#for 하나로 돌릴 수 있을까?