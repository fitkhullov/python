#point_4
string = input()
list_of_string = string.split(' ')
for num, word in enumerate(list_of_string):
    print(f'{num+1}. {word[0:10]}')
    
       