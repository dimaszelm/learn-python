# print("Я к вам пишу - чего же боле?")
# print("Что я могу еще сказать?")
# print("Теперь, я знаю, в вашей воле?")
# e = ZeroDivisionError("Деление на 0")
#
# print("Меня презреньем наказать. ")
# print("Но вы, к моей несчастной доле")
# print("Хоть каплю жалости храня,")
# print("Вы не оставите меня.")


class ExceptionPrint(Exception):
    """Общий класс исключений принтера"""

class ExceptionPrintSendData(ExceptionPrint):
    """Класс исключений для отправки данных принтеру"""
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str(self):
        return f"Ошибка : {self.message}"

class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f"печать: {str(data)}")

    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExceptionPrintSendData(1,2,3)

    def send_to_print(self, data):
        return False


p = PrintData()
p.print("123")

try:
    p.print("123")
except ExceptionPrintSendData:
    print("принтер не отвечает")
except ExceptionPrint:
     print("Общая ошибка печати")