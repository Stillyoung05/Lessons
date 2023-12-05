# class Person:
#     def __init__(self, name, date_of_birth, passport_id):
#         self.name = name
#         self.__date_of_birth = date_of_birth
#         self.passport_id = passport_id
#
#
# p1 = Person("Paul", "01-03-2000", "AC1234567")
# p2 = Person("Carol", "01-10-2002", "AC1234567")
#

# class Phone:
#     def __init__(self, time, duration):
#         self.__time = time
#         self.__duration = duration
#
#     @property
#     def took(self):
#         return self.__time
#
#     def how_much(self):
#         return self.__duration
#
#
# obj = Phone("15-05-2022", "1564 hrs")
# print(obj.took)

"""Homework"""

"""Task1"""


# def roman_to_arabic(roman):
#     roman = roman.upper()  # Convert to uppercase to handle lowercase input
#     roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     arabic_numeral = 0
#     prev_value = 0
#
#     for numeral in reversed(roman):
#         value = roman_numerals[numeral]
#
#         if value < prev_value:
#             arabic_numeral -= value
#         else:
#             arabic_numeral += value
#
#         prev_value = value
#
#     return arabic_numeral
#

# roman_numeral = "vi"
# arabic_numeral = roman_to_arabic(roman_numeral)
# print(f'The Arabic numeral for {roman_numeral} is: {arabic_numeral}')

"""Task2"""

# class Class1:
#     def __init__(self):
#         self.__private_attr1 = 1
#         self.__private_attr2 = 2
#         self._protected_attr = 4
#
#     @property
#     def get_private_attr1(self):
#         return self.__private_attr1
#
#     @property
#     def get_private_attr2(self):
#         return self.__private_attr2
#
#
# class Class2:
#     def __init__(self):
#         self.__private_attr1 = 36
#         self.__private_attr2 = 4
#         self._protected_attr = 74
#
#     @property
#     def get_private_attr1(self):
#         return self.__private_attr1
#
#     @property
#     def get_private_attr2(self):
#         return self.__private_attr2
#
#
# class Class3:
#     def __init__(self):
#         self.__private_attr1 = 789
#         self.__private_attr2 = 4
#         self._protected_attr = 963
#
#     @property
#     def get_private_attr1(self):
#         return self.__private_attr1
#
#     @property
#     def get_private_attr2(self):
#         return self.__private_attr2
#
#
# class Class4:
#     def __init__(self):
#         self.__private_attr1 = 41
#         self.__private_attr2 = 4589
#         self._protected_attr = "qwerty"
#
#     @property
#     def get_private_attr1(self):
#         return self.__private_attr1
#
#     @property
#     def get_private_attr2(self):
#         return self.__private_attr2
#
#
# class Class5:
#     def __init__(self):
#         self.__private_attr1 = 63
#         self.__private_attr2 = False
#         self._protected_attr = False
#
#     @property
#     def get_private_attr1(self):
#         return self.__private_attr1
#
#     @property
#     def get_private_attr2(self):
#         return self.__private_attr2
#
#
# class Class6:
#     def __init__(self):
#         self.__private_attr1 = 78963
#         self.__private_attr2 = True
#         self._protected_attr = None
#
#     @property
#     def get_private_attr1(self):
#         return self.__private_attr1
#
#     @property
#     def get_private_attr2(self):
#         return self.__private_attr2
#
#
# class Class7:
#     def __init__(self):
#         self.__private_attr1 = "A"
#         self.__private_attr2 = "[]"
#         self._protected_attr = {}
#
#     @property
#     def get_private_attr1(self):
#         return self.__private_attr1
#
#     @property
#     def get_private_attr2(self):
#         return self.__private_attr2
#
#
# class Class8:
#     def __init__(self):
#         self.__private_attr1 = None
#         self.__private_attr2 = 12
#         self._protected_attr = 4
#
#     @property
#     def get_private_attr1(self):
#         return self.__private_attr1
#
#     @property
#     def get_private_attr2(self):
#         return self.__private_attr2
#
#
# class Class9:
#     def __init__(self):
#         self.__private_attr1 = ()
#         self.__private_attr2 = range(12, 234, 4)
#         self._protected_attr = None
#
#     @property
#     def get_private_attr1(self):
#         return self.__private_attr1
#
#     @property
#     def get_private_attr2(self):
#         return self.__private_attr2
#
#
# class Class10:
#     def __init__(self):
#         self.__private_attr1 = "Python"
#         self.__private_attr2 = 0
#         self._protected_attr = "THE LAST METHOD😁"
#
#     @property
#     def get_private_attr1(self):
#         return self.__private_attr1
#
#     @property
#     def get_private_attr2(self):
#         return self.__private_attr2
