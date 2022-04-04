timesec = int(input("введите время в секундах  "))
hour = timesec // 3600
minut_1 = timesec % 3600 // 60
sec_1 = timesec % 60
print(f"время в формате чч:мм:сс {hour:02d}:{minut_1:02d}:{sec_1:02d}")