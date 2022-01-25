# List Methods

# color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# # print(color_list.index('Red'))


from ctypes import Union
from re import M


print("Welcome to the astroverse!!")
 
# # choice = input("Enter your favourite color:\n>")
# # position = int(input ("Enter the position:\n>"))


# # color_list.append(choice)
# # color_list.insert(position, choice)
# print(color_list)

# data = input("Enter your colours:\n>")

# cleaned_data = data.split()
# color_list.extend(cleaned_data)

# print(color_list)

# li = [0, 2, 9, 8]

# a = li.pop(1)
# print(a)

# li.append(a)
# print(li)

# a = [1, 5, 7, 2]
# a.remove(5)
# b = a
# print(b)

# a = [1, 5, 7, 2]
# c = a.copy()
# print(c)

#### Tuples

# my_tuple = (1,)
# print(type(my_tuple))

# my_tuple = 1,2,3,4,5,6
# print(my_tuple)

# a = {1,2,4,6}
# b = {2,4,1,5}


# ## difference, intertersection, union,  update, symmetric_difference
# c = a.difference(b)
# c = a.symmetric_difference(b)
# b.intersection_update(a)
# print(c)


# english = input("Enter roll numbers for english students:\n>")
# french = input("Enter roll numbers for french students:\n>")

# english_list = english.split()
# french_list = french.split()

# english_set = set(english_list)
# french_set = set(french_list)

# total = english_set.symmetric_difference(french_set)
# print(len(total))

# english = {1,2,3,4,5,6,7,8,9,}
# french = {10,1,2,3,11,21,55,6,8}

# sub = english.symmetric_difference(french)
# print(len(sub))


english = input("Enter roll numbers for english students:\n>")
french = input("Enter roll numbers for french students:\n>")

english_list = english.split()
french_list = french.split()

english_set = set(english_list)
french_set = set(french_list)

total = english_set.union(french_set)
print(len(total))