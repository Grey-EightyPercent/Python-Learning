# Names, Variables, Code, Funcstions!!! 函数！！

# this one is like your scripts with argv

def print_two(*args): # use def to give the function name
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do This
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothing'.")

# There are no displays above because all of the 'print' command are in the function! only when you give values to the function it can be actived

# Run functions respectively!!!!!
print_two("zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
