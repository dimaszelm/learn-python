# Напишите программу, в которой шифруется и дешифруется введен-
# ный пользователем текст. При шифровании каждая буква заменяет-
# ся на следующую (а последняя — на первую), но только эта операция
# отдельно выполняется для гласных букв и для согласных. Для этого
# нужно сформировать список гласных и согласных букв и шифрование
# и дешифрование выполнять на основе этих списков.

VOWELS = "AEIOU"
vowels = "aeiou"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXYZ"
consonants = "bcdfghjklmnpqrstvwxyz"

def encrypt(txt):
    encrypt_list = []

    for char in txt:
        if char in VOWELS:
            index = (VOWELS.index(char) + 1) % len(VOWELS)
            encrypt_list.append(VOWELS[index])

        elif char in vowels:
            index = (vowels.index(char) + 1) % len(vowels)
            encrypt_list.append(vowels[index])

        elif char in CONSONANTS:
            index = (CONSONANTS.index(char) + 1) % len(CONSONANTS)
            encrypt_list.append(CONSONANTS[index])

        elif char in consonants:
            index = (consonants.index(char) + 1) % len(consonants)
            encrypt_list.append(consonants[index])

        else:
            encrypt_list.append(char)

    return "".join(encrypt_list)


def decrypt(txt):
    decrypt_list = []

    for char in txt:
        if char in VOWELS:
            index = (VOWELS.index(char) - 1) % len(VOWELS)
            decrypt_list.append(VOWELS[index])

        elif char in vowels:
            index = (vowels.index(char) - 1) % len(vowels)
            decrypt_list.append(vowels[index])

        elif char in CONSONANTS:
            index = (CONSONANTS.index(char) - 1) % len(CONSONANTS)
            decrypt_list.append(CONSONANTS[index])

        elif char in consonants:
            index = (consonants.index(char) - 1) % len(consonants)
            decrypt_list.append(consonants[index])

        else:
            decrypt_list.append(char)

    return "".join(decrypt_list)


txt = input("Введите текст: ")
encrypted_text = encrypt(txt)
print(f"Зашифрованный текст: {encrypted_text}")

decrypted_text = decrypt(encrypted_text)
print(f"Расшифрованный текст: {decrypted_text}")