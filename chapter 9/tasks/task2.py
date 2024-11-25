# Напишите программу, в которой есть класс с переопределенными ме-
# тодами для приведения к разным типам. В частности, у объекта должны
# быть поля с целочисленным значением, текстом и действительным чис-
# ловым значением. При приведении объекта к целочисленному, тексто-
# вому или действительному числовому типу возвращается значение со-
# ответствующего поля.

class ConvertType:
    def __init__(self, int_value, str_value, float_value):
        self.int_value = int_value
        self.str_value = str_value
        self.float_value = float_value

    def __int__(self):
        return self.int_value

    def __str__(self):
        return self.str_value

    def __float__(self):
        return self.float_value


obj = ConvertType(123, "Hello!", 134.12)

int_value = int(obj)
str_value = str(obj)
float_value = float(obj)

print(f"Integer value: {int_value}")
print(f"String value: {str_value}")
print(f"Float value: {float_value}")



