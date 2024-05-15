
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
color = input("your color: ")
plural_noun = input("your plural noun: ")
celeb = input("your fav celebrity: ")
print(f"Roses are {color}")
print(f"{plural_noun} are blue")
print(f"I love {celeb}")

