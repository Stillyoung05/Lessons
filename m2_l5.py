# import random
#
#
# class Wealth:
#     def __init__(self, income):
#         self.income = income
#
#     def how_much(self):
#         return self.income
#
#
# class MarketingAgent(Wealth):
#     from random import randint
#     def __init__(self, company, experience, age, volume, income):
#         self.company = company
#         self.experience = experience
#         self.age = age
#         self.volume = volume
#         super().__init__(income)
#         # self.income = income
#
#     def how_much(self):
#         perks = random.randint(100, 1000)
#         return self.income + perks
#
#
# class CompanyRecruiter(Wealth):
#     def __init__(self, staff_amount, income):
#         self.staff_amount = staff_amount
#         # self.income = income
#         super().__init__(income)
#
#
# class Student(Wealth):
#     def __init__(self, field, subjects, group, course, income):
#         self.field = field
#         self.subjects = subjects
#         self.group = group
#         self.course = course
#         # self.income = income
#         super().__init__(income)
#
#
# agent = MarketingAgent("Norman Industries", "6", 28, 300000000, 7000)
# recruiter = CompanyRecruiter(7, 1000)
# student = Student("Economics", "Math, English, Physics", "10C", 1, 500)
#
#
# # print(agent.income + recruiter.income + student.income)
#
# class Group:
#     def __init__(self, student_amount, faculty, start):
#         self.faculty = faculty
#         self.student_amount = student_amount
#         self.start = start


"""isPrime"""
# from datetime import datetime as dtt
#
#
# def is_prime(number):
#     if number <= 1:
#         return False
#     if number <= 3:
#         return True
#     if number % 2 == 0 or number % 3 == 0:
#         return False
#     i = 5
#     while i * i <= number:
#         if number % i == 0 or number % (i + 2) == 0:
#             print(i)
#             return False
#         i += 6
#     return True
#
#
# begin = dtt.now()
#
# number = int(input("Enter a number: "))
# if is_prime(number):
#     finish = dtt.now()
#     duration = finish - begin
#     print(True, duration)
# else:
#     finish = dtt.now()
#     duration = finish - begin
#     print(False, duration)


# n = int(input("enter num: "))
# n + nn + nnn
# input:
# output:


import random


def choose_word():
    words = ["python", "programming", "challenge", "learning", "coding", "developer", "django", "internet", "algorythm"]
    return random.choice(words)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "*"
    return display


def guess_the_word():
    print("Welcome to Guess the Word Game!")
    secret_word = choose_word()
    guessed_letters = []
    attempts = len(choose_word())

    while attempts > 0:
        print("\nAttempts left:", attempts)
        current_display = display_word(secret_word, guessed_letters)
        print("Current Word:", current_display)

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            print("Incorrect guess!")
            attempts -= 1

        if set(guessed_letters) == set(secret_word):
            print("Congratulations! You guessed the word:", secret_word)
            break

    if attempts == 0:
        print("Sorry, you're out of attempts. The correct word was:", secret_word)


guess_the_word()
