import sys
import copy

text = r"c:/asdasd\asdasdasd\asd"

my_text = """Mask 
asdasdsad"""

my_bytes_text = b'kqkkkk'

el_at_string = 'maksssssa'[1:-1:2]

array = 3

myId = id(array)

a = 5
b = 6
# a = 1 if b == 6 else a = 5

my_custom_array = [1, 2, 2, 3, 4, 'asdasdsad']

my_custom_array2 = my_custom_array

my_custom_array3 = copy.deepcopy(my_custom_array2)

print(id(my_custom_array), id(my_custom_array2), id(my_custom_array3))

print(1 in my_custom_array)

if a < b:
    print(my_custom_array is not my_custom_array2)


my_dictionary = {'12312': 'max', '123123': 'vasia'}

# for key, value in my_dictionary:
#     print(key, value)

# my_set = {1, 2, 3, 2}


def max(a, b):
    return


print(max(2,3))
