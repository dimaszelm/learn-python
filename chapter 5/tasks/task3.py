# Напишите программу, в которой пользователю предлагается вве-
# сти текст, а затем в этом тексте, без применения специальных методов
# (а именно, не используя метод swapcase()), все большие буквы меня-
# ются на маленькие, а маленькие — на большие.

txt = (input("Введите текст: "))

swap_txt = ""

for char in txt:
    if "a" <= char <= "z":
        swap_txt += chr(ord(char) - 32)
    elif "A" <= char <= "Z":
        swap_txt += chr(ord(char) + 32)
    else:
        swap_txt += char

print(swap_txt)

