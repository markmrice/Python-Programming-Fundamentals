import sys
import random


# Call for this when you want to create a new knight
def create_knight(knights):
    """Creates a new knight as a dictionary and stores the new knight 
    on the knights_data list.
    
    Takes user input for the name, armour colour and weapon choice
    as strings which are automatically formatted.

    Also generates random health, damage and luck attributes
    automatically for the knight to be used when duelling. 
    """

    # Creates a new List for the knight
    knights_data = {}
    print("Lets create a knight!")

    # Set the information up for the knight
    try:

        # Set the knights name
        knights_data["name"] = (
            str(input("What is the knights name: "))
            ).capitalize()

        # Set the knights armour colour
        knights_data["colour"] = (
            str(input("What is the colour of the knights armor: "))
        ).capitalize()

        # Set the knights weapon of choice
        knights_data["weapon"] = (
            str(input("What weapon does the knight wield?: "))
        ).lower()

        # Randomly assign the knights health points
        knights_data["hp"] = random.randint(70, 100)

        # Randomly assign the knights baseline damage per hit
        knights_data["damage"] = random.randint(10, 20)

        # Randomly assign the knights luck
        knights_data["luck"] = random.randint(10, 24)

        # Adds the information to the knight
        knights.append(knights_data)
    except:
        print("--- Try Again ---")
        create_knight(knights)


# Call a knight and change their data
def change_data(knights):
    """Change the name, armor colour or weapon choice
    of an existing knight with new user inputs as 
    strings and automatically formats.

    Hp, damage and luck cannot be altered after creation.
    """

    # Print menu of ways to edit knight
    print("--- What would you like to update? ---")
    print("1: Knights Name: " + str(knights["name"]))
    print("2: Colour Of Armor: " + str(knights["colour"]))
    print("3: Knights Weapon: " + str(knights["weapon"]))
    print("4: Exit to menu")

    # Allow a selection to be tested
    try:
        selection = int(input("Select your option: "))

        # Rename the knight
        if selection == 1:
            knights["name"] = str(
                input("What is their new name: ")
                ).capitalize()
            print("Your knight's new name is: " + str(knights["name"]))
            return
        
        # Choose a new armor colour for knight
        elif selection == 2:
            knights["colour"] = str(
                input("What is their new armour colour: ")
                ).capitalize()
            print("Your knight's new armour colour is: " 
                  + str(knights["colour"]))
            return
        
        # Choose a new weapon for knight
        elif selection == 3:
            knights["weapon"] = str(
                input("What is their new weapon: ")
                ).lower()
            print("Your knight's new weapon is: " + str(knights["weapon"]))
            return
        
        # Return to the menu
        elif selection == 4:
           return

        # If no valid choice made
        else:
            print("--- Please select a valid option ---")

    # We are looing for an integer selection
    except:
        print("--- Try Again ---")
        change_data(knights)


# Show the current knights and select one
def select_knight(knights):
    """Used to select knights from those created, to then
    edit their name, armor colour and or weapon choice.

    Knights will be listed in order, select them by inputting
    in the relevant integer when prompted.
    """

    # Reset the list to print all the knights you have
    knights_number = 0
    print("What Knight would you like to update?\n")
    try:

        # Iterate through all knights in our list to print
        while knights_number < int(len(knights)):
            print(
                str(knights_number + 1)
                + "- Knight's name : "
                + str(knights[knights_number]["name"])
            )
            knights_number += 1

            # Choose the knight and pass it into change_data
        selection = int(input("\nSelect the Knights number: ")) - 1
        change_data(knights[selection])
    except:
        print("--- Try Again ---")
        select_knight(knights)


# Select two knights to have a duel with
def select_duelists(knights):
    """Used to select knights from those created, to pit them
    against each other in a duel.

    Knights will be listed in order, select them by inputting
    in the relevant integer when prompted. After the first 
    selection, the first knight picked will be excluded from the
    second selection as they cannot duel themselves.
    """

    # Reset the list to print all the knights you have
    knights_number = 0
    print("What Knight would you like to start a duel?\n")
    try:

        # Iterate through all knights in our list
        # to print and select first duelist
        while knights_number < int(len(knights)):
            print(
                str(knights_number + 1)
                + "- Knight's name : "
                + str(knights[knights_number]["name"])
            )
            knights_number += 1

        # Choose the knight to be the first duelist
        duelist_one = int(input("\nSelect the Knights number: ")) - 1

        # Reset the list to print all the knights you have
        knights_number = 0
        print(
            "What Knight will "
            + str(knights[knights_number]["name"])
            + " challenge to a duel? \n"
        )

        # Iterate through all knights in our list to print
        while knights_number < int(len(knights)):

            # Do not show the first duelist selected
            if knights_number != duelist_one:
                print(
                    str(knights_number + 1)
                    + "- Knight's name : "
                    + str(knights[knights_number]["name"])
                )
            knights_number += 1

        # Choose the knight to be the second duelist
        duelist_two = int(input("\nSelect the Knights number: ")) - 1

        # Start the duel with the selected duelists
        duel(duelist_one, duelist_two, knights)
    except:
        print("--- Try Again ---")
        select_duelists(knights)


