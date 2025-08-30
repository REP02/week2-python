my_list = []
print (my_list)

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print (my_list)

my_list[1]=15
print (my_list)

my_list += [50, 60, 70]
print (my_list)

my_list.pop(6)
print (my_list)

my_list.sort()

for i in range (len(my_list)):
    if i == len(my_list) - 1:
        my_list.pop(1)
        print(my_list)

#my_list.pop(5)
print (my_list)
last_element = my_list[i-1]
print (last_element)