def div_func(number1, number2):
    if number2 == 0:
        return 'number2 = 0'
    return number1/number2


my_n = div_func(int(input('enter number1 ')), int(input('enter number2 ')))
print(my_n)

