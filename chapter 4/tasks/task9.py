# Напишите программу, в которой пользователю предлагается вве-
# сти текстовое значение. На основе текста формируется словарь. Клю-
# чами элементов словаря являются символы из текста. Значение соот-
# ветствующего элемента — это исходный текст, в котором «вычеркнут»
# тот символ, который является ключом. Если при формировании оче-
# редного элемента словаря окажется, что такой ключ уже есть, то соот-
# ветствующий символ пропускается. Например, если пользователь ввел
# текст "ABCABD", то в словаре будут представлены элементы с ключами
# "A", "B", "C" и "D" со значениями соответственно "BCABD", "ACABD",
# "ABABD" и "ABCAB".

txt = input("Введите текст: ")
print( "1".join(txt))
print(txt.split(","))

