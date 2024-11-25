
def div(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return "деление на ноль"

res = 0
try:
    x, y = map(int, input().split())
    res = div(x ,y)
except ValueError as z:
    print(z)

print(res)
#     return 0, 0
# finally:
#     print("finally выполняется до return")

# x, y = get_values()
# print(x, y)
    # x, y = map(int, input().split())
    # res = x / y
    # with open("myfile.txt") as f:
    #     f.write("hello")

# except FileNotFoundError as z:
#     print(z)
#     except:
#         print("Другая ошибка")
# finally:
#     if f:
#         f.close()
#         print("файл закрыт")