# parameters, unpacking, variables

from sys import argv #  sys module from Python standard library. Tell it what you want to use
# read the WYSS section for how to run This
script, A, B, C, D, E = argv  # unpack argv. "Take whatever is in argv, unpack it, and assign it to all of these variables on the left order"

# After importing argv from sys module, unpacking argv into four variables, assigning them on the left in order
print("The script is called:", script)
print("Your first variable is:", A)
print("Your second variable is:", B)
print("Your third variable is:", C)
print("Your forth variable is:", D)
print("Your fifth variable is:", E)

cost = input("Which plan is cheapest?")
time = input("Which plan costs the most time?")
preference = input("Which plan do you like most?")

print(f"So {cost} is the cheapest, {time} is the longest and your favorite one is {preference}")
