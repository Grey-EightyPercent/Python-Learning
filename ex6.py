#string and text

types_of_people = 10
x = f"there are {types_of_people} types of people."
# x1 = "there are", types_of_people, "types of people." ??? Is there another method that I can insert a var.

binary = "binary"
do_not = "don't"
y = f"those who know {binary} and those who {do_not}."

print(x)
print(x1)
print(y)

print(f"I said : {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format (hilarious))

w = "This is the left side of ..."
e = "a string with a right side."

print(w + e)
