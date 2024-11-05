# Напишите программу, в которой с использованием операторов цикла
# и форматированных литералов, символом «звездочка» * в области вы-
# вода отображается буква "A".

height = 3
width = height * 2 - 1
mid = width // 2

for i in range(height):
    if i == 0:
        line = f"{'*':^{width}}"
    elif i == height // 2:
        line = f"{'*' * width}"
    else:
        line = f"{'*':<{mid - i}}{'*':>{width - mid + i - 1}}"

    print(line)
