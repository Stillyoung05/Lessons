# class My_class:
#     def __init__(self, me):
#         self.me = me
#
#     def __repr__(self):
#         cl_name = self.me
#
#     def __eq__(self, other):
#         return self.me
#
#     def __str__(self):
#         return f"{self.me}"
#
#     def __bool__(self):
#         a = True
#         b = False
#         return a == b
#
#     def __del__(self):
#         print(f"{self} variable deleted")
#
#
# item = My_class(18)
# del item

"""Fib numbers"""

# import sys
#
# sys.set_int_max_str_digits(100000)
#
#
# def fibo(n):
#     if n <= 1:
#         return n
#
#     a = 0
#     b = 1
#     # c = 1
#     for i in range(2, n + 1):
#         a, b = b, a + b
#
#     return b
#     # return c
#
#
# n = int(input("Enter the num: "))
# print(f"The {n}-th Fibonacci number is: {fibo(n)}")

# items = input("Enter items")
"""Homework"""

"""Task1"""

#
# class Coordinate:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return f"Coordinate({self.x}, {self.y})"
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __eq__(self, other):
#         return self.name == other.name and self.age == other.age
#
#
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#     def __str__(self):
#         return f"Book: {self.title} by {self.author}"
#
#
# class Temperature:
#     def __init__(self, celsius):
#         self.celsius = celsius
#
#     def __bool__(self):
#         return self.celsius > 0
#
#
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def __del__(self):
#         print(f"The {self.brand} {self.model} has been deleted.")


"""Task2"""

nums = [int(g) for g in input("Enter nums for list: ").split()]
target = int(input("Enter target num: "))
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print(i, j)
#             break

d = {}
