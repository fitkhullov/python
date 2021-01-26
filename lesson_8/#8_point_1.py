#point_1
class Date:
    def __init__(self, string):        
        self.string = string
    
    @property
    def string(self):
        return self._string
    
    @string.setter
    def string(self, string):
        if type(string) != str:
            print('input a string type obj, you donut!')
            self._string = ''
            return
        self._string = string
        return
    
    @classmethod
    def parser(cls, string):
        if type(string) == str:
            try:
                date = list(map(int, string.split('-')))
            except ValueError as val_err:
                print(str(val_err) + '\n' + 'cant parse string into a date, you donut!')
                return
        return date
    
    @staticmethod
    def day_in_month_of_year(month, year):
        from math import floor
        return 29 if (year%400 == 0 and month == 2) else 28 + (month + floor(month/8)) % 2 + 2 % month + 2 * floor(1/month) 
    
    @staticmethod
    def validation_test(list_of_num):        
        if list(map(type, list_of_num)) != [int]*3:
            print('wrong date, you donut!')
            return False
        elif (list_of_num[0] > 31 or list_of_num[1] > 12) or (list_of_num[0] <= 0 or list_of_num[1] <= 0 or list_of_num[2] <= 0):
            print('wrong date, you donut!')
            return False
        elif (list_of_num[0] > Date.day_in_month_of_year(list_of_num[1], list_of_num[2])):
            print('wrong date, you donut!')
            return False
        return True
            
date = Date('asdsdf')
date.string
print(date.string)
date.parser(date.string)
date.string = '12--12-2004'
print(date.string)
date.parser(date.string)
date.string = '30-2-2000'
print(date.string)
print(date.parser(date.string))
Date.validation_test(date.parser(date.string))
date.string = '29-2-2000'
print(date.string)
print(date.parser(date.string))
Date.validation_test(date.parser(date.string))