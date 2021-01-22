#point_2
class Clothes:
    tissue_consumption = 0
    def __init__(self, name = None, size = 0):
        self.cons_material = 0 
        self.__name = name
        self.size = size
            
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        try:
            self._size = float(value)
        except ValueError as val_err:
            print(str(val_err)+'\n')
            print('size must be a number')
            try:
                tmp = self._size
            except AttributeError as att_err:
                self._size = 0            
        Clothes.tissue_consumption -= self.cons_material
        self.cons_material = self.own_tiss_cons()
        Clothes.tissue_consumption += self.cons_material
        return
    
    def own_tiss_cons(self):
        if self._size == 0:
            return 0
        return self._size*self._a + self._b
    
class Coat(Clothes):
    def __init__(self,  size = 0):
        self._a = 1/6.5
        self._b = 0.5
        super().__init__('Пальто', size)
        

        
class Costume(Clothes):
    def __init__(self,  size = 0):
        self._a = 2
        self._b = 0.3
        super().__init__('Костюм', size)
        
coat = Coat('sd')
costume = Costume(20)
print(coat.cons_material)
print(costume.cons_material)
print(Clothes.tissue_consumption)
coat.size = 0
print(coat.cons_material)
print(Clothes.tissue_consumption)
coat.size = 10
print(coat.cons_material)
print(Clothes.tissue_consumption)
coat.size = 'sd'
print(coat.cons_material)
print(Clothes.tissue_consumption)
coat.size = 0
print(coat.cons_material)
print(Clothes.tissue_consumption)