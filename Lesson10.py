# while True:
#     try:
#         h = int(input("Enter num: "))
#         if h > 0:
#             print("Plus")
#         elif h == 0:
#             print(f"{0} \"Zero\"")
#         else:
#             print("Minus")
#     except ValueError:
#         print("Write true enter type!!!")
#     finally:
#         print("It\'s working finally!!!")


# while True:
#     try:
#         nums = [j for j in input("Enter list items: ").split()]
#         for m in nums:
#             if int(m) % 2 == 0:
#                 print(f"First even number is {m}")
#             else:
#                 print("There is not any even number in your list")
#     except TypeError:
#         print("Enter available items!!!")

# for h in range(3):
#     print(h)


# from random import randint
#
# a = randint(1, 100)
#
# for g in range(3):
#     k = int(input("Input your guess: "))
#     if k == a:
#         ans = f"Congrats, you found it, answer is {k}"
#         print(ans)
#         break
# else:
#     ans = "Better luck wishes next time"
#     print(ans)


# try:
#     g = int(input("Enter num: "))
#     num_str = str(g)
#     if num_str == num_str[::-1]:
#         print(True)
#     else:
#         print(False)
# except ValueError:
#     print("Enter true data type!!!")


# n = int(input("Enter num: "))
# original = n
# reverse = 0
# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10
# print(original == reverse)



