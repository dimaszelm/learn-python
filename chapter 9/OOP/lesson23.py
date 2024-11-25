class Geom:
    __name = "Geom"

    def __init__(self, x1, x2, y1, y2):
        print(f"инициализатор Geom для {self.__class__}")
        # self.__verefy_coord(x1)
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._fill = 0
        self._name = self.__name


    def _verefy_coord(self, coord):
        return 0 <= coord < 100





class Rect(Geom):
    def __init__(self, x1, x2, y1, y2, fill = "red"):
        super().__init__(x1, x2, y1, y2)
        self._fill = fill
        self._verefy_coord(x1)

    def get_coords(self):
        return(self._x1, self._y1)




# r = Rect(0,0,10,20)
# r.get_coords()
# k = Rect(1,2,3,4)
# k._verefy_coord(1)
# print(k.__dict__)
