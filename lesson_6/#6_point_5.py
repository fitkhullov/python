class Stationery:
    def __init__(self, title = None):
        self.title = title
    def draw(self):
        print('Запуск отрисовки.')
        return

class Pen(Stationery):
    def draw(self):
        self.title = 'pen'
        print(f'start drawing with {self.title}')
        return
    
class Pencil(Stationery):
    def draw(self):
        self.title = 'pencil'
        print(f'start drawing with {self.title}')
        return
    
class Handle(Stationery):
    def draw(self):
        self.title = 'handle'
        print(f'start drawing with {self.title}')
        
pen = Pen()
pencil = Pencil()
handle = Handle()
pen.draw()
pencil.draw()
handle.draw()