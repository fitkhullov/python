#point_4
from collections import Counter
from random import randint
A = 0 #левая граница интервала генерации
B = 10 #правая
N = 10 #кол-во элементов в исходном списке
start_list = [randint(A,B) for i in range(N)]
#start_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
el_dict = dict(Counter(start_list))
res_list = [key for key, val in el_dict.items() if el_dict[key] == 1]
print(res_list)

