#point_2
from random import randint
A = 0 #левая граница интервала генерации
B = 10 #правая
N = 30 #кол-во элементов в исходном списке
rand_list = [randint(A,B) for i in range(N)]
res_list = [rand_list[i] for i in range(len(rand_list)) if rand_list[i-1] < rand_list[i]]
print(res_list)
