number1 = int(input("введите целое число "))

a = number1  # счетчик цикла
max_number = 0

while a > 0:
    b = a % 10
    a = a // 10

    if b > a % 10 and b > max_number:
        max_number = b

print("самая большая цифра в числе  ", max_number)


