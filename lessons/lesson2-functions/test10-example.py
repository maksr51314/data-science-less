import functools
#
# def myFn(x):
#     return functools.reduce(lambda x, y: x*y, range(1, x + 1))
#
# res = myFn(5)
#
# print(res)


# def myFn2():
#     list = []
#     def sumFun(el) :
#         list.append(el)
#         return functools.reduce(lambda x, y: x+y, list)
#     return sumFun
#
# myRunFn = myFn2()
#
# print(myRunFn(2))
# print(myRunFn(3))
# print(myFn2(3))
# print(myFn2(3,3))
# # print(myFn2(2))

# brakes = {
#     '(': ')',
#     '{': '}'
# }
#
# def check_balanced_string(str):
#   stack = []
#   dicc = {'(': ')', '[': ']', '{': '}'}
#
#   for char in enumerate(str):
#     if char in dicc.keys():  # opening char
#       stack.append(char)
#     elif char in dicc.values():  # closing char
#       if dicc[stack[-1]] == char:  # check if closing char corresponds to last opening char
#
#           check_balanced_string()
#         stack.pop()
#       else:
#         return False
#   return not len(stack)  # returns True when len == 0
#
# eq = '{1+[3*5+(2+1)]}'
# print(check_balanced_string(eq))



#
# def myFn3(string):
#     # print(string)
#     for index, el in enumerate(string):
#         if el in brakes.keys():
#             for indexBack, elBack in enumerate(string[::-1]):
#                 # if elBack in brakes.values():
#                     # print(brakes[el], elBack)
#                 if brakes[el] == elBack:
#                     cuttedString = string[index+1:-indexBack-1]
#                     if '(' in cuttedString or '{' in cuttedString:
#                         myFn3(cuttedString)
#                     else:
#                         return True
#                 elif elBack == el:
#                     return False
#
#     return True

# print(myFn3("m(vasia)a"))

# print(myFn3("2(1{k}1)2"))
#
#     my_list = []
#
#     # def checkBrakets(my_string):
#     #     for el in my_string:
#     #         my_list.append(el)
#     #     return my_list
#     # return checkBrakets
#
# # myRunFn = myFn3()
#
# print(myFn3('(())'))
