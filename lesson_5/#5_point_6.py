#point_6
with open('input_6.txt', 'r') as fout:
    school_dict = {}
    while True:
        try:
            subj, lect, prac, lab = fout.readline().split(' ')
        except ValueError:
            break
        subj = subj[:-1]
        lect = 0 if lect == '—' else int(lect.replace('(л)', ''))
        prac = 0 if prac == '—' else int(prac.replace('(пр)', ''))
        lab  = 0 if lab  == '—' else int(lab.replace('(лаб)', ''))
        school_dict.update({subj: lect+prac+lab})
print(school_dict)
            