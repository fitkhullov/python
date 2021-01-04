#point_4
with open('input_4_start.txt', 'r') as fout, open('input_4_end.txt', 'w') as fin:
    ru_num = {'one': 'Один', 'two': 'Два', 'three': 'Три', 'four': 'Четыре'}
    while True:
        try:
            s_num, symb, num = (fout.readline().split(' '))
        except ValueError:
            break
        fin.write(f'{ru_num[s_num.lower()]} {symb} {num}')
