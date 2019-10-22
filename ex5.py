#print more variable. Learning how to use format string
#learning {}, Exp. f"Hello {somevar}

my_name = "Grey"
my_age = 18 # not a lie
my_height_inch = 74 # inches
my_height = 74 * 10
my_weight_lbs = 180 # lbs
my_weight = round (180 / 10.2)
my_eyes = "Blue"
my_teeth = "white"
my_hair = "Brown"

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Acturally, that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right.
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total} .")
