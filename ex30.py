people = 40
cars = 40
trucks = 50


if cars > people : #if cars greater than people, if true then print below.
    print("We should take the cars.")
elif cars < people : #if cars not grearer than people, then run the next elif --- if cars < people ,if true then print below.
    print("We should not take the cars.")
else: # if cars not greater and less than people, then run the else command below.
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we should take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
