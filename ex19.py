# 函数和变量
# define the name of the function, how many and what arguments it needs
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# Below is the content of this function, once it be run, it will run below one by one.
    print(f"You have {cheese_count} cheeses")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Hi Man, that's enough for a party!")
    print("Get a blanket.\n")

# print string
print("We can just give the function numbers directly:")
# giving values to the arguments within the function by typing directly.
cheese_and_crackers(20, 30)  # give arguments to the functoin, and run it
print("OR, we can use variables from our script:")
# define variables
amount_of_cheese = 10 # define variables
amount_of_crackers = 50
# giving values to the arguments within the function by using a variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)# give value via variables and run

print("We can even do math inside too:")
# give the values directly with mathematical computataion.
cheese_and_crackers(10 + 20, 5 + 6)

# give the values using the combination of variables and mathematical computation.
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers +1000)

# give the values using input ()

print("Finally, we can let users to tell us how many things do they have:")
users_cheese = input ("type amount of cheese")
users_crackers = input ("type amount of crackers")

cheese_and_crackers(users_cheese, users_crackers)

print("Eventually, may be we can count it in a easier way like that:")
cheese_and_crackers(int(input ("How many cheese do you have? ")) + 1, int(input("How many crackers do you have? ")) + 1)
