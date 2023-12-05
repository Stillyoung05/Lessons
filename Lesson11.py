# def two_sum(a, b):
#     try:
#         a = int(input("Enter integer a: "))
#         b = int(input("Entern integer b: "))
#         return a + b
#     except ValueError:
#         return "Enter available number!!!"
#     except TypeError:
#         return "Enter available number!!!"

# def num_max(a, b, c, *others):
#     nums = [a, b, c]
#     return max(nums)

# def my_function(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
#
#
# my_function(a=1, b=2, c=3)
# print(my_function())


# def count_vowels(input_str):
#     in_str = input_str.lower()
#     vowels_str = set("aeiou")
#     vowels = 0
#     for char in in_str:
#         if char in vowels_str:
#             vowels += 1
#     return vowels
#
#
# input_str = input("Enter a string: ")
#
# result = count_vowels(input_str)
# print("")
# print("")
# print("Number of vowels in the string:", result)

g = int(input("Enter the amount: "))
for i in range(1, g + 1):
    num1 = f"*{i}"
    ans = f"{i}{num1 * (i - 1)}={i ** i}"
    print(ans)

