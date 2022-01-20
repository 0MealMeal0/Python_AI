list1 = [3, 5, 7]
list2 = [2, 3, 4, 5, 6]

for i in range(len(list1)) :
    for j in range(len(list2)):
        print("{} * {} = {}".format(list1[i], list2[j], list1[i] * list2[j]))

print("####################")

for i in list1:
    for j in list2:
        print("{} * {} = {}".format(i, j, i * j))