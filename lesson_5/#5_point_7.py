#point_7
from json import dump
with open('input_7.txt', 'r') as fout, open('output_7.json', 'w') as fin:
    res_list = []
    comp_dict = {}
    average_prof = 0
    n = 0 #кол-во компаний с прибылью
    while True:
        try:
            name, model, proc, costs = fout.readline().split(' ')
        except ValueError:
            break
        proc = float(proc)
        costs = float(costs)
        prof = proc - costs
        if prof > 0:
            average_prof += prof
            n += 1
        comp_dict.update({name: proc - costs})
    average_prof = average_prof if average_prof == 0 else average_prof/n
    res_list.append(comp_dict)
    res_list.append({'average_profit': average_prof})
    dump(res_list, fin)
