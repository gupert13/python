
n_month = int(input('enter a number of  month '))

month_dict = {'w': 'winter', 's': 'spring', 'su': 'summer', 'au': 'autumn'}
list1 = [12, 1, 2]
list2 = [3, 4, 5]
list3 = [6, 7, 8]
list4 = [9, 10, 11]

for el in list1:
    if el == n_month:
        print(month_dict['w'])
for el in list2:
    if el == n_month:
        print(month_dict['s'])
for el in list3:
    if el == n_month:
        print(month_dict['su'])
for el in list4:
    if el == n_month:
        print(month_dict['au'])
