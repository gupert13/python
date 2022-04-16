"""def my_func(x, y):
       return x**y


   my_deg = my_func(int(input('enter a number ')), int(input('enter minus degree ')))
   print(f'{my_deg:04f}')
"""


def my_func(x, y):
    if y + abs(y) == 0 and x > 0:
        i = 0
        my_count = 1
        while i < abs(y):
            my_count = my_count * (1 / x)
            i += 1
    else:
        return "enter correct number"
    return my_count


my_deg = my_func(int(input('enter a number ')), int(input('enter minus degree ')))
print(my_deg)

