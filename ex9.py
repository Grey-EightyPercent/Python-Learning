# Here is some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
months2 = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# Below are 3 ways to insert or display a defined variable to users.
print("1 Here are the days: ", days)
print(f"2 Here are the days:  {days}")
print("3 Here are the days:  {}".format(days))

print(f"Here are the months: ", months)
print(f"Here are the months: ", months2)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
