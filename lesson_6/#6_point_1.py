#point_1
import threading
from time import sleep

class TrafficLight:
    light_order = {'Red': 7, 'Yellow': 2, 'Green': 5}
    def __init__(self):
        self.__color = 'Red'        
    def running(self):        
        while True:
            print(self.__color)
            curr_color = self.__color
            next_color = 'Red' if self.__color == 'Green' else list(self.light_order)[list(self.light_order).index(self.__color) + 1]
            for sec in range(self.light_order[self.__color]):
                print(sec+1)
                if curr_color != self.__color:
                    print('Я СЛОМАЛСЯ(')
                    return
                sleep(1)
            self.__color = 'Red' if self.__color == 'Green' else list(self.light_order)[list(self.light_order).index(self.__color) + 1]
            if next_color != self.__color:
                return
    def change_color(self, color):
        sleep(0.5)
        self.__color = color.title()
        print(self.__color)
        return

traf_l = TrafficLight()
#traf_l.running()
x = threading.Thread(target = traf_l.running)
x.start()
traf_l.change_color('green')