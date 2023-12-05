# from abc import ABC
#
#
# class Book:
#     def __init__(self, name, page, author, f_name):
#         self.name = name
#         self.page = page
#         self.author = author
#
#     @property
#     def info(self):
#         return f"The book\'s name is {self.name}"
#
#     @staticmethod
#     def add(x, y):
#         return sum(x, y)
#
#     @classmethod
#     def introduce(cls):
#         cls.name = "Patrick"
#         return cls.name
#
#
# i1 = Book("PR only", 243, "Jack Maa", "Jeagar")
# print(i1.introduce())
#
#
# class Car(ABC):
#     def __init__(self, engine, price):
#         self.engine = engine
#         self.price = price
#
#
# class Technique(Car):
#     @staticmethod
#     def fly(self):
#         return False


"""Homework"""

s = input("Enter string: ")
data = {"[": "]", "{": "}", "(": ")"}
length = len(s)
if length % 2 == 0 or length % 2 == 0 or length % 6 == 0:
    if s.count("[") == s.count(data["["]) and s.count("{") == s.count(data["{"]) and s.count("(") == s.count(data["("]):
        print(True)
else:
    print(False)
