cash_plus = int(input("введите выручку  "))
cash_needs = int(input("введите издержки  "))
if cash_plus > cash_needs:
    print("у вас прибыль ")
    cash_your = cash_plus - cash_needs  # прибыль
    rentable = cash_your / cash_plus * 100   # рентабельность
    count_staff = int(input("какая численность сотрудников "))
    cash_one_staff = cash_your / count_staff
    print("ваша рентабельность ", rentable, "%")
    print("прибыль на одного сотрудника ", cash_one_staff)
elif cash_plus < cash_needs:
    print("у вас убыток ")
else:
    print("работаете в ноль")
