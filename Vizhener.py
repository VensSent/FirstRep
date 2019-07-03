import re

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
bigalphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
letter = input("Enter the text you want to encrypt on russian: ")
key = input("Enter the secret word:")
cipher = ""

j = 0
for i in letter:
    if re.search(r"[А-Я]", i) or re.search(r"[а-я]", i):
        if i in alphabet:
            index = (alphabet.index(i) + alphabet.index(key[j])) % 33
            cipher += alphabet[index]
        else:
            index = (bigalphabet.index(i) + alphabet.index(key[j])) % 33
            cipher += bigalphabet[index]
        if j == len(key) - 1:
            j = 0
        else:
            j += 1
    else:
        cipher += i

print(cipher)
