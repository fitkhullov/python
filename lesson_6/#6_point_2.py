#point_2
class Road:
    one_square_meter = 25
    def __init__(self, length, width):
        self._len = length
        self._wid = width
        
    def mass_of_asphalt(self, thick):
        return self._len*self._wid*self.one_square_meter*thick/1000

road = Road(20, 5000)
print(road.mass_of_asphalt(5))
print(road.mass_of_asphalt(10))
