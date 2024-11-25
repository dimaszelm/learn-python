# Напишите программу, в которой на основе текста, введенного поль-
# зователем, создается новый текст, в котором по сравнению с исходным
# удалено самое длинное и самое короткое слово. Если таких слов не-
# сколько, то удаляется первое из них. Под словами подразумевать блоки
# текста, разделенные пробелами.

txt = input("Введите текст: ")

def delete_long_short_words(text):
    words = text.split()

    if len(words) < 2:
        return "Текст должен быть больше двух слов"

    long_word = short_word = words[0]

    for word in words:
        if len(word) > len(long_word):
            long_word = word
        elif len(word) < len(short_word):
            short_word = word

    words.remove(long_word)
    words.remove(short_word)

    return " ".join(words)

result_txt = delete_long_short_words(txt)
print("Результат: ", result_txt)