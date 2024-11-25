# Напишите программу, в которой описан класс со следующими свой-
# ствами. В классе описан конструктор, которому в качестве аргументов
# (помимо первой ссылки на создаваемый объект) передаются текст и це-
# лое число, причем в произвольном порядке. Число и текст присваива-
# ются как значения определенным полям. Если переданы два текстовых
# значения, то создается только текстовое поле со значением, получаю-
# щимся объединением значений аргументов. Если аргументами переда-
# ны два числовых поля, то у объекта будет только поле с целочисленным
# значением, равным сумме значений аргументов. В иных случаях поля
# для объекта не создаются. Создать на основе класса объекты и прове-
# рить функциональность кода.

class Myclass:
    def __init__(self, text, num):

        #Вариант через if elif

        # if type(text) == str and type(num) == int:
        #     self.text = text
        #     self.num = num
        #
        # elif type(text) == str and type(num) == str:
        #     self.text = text + num
        #
        # elif type(text) == int and type(num) == int:
        #     self.num = text + num

        #Вариант через match - case
        match (text,num):
            case(str(), int()):
                self.text = text
                self.num = num
            case(str(), str()):
                self.text = text + num
            case(int(), int()):
                self.num = text + num


    def show(self):
        if hasattr(self, 'text'):
            print(f"Text: {self.text}")
        if hasattr(self, 'num'):
            print(f"Number: {self.num}")


obj_txt = Myclass("hello", "world")
obj_numb = Myclass(3, 8)
obj = Myclass("hello", 2)


obj_txt.show()
obj_numb.show()
obj.show()
