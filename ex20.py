# Functions and files

from sys import argv

script, input_file = argv

# Define functions for using later
# Define function print_all(f) to print what it read from {f}
def print_all(f):
    print(f.read())
# rewind the file from where they have been read.
def rewind(f): # rewind 倒回
    f.seek(0)
# print a line from line 1 , and the curse is at the end line 1 , ready to read line 2
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Open the file given by the users.
current_file = open (input_file)

# Giving values to the functions and using the functions.
print("First let's print the whole file:\n")
# Just read the given file by using function 'print_all', and give this function the variable 'current_file'
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
# Just rewind the given file to the '0' by using function 'rewind', giving this function the variable 'current_file' read by the last function.
rewind(current_file)

print("Let's print three lines:")

# Increase the value of current_line step-by-step.
current_line = 1
# Using function print_a_line to read each line from the line 1 and counting the line numbers by giving it variables：current_line and current_file
# read and print line 1
print_a_line(current_line, current_file)

current_line += 1
# read and print line 2
print_a_line(current_line, current_file)

current_line += 1
# read and print line 3
print_a_line(current_line, current_file)
current_line += 1
# read and print line 4
print_a_line(current_line, current_file)
# rewind from line 5
rewind(current_file)
# read and print line 1
print_a_line(current_line, current_file)
