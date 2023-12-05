import random
import string
import itertools
from rarfile import RarFile
# import pyautogui as pg
from time import sleep
import os


def generate_password():
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits

    all_characters = uppercase_letters + lowercase_letters

    password = ''.join(random.choice(all_characters) for _ in range(5)) + str(random.randint(1000, 10000))

    return password


archname = r'E:\routers.rar'  # Shuni ichida test.rar
outfolder = r'E:'  # Menda hammasi Parol degan papkada

r = RarFile(archname)
s = [str(i) for i in range(9 + 1)]
print(generate_password())
for i in itertools.product(generate_password()):
    print(i)
    for el in itertools.product(s, repeat=4):
        # cur_paw = "".join(i) + "".join(list(el))
        cur_paw = generate_password()
        print(cur_paw)
        try:
            r.extractall(outfolder, pwd=cur_paw)
            exit(0)
        except Exception as e:
            print(e)

# while True:
#     passw = generate_password()
#     code.append(passw)
#     pg.write(passw)
#     sleep(1)
#     pg.press("Enter")
#     sleep(0.5)
#     pg.press("Enter")

# while True:
