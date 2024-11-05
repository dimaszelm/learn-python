# Напишите программу, в которой используется словарь. Ключами
# в словаре являются фамилии писателей, а значение соответствующего
# элемента — название произведения, написанного автором. В программе
# перебираются значения всех элементов словаря, и для каждого значения
# (название произведения) пользователю предлагается указать фамилию
# автора. После перебора содержимого словаря и получения всех ответов
# программа отображает количество правильных ответов пользователя.


literature = {
    "Толстой": "Война и мир",
    "Достоевский": "Преступление и наказание",
    "Чехов": "Вишневый сад",
    "Пушкин": "Евгений Онегин",
    "Гоголь": "Мертвые души"
}

correct_answers = 0

for author, work in literature.items():
    user_answer = input(f"Какой писатель написал '{work}'? ")
    if user_answer.strip() == author:
        print("Правильно!")
        correct_answers += 1
    else:
        print(f"Неправильно. Правильный ответ: {author}")


print(f"Вы дали {correct_answers} правильных ответов из {len(literature)}.")