#point_4
string = input()
list_of_string = string.split(' ')
for num, word in enumerate(list_of_string):
    if len(word) > 10:
        print(f'{num+1}. {word[0:10]}')
    else:
        print(f'{num+1}. {word}')