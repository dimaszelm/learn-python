class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= Point.MAX_COORD:
            self.x = x
            self.y = y
    # @classmethod
    # def set_bound(cls, left):
    #     cls.MIN_COORD = left

    def __getattribute__(self, item):
        if item =="x":
            raise ValueError("Доступ запрещен")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == "z":
            raise AttributeError("недопустимое имя атрибута")
        else:
            object.__setattr__(self, key, value)
            # self.__dict__[key] = value

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        print("__delattr__ : "+ item)
        object.__delattr__(self, item)



pt1 = Point(1, 2)
pt2 = Point(10,20)
del pt1.x
print(pt1.__dict__)
# a = pt1.y
# print(a)
# pt1.set_bound(-100)
# print(pt1.__dict__)
# print(Point.__dict__)
