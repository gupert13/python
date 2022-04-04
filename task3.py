a = int(input("введите число "))
i = 0
b = a
sum1 = 0
while i < 3:
    sum1 = sum1 + b
    b = int(f"{b}{a}")
    i += 1

print(sum1)