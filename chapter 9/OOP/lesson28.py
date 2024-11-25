# print("Я к вам пишу - чего же боле?")
# print("Что я могу еще сказать?")
# print("Теперь, я знаю, в вашей воле?")
#  1 / 0
# print("Меня презреньем наказать. ")
# print("Но вы, к моей несчастной доле")
# print("Хоть каплю жалости храня,")
# print("Вы не оставите меня.")

try:
    # f = open("myfile2.txt")
    x, y = map(int, input().split())
    res = x / y
# except (ValueError, ZeroDivisionError):
#     print("ошибка типа данных")
except ValueError:
    print("ошибка типа данных")

except:
    print("Ошибка")

print("Штатное завершение")