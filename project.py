import random

# Call for this when you want to create a new knight
def create_knight(knights):

    # Creates a new List for the knight
    knights_data = {}

    print("Lets create a knight!")

    # Set the information up for the knight
    # Set the knights name
    knights_data['name'] = (str(input("What is the knights name: ")))

    # Set the knights armour colour
    knights_data['colour'] = (str(input("What is the colour of the knights armor: ")))

    # Set the knights weapon of choice
    knights_data['weapon'] = (str(input("What weapon does the knight wield?: ")))

    # Randomly assign the knights health points
    knights_data['hp'] = (random.randint(70,100))

    # Randomly assign the knights baseline damage per hit
    knights_data['damage'] = (random.randint(10,20))

    # Randomly assign the knights luck
    knights_data['luck'] = (random.randint(0,100))

    # Adds the information to the knight
    knights.append(knights_data)

# Call a knight and change their data
def change_data(knights):
    #Print menu of ways to edit knight
    print("--- What would you like to update? ---")
    print("1: Knights Name: " + str(knights['name']))
    print("2: Colour Of Armor: " + str(knights['colour']))
    print("3: Knights Weapon: " +str(knights['weapon']))

    # Allow a selection to be tested
    try:
        selection = int(input("Select your option: "))

        # Rename the knight
        if selection == 1:
            knights['name'] = str(input("What is their new name: "))
            print("Your knight's new name is: " + str(knights['name']))
            return
        
        # Choose a new armor colour for knight
        elif selection == 2:
            knights['colour'] = str(input("What is their new armour colour: "))
            print("Your knight's new armour colour is: " + str(knights['colour']))
            return
        
        # Choose a new weapon for knight
        elif selection == 3:
            knights['weapon'] = str(input("What is their new weapon: "))
            print("Your knight's new weapon is: " + str(knights['weapon']))
            return
        
        # If no valid choice made
        else:
            print("--- Please select a valid option ---")       
    
    # We are looing for an integer selection
    except:
        print("(Change Data Error)--- Try Again ---")
        change_data(knights)

# Show the current knights and select one
def select_knight(knights):

    # Reset the list to print all the knights you have
    knights_number = 0
    print("What Knight would you like to update?\n")
    # Iterate through all knights in our list to print
    while knights_number < int(len(knights)):
        print(str(knights_number + 1) + "- Knight's name : " + str(knights[knights_number]['name']))
        knights_number += 1

    # Choose the knight and pass it into change_data
    selection = (int(input("\nSelect the Knights number: ")) - 1)
    change_data(knights[selection])

# This is the menu and we make our selections here
def menu(knights_number):
    # Print the display options
    print("What do you want to do?")
    print("1: Create a new knight")
    print("2: Update your knight")
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
            print("Knight's name: " + str(knights[knights_number]['name'] + "\n"))
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

        # Exit the program
        elif select == 0:
            print("--- All your knights! ---\n")

            # Reset the knights_number, to count all the knights
            knights_number = 0

            # Print out all of the knights made
            while knights_number < int(len(knights)):
                print(str(knights_number + 1) + "- " + str(knights[knights_number]['name']) + " the " + str(knights[knights_number]['colour']) 
                + " Knight, wielding a " + str(knights[knights_number]['weapon']))
                knights_number += 1

            # If no knights were made
            if int(len(knights)) == 0:
                print("Wait... You have no knights! Have a number: " + str(random.randint(0,100)))

        # Required for catching an integer
        else:
            print("--- Try Again! ---\n")
            menu(knights_number)

    # We are looking for integer selection
    except:
        print("(EXCEPTION)--- Try Again! ---\n")
        menu(knights_number)

# Setting the scene
knights_number = 0
knights = []

# Run the program
menu(knights_number)
