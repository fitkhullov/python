#point_1
with open('input_1.txt', 'a') as fin:
    while True:
        string = input()
        if not string:
            break
        else:
            fin.write(string + '\n')
            
