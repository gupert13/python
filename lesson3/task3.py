def my_func(arg1, arg2, arg3):
    my_sort = [arg1, arg2, arg3]
    my_sort.sort()
    return my_sort[1] + my_sort[2]


my_sum = my_func(int(input('enter argument1 ')), int(input('enter argument2 ')), int(input('enter argument3 ')))
print(my_sum)
