#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)
tame = [1, 2, 3]
new_list = copy_list(my_list)

print(my_list)
print(new_list)


print(new_list == my_list)
print(new_list is my_list)
print(new_list is tame)
print(my_list is tame)
