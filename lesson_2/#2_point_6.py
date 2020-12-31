#point_6
items = []
cond = True
k = 0 #кол-во элементов в "Товары"
while cond:
    k += 1
    name = input('Введите название товара:').lower()
    price = float(input('Введите цену товара:'))
    quantity = int(input('Введите кол-во товара:'))
    unit = input('Введите единицу измерения товара:').lower()
    items.append((k, {'название': name, 'цена': price, 'количество': quantity, 'ед': unit}))
    cond = True if input('Продолжить ввод? Введите "да", если хотите продолжить:') == 'да' else False
stat_dict = dict()
for specif in items[0][1].keys():
    stat_dict[specif] = []
for key in stat_dict.keys():
    for i in range(k):
        stat_dict[key].append(items[i][1][key])
print(stat_dict)   
    