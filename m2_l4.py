# class Wealth:
#     def __init__(self, income):
#         self.income = income
#
#
# class MarketingAgent(Wealth):
#     def __init__(self, company, experience, age, volume, income):
#         self.company = company
#         self.experience = experience
#         self.age = age
#         self.volume = volume
#         super().__init__(income)
#         # self.income = income
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
# # agent = MarketingAgent("Norman Industries", "6", 28, 300000000, 7000)
# # recruiter = CompanyRecruiter(7, 1000)
# # student = Student("Economics", "Math, English, Physics", "10C", 1, 500)
# # print(agent.income + recruiter.income + student.income)
#
# class Group:
#     def __init__(self, student_amount, faculty, start):
#         self.faculty = faculty
#         self.student_amount = student_amount
#         self.start = start
#


"""Homework"""

"""Work1"""
# class Student:
#     def __init__(self, name, group, start_time):
#         self.name = name
#         self.group = group
#         self.start_time = start_time
#         self.finish_time = None
#
#
# students = [
#     Student("Asadbek", "101-1", "2023-01-15"),
#     Student("Jasur", "101-1", "2023-01-20"),
#     Student("Abdullo", "101-1", "2023-01-25"),
#
#     Student("Ismoil", "102-2", "2023-02-01"),
#     Student("Sevara", "102-2", "2023-02-05"),
#     Student("Sevinch", "102-2", "2023-02-10"),
#
#     Student("Aziza", "101-3", "2023-03-01"),
#     Student("Umar", "101-3", "2023-03-05"),
#     Student("Javohir", "101-3", "2023-03-10"),
#
#     Student("Nodir", "100-4", "2023-04-01"),
#     Student("Shaxlo", "100-4", "2023-04-05"),
#     Student("Madina", "100-4", "2023-04-10"),
#
#     Student("Sardor", "103-1", "2023-05-01"),
#     Student("Ibrohim", "103-1", "2023-05-05"),
#     Student("Abduqodir", "103-1", "2023-05-10"),
# ]
#
# from datetime import datetime
#
#
# def calc(start_time, finish_time):
#     start = datetime.strptime(start_time, "%Y-%m-%d")
#     finish = datetime.strptime(finish_time, "%Y-%m-%d")
#     duration = finish - start
#     return duration.days
#
#
# for student in students:
#     finish_date = datetime.strptime(student.start_time, "%Y-%m-%d")
#     student.finish_time = finish_date.strftime("%Y-%m-%d")
#     course_duration = calc(student.start_time, student.finish_time)
#     print(f"{student.name} ({student.group}): {course_duration} days")


"""Work2"""

# Superclass 1
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#
# # Subclass 1.1
# class Mammal(Animal):
#     def speak(self):
#         return "Mammal sound"
#
#
# # Subclass 1.2
# class Bird(Animal):
#     def fly(self):
#         return "Flying high"
#
#
# # Superclass 2
# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand
#
#
# # Subclass 2.1
# class Car(Vehicle):
#     def drive(self):
#         return "Vroom! Driving the car"
#
#
# # Subclass 2.2
# class Bicycle(Vehicle):
#     def pedal(self):
#         return "Pedaling the bicycle"
#
#
# # Superclass 3
# class Shape:
#     def __init__(self, color):
#         self.color = color
#
#
# # Subclass 3.1
# class Circle(Shape):
#     def calculate_area(self, radius):
#         return 3.14 * radius ** 2
#
#
# # Subclass 3.2
# class Square(Shape):
#     def calculate_area(self, side_length):
#         return side_length ** 2
#
#
# # Superclass 4
# class Employee:
#     def __init__(self, name, employee_id):
#         self.name = name
#         self.employee_id = employee_id
#
#
# # Subclass 4.1
# class Manager(Employee):
#     def manage_team(self):
#         return "Managing the team"
#
#
# # Subclass 4.2
# class Developer(Employee):
#     def code(self):
#         return "Writing code"
#
#
# # Superclass 5
# class Food:
#     def __init__(self, name):
#         self.name = name
#
#
# # Subclass 5.1
# class Fruit(Food):
#     def is_sweet(self):
#         return True
#
#
# # Subclass 5.2
# class Vegetable(Food):
#     def is_green(self):
#         return True
#
#
# # Examples
# mammal_instance = Mammal("Dog")
# print(mammal_instance.name)
# print(mammal_instance.speak())
#
# car_instance = Car("Toyota")
# print(car_instance.brand)
# print(car_instance.drive())
#
# circle_instance = Circle("Red")
# print(circle_instance.color)
# print(circle_instance.calculate_area(5))
#
# manager_instance = Manager("John", "M123")
# print(manager_instance.name)
# print(manager_instance.manage_team())
#
# fruit_instance = Fruit("Apple")
# print(fruit_instance.name)
# print(fruit_instance.is_sweet())
