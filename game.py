name = str(input("Hello, What is your name? "))
print("")
inv = list()
doorOpen = False
while doorOpen == False:
    print("Hello",name,"you are standing in a small room. There are only two things in the room large metal door and a small wooden desk")
    print("")
    choice1=str(input("Would you like to go towards the door or the desk? (desk/door) "))
    print("")
    if choice1 == "Door" or choice1 == "door":
        print("You walk towards the door")
        choice2 = str(input("The door is closed would you like to try and open it? or go back? (yes/back) "))
        print("")
        if choguessice2 == "yes":
            print("You try the door handle")
            print("")
            for x in inv:
                if x == "key":
                    print("The door opened")
                    print("")
                else:
                    print("The door is locked, you need to find a way to open it and so you move back towards the middle of the room")
                    print("")
                
    elif choice1 == "Desk" or choice1 == "desk":
        print("You walk towards the desk")
        print("")
        print("The desk is small and made of hard wood, it has one drawer that is closed and bears a strange symbol")
        print("")
        choice3 = str(input("Would you like to open the drawer? (yes/no) "))
        print("")
        print("Upon closer inspection you find that the strange symbol is actually made up of some dials that can be turned")
        print("")
        print("you spin the dials and they contain numbers from 1-9, 'too many combinations to guess' you think to yourself")
        print("")
        puzzle1 = str(input("Try to guess the combination or look for clues? (guess/clues)"))
        if puzzle1 == "guess":
            print("You spend all your time and energy guessing combinations and sucumb to lack of water, unlucky!")
        elif puzzle1 == "clues":
            print("You search around the desk and on one side is carved some numbers")
            print("00000001")
            print("00000010")
            print("00000100")
            print("What could it mean?")
            print("a little further round the desk you find a torn piece of paper it once said much more however all that remains is")
            print("bina")
            puzzle1a = int(input("You have your clues and the combination lock in front of you, you need to try some numbers: "))
            combi = 124
            drOpen = False
            while drOpen == False:
                if puzzle1a == combi:
                    print("Well done! it was binary for 124.  The drawer clicks open and inside is a key")
                    drOpen = True
                else:
                    print("No try again")

            if choice3 == "yes":
                inv.append("key")
                print("You have added a key to your inventory")
                print("")
                print("Items in inventory:",inv)
                print("")
                print("You are standing in front of a desk, the drawer is fully open and empty")
                print("")
                print("There is a door on the other side of the room")
                print("")
                choice4 = str(input("Would you like to walk towards the door? (yes/no) "))
                print("")
                if choice4 == "yes":
                    print("You are standing infront of the door, your curiosity gets the better of you and you reach out and try the handle \n the door is locked")
                    print("")
                    print("You remember that you have a key in your pocket")
                    print("")
                    choice5 = str(input("Would you like to try and open the door with the key? (yes/no)"))
                    print("")
                    if choice5 == "yes":
                        for x in inv:
                            if x == "key":
                                print("You take the key from your inventory and try it in the lock, the door clicks open")
                                print("")
                                inv.remove("key")
                                print("items in inventory:",inv)
                                doorOpen = True
                            




    else:
        print("You have not chosen door or desk")


print("You are outside, you turn around to see where you have just exited from and you are greeted with a small building")
print("")
print("it as no windows and you see the door you have just opened to leave it, above the door a sign reads 'Quarantine'")
print("")
print("the words echo through your head as you try to come to terms with the word, 'why was i in there?'")
print("")
print("you catch yourself saying it outloud and then look around and remind yourself that you are alone.")
print("")
print("you turn away from the building to assess the situation infront of you.")
print("")
print("You are in a forest, it is quite dense with trees but through a crack in the canopy you see some buildings")
print("")
print("you decide the best course of action is to head towards this potential civilization")
print("")
print("")

