#point_5
def summ_before_spec(spec, elem_list):
    summ = 0
    if spec in elem_list:
        index = elem_list.index(spec)        
        for el in elem_list[0:index]:
            summ += float(el)            
        return summ, False
    else:
        for el in elem_list:
            summ += float(el)            
        return summ, True
    
spec = 'stop'    
summ = 0
cond = True
while cond:    
    elem_list = [i for i in input().split()]
    curr_summ, cond = summ_before_spec(spec, elem_list)
    summ += curr_summ
    print(summ)

