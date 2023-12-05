# my_st = {1, 2, 'sds,as', False, True}
# ya_st = {'q', False, 0, 1, -1}
# my_st.add(True)
# print(my_st)
# print(my_st.intersection(ya_st))
# print(ya_st.intersection(my_st))

# print(my_st.difference(ya_st))
# print(ya_st.difference(my_st))

# g = int(input("Enter amount: "))
# lst = []
# for i in range(g):
#     global o
#     o = int(input(f"Enter num{i + 1}: "))
#     lst.append(o)
# for j in range(g + 1):
#     print(f"There are {lst.count(o)} {o}s in my list")

"""Strip comments"""
# def solution(s, markers):
#     lines = s.split('\n')
#     for i in range(len(lines)):
#         for marker in markers:
#             pos = lines[i].find(marker)
#             if pos != -1:
#                 lines[i] = lines[i][:pos]
#         lines[i] = lines[i].rstrip()
#     return '\n'.join(lines)
#
#
# p = solution(' a #b\nc\nd $e f g', ['#', '$'])
# print(p)

""""""