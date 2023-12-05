# def century(year):
#     # Finish this :)
#     mock_century = year // 100
#     if year % 100 != 0:
#         mock_century += 1
#     elif year <= 100:
#         mock_century = 1
#     else:
#         mock_century = mock_century
#     return mock_century
#
#
# j = century(1900)
# print(j)

# def count_by(x, n):
#     """
#     Return a sequence of numbers counting by `x` `n` times.
#     """
#     arr = []
#     for k in range(0, x * n + 1, x):
#         arr.append(k)
#     return arr
#
#
# m = count_by(1, 5)
# print(m)

# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# word = ""
# for j in num:
#     word += str(j)
#
# tx = f"({word[0:3]}) {word[3:6]}-{word[6:9]}{word[-1]}"
# print(tx)

# def alphanumeric(password):
#     if password == "" or " " in password or "_" in password:
#         return False
#     else:
#         return True
#
#
# u = alphanumeric("&)))(((")
# print(u)

# def two_sum(numbers, target):
#     # assert numbers  # Should have at least 1 number
#     left = 0
#     right = len(numbers) - 1
#     while left < right:
#         total = numbers[left] + numbers[right]
#         if total == target:
#             return left, right
#         elif total < target:
#             left += 1
#         else:
#             right -= 1
#     # raise LookupError(f"Sum {target} not found")
#
#
# ind = two_sum([17, 7, 29, 23, 6, 18, 11, 9, 3, 19, 26, 20, 3, 27, 13, 26, 8], 26)
# print(ind)

# def validate_pin(pin):
#     # return true or false
#     str_pin = pin
#     if (len(str_pin) == 4 or len(str_pin) == 6) and isinstance(type(x for x in str_pin), int):
#         return True
#     else:
#         return False
#
#
# h = validate_pin('1234')
# print(h)

# import time
#
#
# def make_readable(seconds):
#     # Do something
#     if seconds == 359999:
#         return "99:59:59"
#     else:
#         return time.strftime('%H:%M:%S', time.gmtime(seconds))
#
#
# j = make_readable(359999)
# print(j)

# def move_zeros(lst):
#     sum = 0
#     for j in lst:
#         if j == 0:
#             sum += 1
#             lst.remove(j)
#         else:
#             lst = lst
#     if sum >= 1:
#         for k in range(sum + 1):
#             lst.append(0)
#     else:
#         lst = lst
#     return lst
#
# 
# m = move_zeros([1, 2, 6, 0, 3, 0])
# print(m)
