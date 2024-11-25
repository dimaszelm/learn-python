class Geom:
    name = "Geom"

    def __init__(self, x1, x2, y1, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.fill = 0

    def draw (self):
        print("Рисование линии")



class Line(Geom):
    def draw (self):
        print("Рисование линии")


class Rect(Geom):
    def __init__(self, x1, x2, y1, y2, fill = None):
        self.fill = fill
        print("инициализатор Rect")
        super().__init__(x1, x2, y1, y2)

    def draw (self):
        print("Рисование прямоугольника")

l = Line(0,0, 10 , 20)
r = Rect(1,2,3,4)
print(r.__dict__)