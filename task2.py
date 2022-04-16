def data_func(name1, date1, city1, email1, phone1):
    my_list = [name, date, city, email, phone]
    return ' '.join(my_list)


name = input('enter your name ')
date = input('enter your date of birth ')
city = input('enter your city ')
email = input('enter your email ')
phone = input('enter your phone ')

print(data_func(name1=name, date1=date, email1=email, city1=city, phone1=phone))
