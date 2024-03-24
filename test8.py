my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_list2 = []
for i in my_list:
    print(my_list[i])
    print(i not in my_list2)
    if i not in my_list2:
        
        my_list2.append(i)


print(my_list2)
    
