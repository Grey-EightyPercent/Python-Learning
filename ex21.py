#2019/10/25

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a - b # what is this?

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5) # 35
height = subtract(78, 4) #74  spelling wrong
weight = multiply(90, 2) #180
iq = divide(250, 2) #125
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for extra credit. Type it in anyway.
print("Here is a puzzle")
# Description； what = (height - ((iq / 2) * weight)) + age = (74-((250/2)*180))+35 =
what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print("That becomes: ", what, "Can you do it by hand?")
