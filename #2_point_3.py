#point_3
seasons = {'Зима': [12, 1, 2] , 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
month = int(input('Введите номер месяца:'))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)
        break