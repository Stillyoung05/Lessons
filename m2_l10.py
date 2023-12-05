# # l = [k for k in input().split()]
# # for h in range(len(l)):
# #     print(h, l[h])
# from enum import Enum
#
#
# # class Months(Enum):
# #     January = 1
# #     February = 2
# #     March = 3
# #     April = 4
# #     May = 5
# #     June = 6
# #     July = 7
# #     August = 8
# #     September = 9
# #     October = 10
# #     November = 11
# #     December = 12
#
# class Regions(Enum):
#     Tashkent = ["Tashkent", "Ташкент", "Toshkent"]
#     Andijan = ["Andijan", "Андижан", "Andijon"]
#     Bukhara = ["Bukhara", "Букхара", ""]
#     Ferghana = ["", "", ""]
#     Jizzakh = ["", "", ""]
#     Namangan = ["", "", ""]
#     Navai = ["", "", ""]
#     Kashkadarya = ["", "", ""]
#     Samarkand = ["", "", ""]
#     Sirdarya = ["", "", ""]
#     Surkhondarya = ["", "", ""]
#     Khorezm = ["", "", ""]
#     Karakalpakistan_Republic = ["", "", ""]
#
#
# regs = {"Tashkent": 1, "Andijan": 2, "Bukhara": 3, "Ferghana": 4, "Jizzakh": 5, "Namangan": 6, "Navai": 7, "Kashkadarya": 8,
#         "Samarkand": 9, "Sirdarya": 10, "Surkhondarya": 11, "Khorezm": 12, "Karakalpakistan_Republic": 13}
#
# key_regs = regs.keys()
# key_regs_l = list(key_regs)
# num = 1
# for f in key_regs:
#     print(f"{f} - {num}")
#     num += 1
# reg_order = int(input("Enter region order: "))
# # lang = input("Enter important language: ")
# print(key_regs_l)
# name = key_regs_l[reg_order - 1]
# region = Regions[name]
# print(region.value[1])
#
# f = input("Enter text: ")
# signs, sign2 = ',', '.'
# words = []
# for g in f.split():
#     if signs in g and sign2 in g:
#         words.append(g.replace(signs, ""))
#         words.append(g.replace(sign2, ""))
#     else:
#         words.append(g)
# ls = []
# for k in words:
#     ls.append(len(k))
# max_word = max(ls)
# print(words[ls.index(max_word)])
# g = input("Enter word: ")
# new_w = ""
# for k in g:
#     if k.isupper():
#         new_w += k.lower()
#     else:
#         new_w += k.upper()
# print(new_w)

def float_range(start, end, step):
    current = start
    while current < end:
        yield current
        current += step

# Example usage
start = float(input("Enter num in float for start: "))
end = float(input("Enter num for end of the range in float: "))
step = float(input("Enter num in float for step value: "))

for value in float_range(start, end, step):
    print(value)
