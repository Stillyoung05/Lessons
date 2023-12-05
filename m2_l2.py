f1 = open('data1.txt', 'r')

# odd_sum = 0
# for j in f1:
#     if int(j) % 2 == 0:
#         odd_sum += int(j)
#         # print(j, end='')
#     else:
#         odd_sum = odd_sum
# print(odd_sum)


# def iseven(n):
#     iseven = True
#     for i in range(1, n + 1):
#         if iseven == True:
#             iseven = False
#         else:
#             iseven = True
#
#     return iseven
# d = iseven(13)
# print(d)

first_file_name = "data1.txt"  # 1st file
second_file_name = "data2.txt"  # 2nd file name
source = open(first_file_name, 'r')
destination = open(second_file_name, 'w')
for h in source:
    destination.write(str(h))
