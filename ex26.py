print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height= input()
print("How much do you weigh?", end=' ') # lack a parenthesis
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.") # {height} is not defined.

from sys import argv
script, filename = argv # ?

txt = open(filename)

print(f"Here's your file {filename}:") #lack a format, f.
print(txt.read()) # lack a t

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read()) # use wrong symbol. replace _ -> .


print('Let\'s practice everything.')
print('You\'d need to know \'bout escape with \\ that do \n newlines and \t tabs.') #????

poem = """
\tThe lovely world
\twith logic so firmly planted
\tcannot discern \n\tthe needs of love
\tnor comprehend passion from intuition
\tand requires an explanation
\n\t\twhere there is none.
"""

print("--------------") # lack a "
print(poem)
print("--------------")# lack a


five = 10 - 2 + 3 -6 # lack a 6
print(f"This should be five: {five}") # there is no parenthesis

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100 # lack a /
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) # lack a variable /crates/

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula)) #lack a f



people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs: # there is no colon
    print("The world is dry!")


dogs += 5# dog = dog +5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")
