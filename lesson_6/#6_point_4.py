#point_4
from random import random
class Car:
    def __init__(self, speed = 0, color = None, name = None, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self, speed):
        self.speed = speed
        print('car rides')
        return
    def stop(self):
        self.speed = 0
        print('the car is stopped')
        return
    def turn(self, direction):
        self.direction = direction
        print(f'the car went in the direction {direction}')
        return
    def show_speed(self):
        print(f'current speed of car equals to {self.speed}')
        return

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('high speed! slow down!')
        else:
            super().show_speed()
        return

class SportCar(Car):
    def develop_maximum_speed(self):
        decision = input('ARE YOU SURE ABOUT THAT?:  ')
        if decision.lower() == 'yes':
            self.speed = 9999
        else:
            print('DWEEB')
        return
    def show_speed(self):
        if self.speed == 9999:
            print(f'YOUR SPEED {self.speed}')
        else:
            super().show_speed()
        return
    def where_is_cops(self):
        if self.speed == 9999:
            print('COPS FAR BEHIND DUDE')
        else:
            print('THEY ARE CLOSE DUDE')
        return

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('high speed! slow down!')
        else:
            super().show_speed()
        return

class PoliceCar(Car):
    def __init__(self):
        Car.__init__(self)
        self.is_police = True
    def need_to_police(self, car_type):
        if isinstance(car_type, SportCar) and car_type.speed == 9999:
            self.speed = 9998.5 + random()
            print('GOGOGOGOGOGO')
        else:            
            self.lets_go_for_donuts()
        return
    def lets_go_for_donuts(self):
        print('lets go for donuts')
        self.speed = 40
        self.direction = 'donut market'
    def stop_the_criminal(self, car_type):
        if car_type.speed == 9999 and self.speed > 9999:            
            car_type.speed = 0
            car_type.busted = True
            self.speed = 0
            print('BUSTED')
        else:
            self.lets_go_for_donuts()
            print('we cant catch him')
        return
    

sport_car = SportCar()
sport_car.develop_maximum_speed()
police_car = PoliceCar()
police_car.need_to_police(sport_car)
police_car.show_speed()
police_car.stop_the_criminal(sport_car)
