#point_1
from time import sleep

class TrafficLight:
    light_order = {'Red': 7, 'Yellow': 2, 'Green': 5}
    def __init__(self):
        self.__color = 'Red'        
    def running(self):
        print(self.__color)
        for i in range(2):
            sleep(self.light_order[self.__color])
            self.__color = list(self.light_order)[list(self.light_order).index(self.__color)+1]
            print(self.__color)
        sleep(self.light_order[self.__color])
        self.__color = 'Red'
        return


traf_l = TrafficLight()
traf_l.running()
traf_l.running()