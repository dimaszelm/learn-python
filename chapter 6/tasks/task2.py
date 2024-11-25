# Напишите программу с функцией, аргументом которой передается
# числовой список, а результатом является еще один список, в который
# включены только нечетные числа из списка-аргумента.

num_list = [0,1,2,3,4,5,6,7,8,9,10,11]

def uneven_num(numb_list):
    num_uneven_list = []
    for digit in numb_list:
        if digit % 2 != 0:
            num_uneven_list.append(digit)
    return num_uneven_list

print(uneven_num(num_list))


