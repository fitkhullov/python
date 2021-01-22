#point_1
import threading
from time import sleep

class TrafficLight:
    light_order = {'Red': 7, 'Yellow': 2, 'Green': 5}
    
    def __init__(self):
        self.__color = 'Red'
        self.__next_color = 'Red'
        x = threading.Thread(target = self.running)
        x.start()

    def running(self):        
        while True:
            #цвет поменяли ДО начала итерации
            curr_color = self.__color
            if self.__color != self.__next_color:
                return
            print(self.__color)
            self.__next_color = 'Red' if self.__color == 'Green' else list(self.light_order)[list(self.light_order).index(self.__color) + 1]
            
            #цвет поменяли в момент ожидания переключения
            for sec in range(self.light_order[self.__color]):
                print(sec+1)
                if curr_color != self.__color:
                    print('Я СЛОМАЛСЯ(')
                    return
                sleep(1)
            self.__color = self.__next_color
            
            #цвет поменяли после переключения
            if self.__next_color != self.__color:
                return

    def change_color(self, color):
        sleep(0.5)
        self.__color = color.title()
        print(self.__color)
        return

traf_l = TrafficLight()
traf_l.change_color('green')