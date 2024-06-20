# 01 Three In, Three Out
# Write a program that will allow a user to enter their name (string), their age (integer) and their favourite TV program (string).
# An example of the input and output from the program is shown below.

"""
INPUT:
Lister
39
Red Dwarf
"""

"""
OUTPUT:
Lister
is
39
years old and likes
Red Dwarf
"""

####### WRITE CODE BELOW #######
name = input("Please enter your name: ")
age = input("What is your age?")
tv_program = input("What is your favourite TV program?")

print(name)
print("is")
print(age)
print("years old and likes")
print(tv_program)