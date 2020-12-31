#point_5
proc = float(input('Введите значение выручки:'))
cost = float(input('Введите значение издержек:'))
if (proc > cost):
    profit = proc - cost
    print('Прибыль = {}'.format(profit))
    print('Рентабельность выручки = {}'.format(profit/proc))
    n = int(input('Введите кол-во рабочих:'))
    print('Прибыль фирмы в расчете на одного сотрудника = {}'.format(profit/n))    
elif (proc < cost):
    print('Убыток')
else: print('Нерассмотренный случай')

