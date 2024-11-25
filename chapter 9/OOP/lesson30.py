def func2():
    try:
        return 1 / 0
    except:
        print("func2 error")

def func1():
    try:
        return func2()
    except:
        print("func1 error")

print("Я к вам пишу - чего же боле?")
print("Что я могу еще сказать?")
print("Теперь, я знаю, в вашей воле?")
# try:
func1()
# except:
#     print("func1 error")
print("Меня презреньем наказать. ")
print("Но вы, к моей несчастной доле")
print("Хоть каплю жалости храня,")
print("Вы не оставите меня.")