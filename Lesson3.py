# while True:
#     num = int(input("Enter the num: "))
#     if num > 0:
#         print("Musbat son")
#     elif num == 0:
#         print("Siz n0l kiritdingiz")
#     else:
#         print("Manfiy son kiritdingiz")

# num = int(input("Enter the num: "))
# for h in range(num + 1):
#     if num == h:
#         global num2
#         num2 = h
# print(f"Siz {num2} kiritdingiz")

# num = int(input("Enter the num: "))
# if num == 1:
#     print("Siz 1 kiritdingiz")
# elif num == 2:
#     print("Siz 2 kiritdingiz")
# elif num == 3:
#     print("Siz 3 kiritdingiz")
# elif num == 4:
#     print("Siz 4 kiritdingiz")
# else:
#     print("Siz 5 kiritdingiz")

# num = int(input("Enter the num: "))
# if num > 0:
#     num += 1
# print(num)

# a = int(input("A sonni kiriting"))
# b = int(input("B sonni kiriting"))
# c = int(input("C sonni kiriting"))
# d = 0
# if a > 0:
#     d += 1
# if b > 0:
#     d += 1
# if c > 0:
#     d += 1
# print(d)

"""if2"""
# int = int(input())
# if int > 0:
#     int += 1
# else:
#     int -= 2
# print(int)

"""if3"""
# int = int(input())
# if int > 0:
#     int += 1
# elif int == 0:
#     int = 10
# else:
#     int -= 2

"""if5"""
# a, b, c = map(int, input().split())
# minuses = 0
# pluses = 0
# if a > 0 and b < 0 and c < 0:
#     pluses += 1
#     minuses += 2
# elif b > 0 and a < 0 and c < 0:
#     pluses += 1
#     minuses += 2
# elif c > 0 and b < 0 and a < 0:
#     pluses += 1
#     minuses += 2
# elif a > 0 and b > 0 and c < 0:
#     pluses += 2
#     minuses += 1
# elif a > 0 and c > 0 and b < 0:
#     minuses += 1
#     pluses += 2
# elif b > 0 and c > 0 and a < 0:
#     minuses += 1
#     pluses += 2
# elif a > 0 and b > 0 and c > 0:
#     pluses += 3
# elif a < 0 and b < 0 and c < 0:
#     minuses += 3
# else:
#     print("Wrong nums")
# print(minuses, pluses)

"""if6"""
# a, b = map(int, input().split())
# if a > b:
#     print(a)
# else:
#     print(b)

"""if7"""
# a, b = map(int, input().split())
# if a < b:
#     print(1)
# else:
#     print(2)

"""if8"""
# a, b = map(int, input().split())
# if a > b:
#     print(a, b)
# else:
#     print(b, a)

"""if9"""
# a, b =map(int, input().split())
# if a > b:
#     a = a-b
# elif b > a:
#     a = a
# elif a == b:
#     a -= 1
# else:
#     print("Wrong num")

"""if10"""
# a, b = map(int, input().split())
# if a != b:
#     a, b = a + b
# else:
#     a, b = 0
# print(a, b)

"""if11"""
# a, b = map(int, input().split())
# if a != b:
#     a, b = max(a, b)
# else:
#     a, b = 0
# print(a, b)

"""if12"""
# a, b, c = map(int, input().split())
# print(min(a, b, c))

"""if13"""
# a, b, c = map(int, input().split())
# nums = [a, b, c]
# max = max(a, b, c)
# min = min(a, b, c)
# nums.remove(max)
# nums.remove(min)
# print(nums[0])

"""if14"""
# a, b, c = map(int, input().split())
# print(min(a, b, c), max(a, b, c))

"""if15"""
# a, b, c = map(int, input().split())
# nums = [a, b, c]
# nums.remove(max(a, b, c))
# print(max(a, b, c), max(nums))

"""if16"""
# a, b, c = map(int, input().split())
# if a > b > c:
#     a *= 2
#     b *= 2
#     c *= 2
# else:
#     a *= -1
#     b *= -1
#     c *= -1
# print(a, b, c)

"""if17"""
# a, b, c = map(int, input().split())
# if a > b > c or c > b > c:
#     a *= 2
#     b *= 2
#     c *= 2
# else:
#     a *= -1
#     b *= -1
#     c *= -1
# print(a, b, c)

"""if18"""
# a, b, c = map(int, input().split())
# # nums = [a, b, c]
# # index = 0
# if a == b:
#     print(3)
# elif a == c:
#     print(2)
# elif b == c:
#     print(1)
# else:
#     print('Bir biriga teng 2 ta son mavjud emas')
# print(index)

"""if19"""
# a, b, c, d = map(int, input().split())
# if a == b == c:
#     print(4)
# elif a == b == d:
#     print(3)
# elif a == c == d:
#     print(2)
# elif b == c == d:
#     print(1)
# else:
#     print('Teng sonlar yetishmayapti')

"""if20"""
# a, b, c = map(int, input().split())
# distance1 = abs(a - c)
# distance2 = abs(a - b)
# if distance2 > distance1:
#     print(c, distance1)
# elif distance1 > distance2:
#     print(b, distance2)
# else:
#     print('None')

"""if21"""
# a, b = map(int, input().split())
# if a == 0 and b == 0:
#     print(0)
# elif a == 0:
#     print(1)
# elif b == 0:
#     print(2)
# else:
#     print(3)

"""if22"""
# a, b = map(int, input().split())
# if a > 0 and b > 0:
#     print(1)
# elif a > 0 and b < 0:
#     print(4)
# elif a < 0 and b < 0:
#     print(3)
# elif a < 0 and b > 0:
#     print(2)
# else:
#     print('Nuqta koordinata boshida yoki koordinata tog\'ri chiziqlari bn kesishgan')

"""if23"""
# a, b = map(int, input().split())
# c, d = map(int, input().split())
# e, f = map(int, input().split())
# print(e, b)

"""if28"""
# years = int(input())
# days = years * 365
# if years % 100 == 0:
#     days += years // 400
# else:
#     days += years // 4
# print(days)

"""if29"""
# v = int(input())
# if v > 0 and v % 2 == 0:
#     print('Musbat juft son')
# elif v == 0:
#     print('Son 0 ga teng')
# elif v > 0 and v % 2 != 0:
#     print('Musbat juft son')
# elif v < 0 and abs(v) % 2 == 0:
#     print('Manfiy juft son')
# elif v < 0 and abs(v) % 2 != 0:
#     print('Manfiy toq son')
# else:
#     print('')

"""if30"""
# g = int(input())
# if g % 100 > 1:
#     if g % 2 == 0:
#         print('3 xonali juft son')
#     else:
#         print('3 xonali toq son')
# elif (g - g // 100) % 10 > 1:
#     if g % 2 == 0:
#         print('2 xonali juft son')
#     else:
#         print('2 xonali toq son')
# elif g % 2 == 0:
#     print('1 xonali fuft son')
# else:
#     print('1 xonali toq son')
