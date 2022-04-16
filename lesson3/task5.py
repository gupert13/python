def my_func(arg):
    my_su = 0
    for el in arg:
        my_su = my_su + int(el)
    return my_su


my_sum = 0
my_symbol = ''
while my_symbol != 'h':
    my_num = input('enter numbers with space (h - exit) ')
    my_enter = my_num.split()
    if my_enter.count('h'):
        my_symbol = 'h'
        my_enter = my_enter[:my_enter.index('h')]
    my_sum = my_sum + my_func(my_enter)
    print(my_sum)
