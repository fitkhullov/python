#point_3
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': income*0.8, 'bonus': income*0.2}

class Position(Worker):
    def get_full_name(self):
        return (self.name + ' ' + self.surname)
    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

pos_1 = Position('Jon', 'Don', 'manager', 25000)
print(pos_1.get_total_income())
print(pos_1.get_full_name())