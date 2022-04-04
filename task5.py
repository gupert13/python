cash_plus = int(input("введите выручку  "))
cash_needs = int(input("введите издержки  "))
if cash_plus > cash_needs:
    print("у вас прибыль ")
elif cash_plus < cash_needs:
    print("у вас убыток ")
else:
    print("работаете в ноль")
