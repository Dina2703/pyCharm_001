# #
# # from math import *
# # # 'math' - module, where we get functions
# # # strings
# # phrase = 'Hello World'
# # print(phrase.lower())
# # print(phrase.upper())
# # print(phrase.isupper())
# # print(phrase.upper().isupper())
# # print(len(phrase))
# # print(phrase[-1])
# # print(phrase.lower().index("w"))
# # print(phrase.replace("World", "Ann"))
# #
# # # numbers
# # my_num = 27
# # print(str(my_num) + " my fav number")
# # print(floor(3.2))
# # print(ceil(3.2))
# # print(sqrt(144))
# #
# # # input
# # # name = input("What is your name?")
# # # age = input("How old are you?")
# # # print("Hello " + name, " " + age)
# #
# # # calculator
# # # num1 = input("enter a number")
# # # num2 = input("enter another number")
# # # result = float(num1) + float(num2)
# # # print(result)
# #
# # # game
# # # color = input("your color: ")
# # # plural_noun = input("your plural noun: ")
# # # celeb = input("your fav celebrity: ")
# # # print(f"Roses are {color}")
# # # print(f"{plural_noun} are blue")
# # # print(f"I love {celeb}")
# #
# # # lists
# # numbers = [1, 2, 3, 45,2,  56, 2]
# # colors = ["red", "blue", "grey", "green"]
# #
# # # print(colors[1:-1])
# # # print(len(colors))
# # colors.extend(numbers)
# # # add an item to the end of  the list
# # colors.append("white")
# # # add to the specific place/position into the list
# # colors.insert(2, "yellow")
# # # remove an item
# # colors.remove("red")
# # # remove all the elements
# # # colors.clear()
# # # remove the last element off the list
# # colors.pop()
# # # check and get the index of an element
# # print(colors.index('grey'))
# # print(colors.count(2))
# # numbers.sort()
# # numbers.reverse()
# # print(numbers)
# # colors2 = colors.copy()
# # print(colors2)
# # print(colors)
#
# # TUPLES, immutable, can not be changes or modified, can not add an item after you initially have defined/created it.
# # And use () curly brackets instead of square as in list.
# # coordinates = (1, 2)
# # print(coordinates[0])
#
# # Functions
# def say_hi(name, age):
#     print(f"Hi {name}, you are {age}")
#
#
# say_hi('Mike', 35)
#
#
# # return statement
# def cube(num):
#     return num * num * num
#
#
# result = cube(4)
# print(result)
#
# # IF statements
# # is_adult = False
# # is_female = True
# #
# # if is_adult or is_female:
# #     print('You are an adult or a female')
# # elif is_adult and is_female:
# #     print('You are a women')
# # elif is_adult and not is_female:
# #     print('You are a men')
# # elif not is_adult and is_female:
# #     print('You are a girl')
# # else:
# #     print("You are a kid")
# #
# #
# # # If statements and comparisons
# #
# # def max_num(num1, num2, num3):
# #     if num1 >= num2 and num1 >= num3:
# #         return num1
# #     elif num2 >= num1 and num2 >= num3:
# #         return num2
# #     else:
# #         return num3
# #
# #
# # print(max_num(12, 15, 10))
#
#
# # Calculator exercise
# # first_number = float(input("Enter first number: "))
# # second_number = float(input("Enter second number: "))
# # operator = input("Enter the operator: ")
#
#
# # if operator == '+':
# #     print(first_number + second_number)
# # elif operator == '-':
# #     print(first_number - second_number)
# # elif operator == '/':
# #     print(first_number / second_number)
# # elif operator == '*':
# #     print(first_number * second_number)
# # else:
# #     print('Invalid operator')
#
# # Dictionary. the keys might be a number and strings, but it must be unique
#
# month_conversions = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December",
# }
# # 2 ways to access the values, first is by []
# print(month_conversions["Jan"])
# # second is get() method that allows us to set a default value
# print(month_conversions.get('Asd', 'Not a valid key'))
#
# # While Loop
#
# # i = 1
# # while i <= 10:
# #     print(i)
# #     i += 1
# #
# # print('Done with looping')
#
# # guess game
#
# # secret_word = "thanks"
# # guess = ''
# # guess_count = 0
# # guess_limit = 3
# # out_of_guesses = False
# #
# #
# # while guess != secret_word and not out_of_guesses:
# #     if guess_count < guess_limit:
# #         guess = input('Your guess: ')
# #         guess_count += 1
# #     else:
# #         out_of_guesses = True
# #
# # if out_of_guesses:
# #     print('Out of Guesses, You Lost!')
# # else:
# #     print('You got it right!')
# #
#
# # For Loop
#
#
# for letter in "Hello World":
#     print(letter)
#
# # OR
#
# my_list = [1, 2, 3, 4, 5]
#
# total = 0
#
# for number in my_list:
#     total += number
# print(total)
#
# for index in range(5, 10):
#     print(index)
#
# colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink"]
#
# for index in range(len(colors)):
#     print(colors[index])
#
#
# # practice
# def raise_to_power(base_number, pow_number):
#     result_pow = 1
#     for i in range(pow_number):
#         result_pow = result_pow * base_number
#     return result_pow
#
#
# print(raise_to_power(2, 4))

# number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# print(number_grid[1][0])
# # use nested for loop
#
# for row in number_grid:
#     for index in row:
#         print(index)
#

# practice translator

# def translator(word, magic_letter):
#     translation = ''
#     for letter in word:
#         if letter.lower() in 'aeiou':
#             if letter.isupper():
#                 translation = translation + magic_letter.upper()
#             else:
#                 translation = translation + magic_letter.lower()
#         else:
#             translation = translation + letter
#     return translation
#
#
# print(translator('hello', 'ee'))
# # with input from a user
# print(translator(input('Enter a phrase: '), input('Enter a magic_letter: ')))

# Try / Expect
#
# try:
#     # value = 10/0
#     number = int(input('Enter your number: '))
#     print(number + 2)
# # except ZeroDivisionError:
# #     print('Division by Zero')
# except ValueError:
#     print('Invalid number')


# READing Files, r- read, w-write(over-write to an existing file), a- append(only add), r+  - to read and write

random_data = open('test1.txt', 'w')
# print(random_data.readable())
# print(random_data.readline())
# print(random_data.readline())
#
# print(random_data.readlines()[3])

# for name in random_data.readlines():
#     print(name)

print(random_data.write('\nTest'))


random_data.close()

# Classes and Objects
from Student import Student

student1 = Student('Sam', 23, 4.2, 'student')
print(student1.name)