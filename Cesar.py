alpha = ' abcdefghijklmnopqrstuvwxyz'
alpha2 = ' абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

a = input("Select the language to encrypt and enter rus or eng\n")
if a == "rus":
    x = alpha2
elif a == "eng":
    x = alpha


n = int(input("Enter encryption key \n"))
s = input("Enter text \n").strip()
res = ''

for c in s:
    res += x[(x.index(c) + n) % len(x)]
print('Result: "' + res + '"')
input()