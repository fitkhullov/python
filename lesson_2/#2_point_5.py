#point_5
import random
N = 10
k = 0 #итератор
rate_list = [random.randint(0, 100) for i in range(N)]
rate_list.sort(reverse = True)
print(rate_list)
new_el = int(input('Введите новый элемент рейтинга:'))
for el in rate_list:
    if new_el < el:
        k += 1                       
    else:
        rate_list.insert(k, new_el)
        break
if k == len(rate_list):
    rate_list.append(new_el)
print(rate_list)