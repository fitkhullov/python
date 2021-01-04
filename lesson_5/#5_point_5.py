#point_5
with open('input_5.txt', 'w') as fin:
    list_of_num = [float(num) for num in input().split(' ')]
    fin.write(str(list_of_num)[1:-1].replace(',', ''))
    print(sum(list_of_num))