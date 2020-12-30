#point_5
def summ_before_spec(spec, elem_list):
    summ = 0
    index = elem_list.index(spec) if spec in elem_list else len(elem_list)
    cond = True if len(elem_list) == index else False   
    for el in elem_list[0:index]:
            summ += float(el)
    return summ, cond

    
spec = 'stop'    
summ = 0
cond = True
while cond:
    elem_list = [i for i in input().split()]
    curr_summ, cond = summ_before_spec(spec, elem_list)
    summ += curr_summ
    print(summ)

