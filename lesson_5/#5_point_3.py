#point_3
with open('input_3.txt', 'r') as fout:
    empl_list = [string.split(' ') for string in fout.read().split('\n')]
    mean_sal = 0
    for emp, sal in empl_list:
        sal = float(sal)
        if sal < 20000:
            print(emp)
        mean_sal += sal
    mean_sal /= len(empl_list)
    print(mean_sal)
    