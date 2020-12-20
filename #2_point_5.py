#point_5
import random
N = 10
rate_list = [random.randint(0, 100) for i in range(N)]
rate_list.sort(reverse = True)
print(rate_list)
rate_list.append(int(input('Введите новый элемент рейтинга:')))
rate_list.sort(reverse = True)
print(rate_list)