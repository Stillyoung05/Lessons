#!_to'liq
# a = []
# for i in range(0,4):
#     num = int(input("son kiriting "))
#     a.append(num)
# def func(a):
#     a.sort()
#     return a[2]
# print(func(a))


# 2_algoritm
# d=0
# a=[]
# element = int(input("list nechta element saqlasin "))
# for i in range(0,element):
#     b=input("son kiriting ")
#     a.append(b)
# for num in a:
#     d+=int(num)
# print(d)    


# 2_funksiya - UnboundLocalError: cannot access local variable 'd' where it is not associated with a value
# d=0
# a=[]
# element = int(input("list nechta element saqlasin "))
# for i in range(0,element):
#     b=input("element kiriting ")
#     a.append(b)
# def sum(a):
#     for num in a:
#         d+=int(num)
#     return(d)   
# print(sum(a))


# 3_funksiya_to'liq
# a=[]
# element = int(input("list nechta element saqlasin "))
# for i in range(0,element):
#     b=input("element kiriting ")
#     a.append(b)
# def title(a):
#     res = [i.title() for i in a]
#     return res
# print(title(a)) 


# #4_algoritm
# d=0
# a=[]
# element = int(input("list nechta element saqlasin "))
# for i in range(0,element):
#     b=input("element kiriting ")
#     if b==int:
#         d+=1
#     a.append(b)

# print(d)


# 4
# a = []
# global d
# element = int(input("list nechta element saqlasin: "))
# for i in range(0, element):
#     b = input("element kiriting ")
#     a.append(b)
#
#
# def check(a):
#     for item in a:
#         if item == int:
#             d = 0
#             d += 1
#     return d
#
#
# print(check(a))


# def counter():
#     k = int(input("Enter list length: "))
#     lst = [x for x in input("Enter list items: ").split()]
#     ans = 0
#     if len(lst) == k:
#         for j in lst:
#             if int(j) == j:
#                 ans += 1
#             else:
#                 ans = ans
#     else:
#         return "Wrong list length"
#     return ans
#
#
# print(counter())
