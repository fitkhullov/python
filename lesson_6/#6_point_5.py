#point_5
class Stationery:
    def __init__(self, title = None):
        self.title = title
    def draw(self):
        print('Запуск отрисовки.')
        return

class Pen(Stationery):
    def draw(self):
        print(f'start drawing with pen that named {self.title}')
        return
    
class Pencil(Stationery):
    def draw(self):
        print(f'start drawing with pencil that named  {self.title}')
        return
    
class Handle(Stationery):
    def draw(self):
        print(f'start drawing with handle that named {self.title}')
        
pen = Pen('Erich Krause')
pencil = Pencil('Cherchil')
handle = Handle('cheap_handle')
pen.draw()
pencil.draw()
handle.draw()