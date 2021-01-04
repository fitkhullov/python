#point_2
with open('input_2.txt', 'r') as fout:
    text = [string.split(' ') for string in fout.read().split('\n')]
    print(len(text)) #кол-во строк
    words_num = 0
    for string in text:
        empty_el = string.count('')
        words_num += len(string) - empty_el
    print(words_num)
    