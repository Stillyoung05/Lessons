# file = open('names.txt')
# print(file.read())
# name = input("Ismni kiriting: ")
# line = 0
# by_line = file.readline()
# with open("names.txt", "r") as nm:
#     while True:
#         if nm.readline() == name:
#             line += 1
#             break
#         else:
#             line += 1
# print(line)


# with open("names.txt") as nms:
#     for data in nms:
#

"""Homework"""
# 25.09#

import os

main_folder = "main_folder"

if not os.path.exists(main_folder):
    os.mkdir(main_folder)

subfolders = ["folder1", "folder2", "folder3"]

for subfolder in subfolders:
    subfolder_path = os.path.join(main_folder, subfolder)
    os.mkdir(subfolder_path)

    python_file = os.path.join(subfolder_path, "functions.py")
    file = open("functions.py")
    for a in range(4):
        a = a
    file.write(f"from foder{a} import functions\ndef call():\n    return Function called from folder{a}/functions.py")
    with open(python_file, 'w') as f:
        f.write("# This is the functions.py file in {} folder\n".format(subfolder))
        f.write("# You can define your Python functions here")

print("Done")

# 27.09#


# 29.09#

# class Class1:
#     pass
#
#
# class Class2(Class1):
#     pass
#
#
# class Class3:
#     pass
#
#
# class Class4(Class3):
#     pass
#
#
# class Class5:
#     pass
#
#
# class Class6(Class5):
#     pass
#
#
# class Class7:
#     pass
#
#
# class Class8(Class7):
#     pass
#
#
# class Class9:
#     pass
#
#
# class Class10(Class9):
#     pass
#
#
# class Class11:
#     pass
#
#
# class Class12(Class11):
#     pass
#
#
# class Class13:
#     pass
#
#
# class Class14(Class13):
#     pass
#
#
# class Class15:
#     pass
#
#
# class Class16(Class15):
#     pass
#
#
# class Class17:
#     pass
#
#
# class Class18(Class17):
#     pass
#
#
# class Class19:
#     pass
#
#
# class Class20(Class19):
#     pass


# 04.10#

#
# import random
#
#
# def choose_word():
#     words = ["python", "programming", "challenge", "learning", "coding", "developer", "django", "internet", "algorythm"]
#     return random.choice(words)
#
#
# def display_word(word, guessed_letters):
#     display = ""
#     for letter in word:
#         if letter in guessed_letters:
#             display += letter
#         else:
#             display += "*"
#     return display
#
#
# def guess_the_word():
#     print("Welcome to Guess the Word Game!")
#     secret_word = choose_word()
#     guessed_letters = []
#     attempts = len(choose_word())
#
#     while attempts > 0:
#         print("\nAttempts left:", attempts)
#         current_display = display_word(secret_word, guessed_letters)
#         print("Current Word:", current_display)
#
#         guess = input("Enter a letter: ").lower()
#
#         if len(guess) != 1 or not guess.isalpha():
#             print("Please enter a single alphabetical character.")
#             continue
#
#         if guess in guessed_letters:
#             print("You've already guessed that letter. Try again.")
#             continue
#
#         guessed_letters.append(guess)
#
#         if guess not in secret_word:
#             print("Incorrect guess!")
#             attempts -= 1
#
#         if set(guessed_letters) == set(secret_word):
#             print("Congratulations! You guessed the word:", secret_word)
#             break
#
#     if attempts == 0:
#         print("Sorry, you're out of attempts. The correct word was:", secret_word)
#
#
# guess_the_word()

# 12.10#

from abc import ABC, abstractmethod


# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius * self.radius
#
#     def perimeter(self):
#         return 2 * 3.14 * self.radius


# class Animal(ABC):
#     @abstractmethod
#     def speak(self):
#         pass
#
#
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
#
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"


# class Employee(ABC):
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#
#     @abstractmethod
#     def calculate_salary(self):
#         pass
#
#
# class Manager(Employee):
#     def calculate_salary(self):
#         return 50000


# class Developer(Employee):
#     def calculate_salary(self):
#         return 60000


# class Vehicle(ABC):
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
#
#     @abstractmethod
#     def start_engine(self):
#         pass
#
#
# class Car(Vehicle):
#     def start_engine(self):
#         return "Starting car engine."
#
#
# class Motorcycle(Vehicle):
#     def start_engine(self):
#         return "Starting motorcycle engine."


# class BankAccount(ABC):
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance
#
#     @abstractmethod
#     def deposit(self, amount):
#         pass
#
#     @abstractmethod
#     def withdraw(self, amount):
#         pass
#
#
# class SavingsAccount(BankAccount):
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         if self.balance - amount >= 0:
#             self.balance -= amount
#
#
# class CheckingAccount(BankAccount):
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         if self.balance - amount >= 0:
#             self.balance -= amount

# s = input("Enter string: ")
# data = {"[": "]", "{": "}", "(": ")"}
# length = len(s)
# if length % 2 == 0 or length % 2 == 0 or length % 6 == 0:
#     if s.count("[") == s.count(data["["]) and s.count("{") == s.count(data["{"]) and s.count("(") == s.count(data["("]):
#         print(True)
# else:
#     print(False)


# 17.10#

# def float_range(start, end, step):
#     current = start
#     while current < end:
#         yield current
#         current += step
#
#
# start = float(input("Enter num in float for start: "))
# end = float(input("Enter num for end of the range in float: "))
# step = float(input("Enter num in float for step value: "))
#
# for value in float_range(start, end, step):
#     print(value)