# Start a duel between the two selected knights
def duel(knight_one, knight_two, knights):
    """This function serves as the combat loop between the two 
    knights that were selected to duel.

    The first knight that attacks is selected by comparing their
    luck attributes, multiplied by a random int. This gives the lower
    luck knight some chance to get the initiative.

    Then the knights will be temporarily saved to a variable of 
    attacker or defender for the purposes of the combat loop. 
    Their health points (hp) will be saved in a temporary variable 
    so that we are not reducing it on the actual key:value of the 
    knight, so they can fight multiple times.

    The knights take turns attacking, the attack will either be a hit
    or a miss, which again is checked on their luck multiplied by a 
    random integer, which again gives lower luck knights more chance.
    If it is a miss, the attack ends.

    If the attack hits, there is yet another luck check multiplied by
    a random integer, to give low luck knights a chance, which gives 
    the attack a chance to be a critical hit dealing double damage.

    After the attack hits, the defending knight takes damage by 
    reducing the temporary hp variable. After a hit, or a miss, 
    the defending knight is swapped over to be the attacker, and 
    the attacker becomes the defender. Then the while loop continues, 
    with the roles reversed. 

    Each knight takes a turn of attacking until one of the knights 
    temporary hp variables is equal to or less than zero. The winner 
    is then declared and the loop ends and the program goes back to 
    the main menu.
    """

    # Announce the duel
    print(
        "\nThe duel between the "
        + knights[knight_one]["colour"]
        + " Knight "
        + knights[knight_one]["name"]
        + " and the "
        + knights[knight_two]["colour"]
        + " Knight "
        + knights[knight_two]["name"]
        + " begins!\n"
    )

    # Find which knight gets the iniative and attacks first
    # Assign knight two as attacker and knight one as defender 
    attacker = knights[knight_two]
    defender = knights[knight_one]

    # Do a luck check to see who gets the initiative, swap
    # knight one as attacker if he wins
    if int(knights[knight_one]["luck"]) * random.randint(1, 20) > int(
        knights[knight_two]["luck"]
    ) * random.randint(1, 20):
        attacker = knights[knight_one]
        defender = knights[knight_two]

    # Save the knights health points to a temporary variable,
    # so that we are not reducing the actual hp on the knight
    attacker_hp = int(attacker["hp"])
    defender_hp = int(defender["hp"])

    # Combat loop
    while int(attacker_hp) > 0 and int(defender_hp) > 0:

        # Check if attack hits or misses
        if int(attacker["luck"]) * random.randint(2, 4) >= 35:

            # Attack hits
            # Check if the attack is a critical hit and inflict damage
            if int(attacker["luck"]) * random.randint(1, 5) >= 50:
                defender_hp -= attacker["damage"] * 2
                print(
                    "The "
                    + str(attacker["colour"])
                    + " Knight swings with his "
                    + str(attacker["weapon"])
                    + " and delivers a critical hit!"
                )

            # Inflict normal damage
            else:
                defender_hp -= attacker["damage"]
                print(
                    "The "
                    + str(attacker["colour"])
                    + " Knight swings with his "
                    + str(attacker["weapon"])
                    + " and hits!"
                )
            if defender_hp <= 0:
                print(
                    str(attacker["name"])
                    + " the "
                    + str(attacker["colour"])
                    + " Knight wins the duel!\n"
                )
                break
        else:

            # Attack misses
            print(
                "The "
                + str(attacker["colour"])
                + " Knight swings with his "
                + str(attacker["weapon"])
                + " and misses!"
            )

        # Switch the attacker and defenders
        # temporary health point around
        temp_hp = defender_hp
        defender_hp = attacker_hp
        attacker_hp = temp_hp

        # Switch the attacker and defender around
        # then loop again to next round of combat
        temp = defender
        defender = attacker
        attacker = temp


# This is the menu and we make our selections here
def menu(knights_number):
    """This is the main menu, where you can input an integer
    to go to the relevant page. Options are create a knight,
    update an existing knight, duel with knights or exit the
    program.
    
    In order to update a knight, you must already have at least
    one existing knight already. To start a duel, you must have 
    at least two knights created.
    """

    # Print the display options
    print("What do you want to do?")
    print("1: Create a new knight")
    print("2: Update your knights")
    print("3: Duel your knights")
    print("0: Exit")

    # Allow a selection to be tested
    try:

        # Takes the users selection option
        select = int(input("Selection number: "))
        print()  # Creates a blank line

        # Creates a new knight
        if select == 1:
            create_knight(knights)

            # Print out the Knight that was made
            print("\n--- Your Knight ---\n")
            print("Knight's name: " + str(
                knights[knights_number]["name"] + "\n"))
            knights_number += 1
            menu(knights_number)

        # Update an existing knight
        elif select == 2:

            # Check if a knight already exists
            if int(len(knights)) == 0:
                print("You need to create a knight first!\n")
            else:
                select_knight(knights)
            menu(knights_number)

        # Select two knights to enter into a duel
        elif select == 3:

            # Check if you have at least two knights
            if int(len(knights)) < 2:
                print("You need at least two knights to duel!")
            else:
                select_duelists(knights)
            menu(knights_number)

        # Exit the program
        elif select == 0:
            print("--- All your knights! ---\n")

            # Reset the knights_number, to count all the knights
            knights_number = 0
            # Print out all of the knights made
            while knights_number < int(len(knights)):
                print(
                    str(knights_number + 1)
                    + "- "
                    + str(knights[knights_number]["name"])
                    + " the "
                    + str(knights[knights_number]["colour"])
                    + " Knight, wielding a "
                    + str(knights[knights_number]["weapon"])
                )
                knights_number += 1

            # If no knights were made
            if int(len(knights)) == 0:
                print(
                    "Wait... You have no knights! Have a number: "
                    + str(random.randint(0, 100))
                )

        # Required for catching an integer
        else:
            print("--- Try Again! ---\n")
            menu(knights_number)

    # We are looking for integer selection
    except:
        print("--- Try Again! ---\n")
        menu(knights_number)
    

# Setting the scene
knights_number = 0
knights = []

# Run the program
menu(knights_number)
