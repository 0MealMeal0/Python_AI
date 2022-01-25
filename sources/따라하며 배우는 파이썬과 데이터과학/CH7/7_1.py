num_list = [100, 200, 300, 400, 500, 600, 700, 800]
high = 6
low = 3

# 1
print(num_list[high]) # 700
# 2
print(num_list[high - 2]) # 500
# 3
print(num_list[high - low]) # 400
# 4
print(num_list[low - high]) # 600
# 5
print(num_list[-1]) # 800
# 6
print(num_list[-low]) # 600
# 7
print(num_list[2 * 3]) # 700
# 8
print(num_list[2] * 3) # 900
# 9
print(num_list[5 % 4]) # 200
# 10
print(len(num_list)) # 8
# 11
print(min(num_list)) # 100
# 12
print(max(num_list)) # 800
# 13
print(num_list[:3]) # [100, 200, 300]
# 14
print(num_list[1:5]) # [200, 300, 400, 500]
# 15
print(num_list[-1:-5:-1]) # [800, 700, 600, 500]
# 16
print(num_list[-5:-1:1]) # [400, 500, 600, 700]
