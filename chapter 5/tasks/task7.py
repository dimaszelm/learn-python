# Напишите программу для шифрования и дешифрования текста. Текст
# шифруется так: каждая буква заменяется на ту, что размещена от нее
# на две позиции влево. Вторая буква в алфавите заменяется на послед-
# нюю. Первая буква в алфавите заменяется на предпоследнюю.

txt = input("Введите текст: ")

decrypt_txt = ""
result_decrypt_txt = ""
m = ord("a")
n = ord("z")
M = ord("A")
N = ord("Z")

def encrypt (text):
    encrypt_txt = ""
    for s in text:
        k = ord(s)
        if (k >= m and k < n) or (k >= M and k <= N):
            s = chr(k - 3)
        elif k == m + 1:
            s = chr(n)
        elif k == m:
            s = chr(n - 1)
        elif k == M + 1:
            s = chr(N)
        elif k == M:
            s = chr(N - 1)
        encrypt_txt += s
    return encrypt_txt


def decrypt(text):
    decrypt_txt = ""
    for s in text:
        k = ord(s)
        if (k >= m and k < n) or (k >= M and k <= N):
            s = chr(k + 3)
        elif k == n:
            s = chr(m + 1)
        elif k == n - 1:
            s = chr(m)
        elif k == N:
            s = chr(M + 1)
        elif k == N - 1:
            s = chr(M)
        decrypt_txt += s
    return decrypt_txt

encrypted_text = encrypt(txt)
print(f"Зашифрованный текст: {encrypted_text}")

decrypted_text = decrypt(encrypted_text)
print(f"Расшифрованный текст: {decrypted_text}")

