
from math import *
# 'math' - module, where we get functions
# strings
phrase = 'Hello World'
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[-1])
print(phrase.lower().index("w"))
print(phrase.replace("World", "Ann"))

# numbers
my_num = 27
print(str(my_num) + " my fav number")
print(floor(3.2))
print(ceil(3.2))
print(sqrt(144))

# input
# name = input("What is your name?")
# age = input("How old are you?")
# print("Hello " + name, " " + age)

# calculator
# num1 = input("enter a number")
# num2 = input("enter another number")
# result = float(num1) + float(num2)
# print(result)

# game
# color = input("your color: ")
# plural_noun = input("your plural noun: ")
# celeb = input("your fav celebrity: ")
# print(f"Roses are {color}")
# print(f"{plural_noun} are blue")
# print(f"I love {celeb}")

# lists
numbers = [1, 2, 3, 45,2,  56, 2]
colors = ["red", "blue", "grey", "green"]

# print(colors[1:-1])
# print(len(colors))
colors.extend(numbers)
# add an item to the end of  the list
colors.append("white")
# add to the specific place/position into the list
colors.insert(2, "yellow")
# remove an item
colors.remove("red")
# remove all the elements
# colors.clear()
# remove the last element off the list
colors.pop()
# check and get the index of an element
print(colors.index('grey'))
print(colors.count(2))
numbers.sort()
numbers.reverse()
print(numbers)
colors2 = colors.copy()
print(colors2)
print(colors)


