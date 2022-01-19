list1 = ['I like', 'I love']
list2 = ['pancakes.', 'kiwi juice.', 'espresso.']

for i in range(len(list1)) :
    for j in range(len(list2)):
        print("{} {}".format(list1[i], list2[j]))