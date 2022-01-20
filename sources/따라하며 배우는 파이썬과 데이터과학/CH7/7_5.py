alpha = ('A', 'B', 'C')
nums = ('1', '2')

nums2 = (1, 2)

seats = list()
seats2 = list()

for i in range(len(alpha)):
    for j in range(len(nums)):
        seats.append(alpha[i] + nums[j])

for i in range(len(alpha)):
    for j in range(len(nums2)):
        seats2.append(alpha[i] + str(nums2[j]))

print(seats)
print(type(seats))

print(seats2)
print(type(seats2))
