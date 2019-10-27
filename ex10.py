# There are currently two ways to make a string that goes across multiple lines
# One is to use \n
# Another one is to sue """ """ triple-quotes

#escape sequences using   ---> \ (backslash)

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
\r* Fishies
\a* Fishies
\t\b* Fishies
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\n\tSep\n\tOct\n\tNov\n\tDec"

print(f"Here are the days: \\{days}\\")
print("Here are the months: {}".format(months))
