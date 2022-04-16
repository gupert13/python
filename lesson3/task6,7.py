def int_func(arg):
    my_wor = ""
    for el in arg:
        if 97 <= ord(el) <= 122:
            my_lo = arg[0]
            my_up = my_lo.upper()
            my_wor = arg.replace(my_lo, my_up)
        else:
            my_wor = "enter correct string "
            break
    return my_wor


my_lis = []
my_phrase = ''
my_str = input('enter a string lower ')
my_list = my_str.split()
for elm in my_list:
    my_lis.append(int_func(elm))
    my_phrase = ' '.join(my_lis)
print(my_phrase)
