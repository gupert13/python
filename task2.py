
my_list = list(input("enter elements of a list "))

a = 0
b = 1
i = 0

while i < len(my_list)//2:
    my_list[a], my_list[b] = my_list[b], my_list[a]
    a += 2
    b += 2
    i += 1

print(my_list)



