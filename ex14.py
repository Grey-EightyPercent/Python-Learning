# promting and passing

from sys import argv  #!!! Wrong spelling!!!

script, user_name, title, role=argv
prompt1 = "Yes or No:\t"
prompt2 = "City:\t"
prompt3 = "Mode Number:\t"


print(f"Hi {title}.{user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {title}.{user_name}?")
likes = input(prompt1)

print(f"Where do you live {title}.{user_name}?")
lives = input(prompt2)

print("What kind of computer do you have？")
computer = input(prompt3)
print(f"Is your computer could meet your requirement for being a {role}?")
satisfication = input(prompt1)

print(f"""
Alright, you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer}. Nice. You said {satisfication} about using this computer.
Goodbye {title}.{user_name}!
""")
