# Напишите программу, в которой описывается класс со следующими
# характеристиками. У класса есть конструктор, которому (кроме ссылки
# на объект вызова) передаются два значения. Эти значения присваивают-
# ся полям объекта класса. В классе должен быть описан метод, при вызо-
# ве которого отображаются значения полей класса. Проверьте функцио-
# нальность класса, создав на его основе несколько объектов.

#
# class Myclass:
#     def __init__(self, a,b):
#         self.a = a
#         self.b = b
#
#     def show(self):
#         print(self.a, self.b)
#
#
#
#
# obj_1 = Myclass(1,3)
# obj_2 = Myclass(2,8)
#
#
# obj_1.show()
# obj_2.show()

class Car:
    color = "Yellow"
    def __init__(self, Name, color, type=None):
        self.Name = Name
        self.color = color
        self.type = type
        self.speed = 0

    @property
    def drive(self):
        return self.speed

    @drive.setter
    def drive(self, speed):
        print(f"car edet {speed}")
        self.speed = speed
    @staticmethod
    def stop():
        print("car stop")

    @classmethod
    def stay(cls):
        print("car stay")
        print(cls.color)



# car = Car("Toyota","black")
Car.drive = 10
print(Car.drive)
# speed = car.drive
# print(speed)

# print(Car.stop())
# print(Car.stay())
