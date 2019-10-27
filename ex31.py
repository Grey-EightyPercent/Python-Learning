print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input(">")

if door == "1":
    print("There is a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cheese.")
    print("2. Scream at the bear.")

    bear = input(">")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

if door == "2":
    print("You stare into the endless abyss at Cthulhu's retuna.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input(">")

    if insanity == "1" or insanity =="2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You find door #3 and a key in the room.")
    print("A. Taking the key and enter the door 3")
    print("B. Sitting forever.")
    enter_door_3 = input("Enter 3 or not?")

    if enter_door_3 == "A":
        print("There are many guards with guns in a room.")
        print("There is a lift that can take you out of the room enclosed by them.")
        print("1. Kill them all.")
        print("2. Negotiating with them and pay for them.")

        method = input(">")
        if method == "1":
            print("Good job! They are too weak to fight with you. Go ahead! Solider!")
        elif method == "2":
            print("You are killed.")
        else:
            print("You are found and killed immediately by them.")
    elif enter_door_3 == "B":
        print("Die in hungry.")
    else:
        print("Die too.")
