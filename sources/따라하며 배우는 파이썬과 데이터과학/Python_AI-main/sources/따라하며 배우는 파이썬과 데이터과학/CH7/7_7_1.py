fruit_list = ['banana', 'orange', 'kiwi', 'apple', 'melon']

print(len(max(fruit_list)))

print("가장 길이가 긴 문자열 : ", end = '')

for i in range(len(fruit_list)):
    if len(max(fruit_list)) == len(fruit_list[i]):
        
        print(fruit_list[i], end = ' ')
        fruit_list.pop[i]

print(fruit_list)
#https://hashcode.co.kr/questions/13142/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%B5%9C%EB%8C%80-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%82%AD%EC%A0%9C