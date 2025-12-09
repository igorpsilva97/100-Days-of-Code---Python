print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# --- BRANCH 1: The Cross Road ---
# Get the user's first choice.
# .lower() converts the input (e.g., "Left" or "LEFT") to "left"
# so the 'if' check is easier and not case-sensitive.
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()

# Check if the user chose the "correct" path.
if choice1 == "left":

    # --- BRANCH 2: The Lake (Nested inside "left") ---
    # This code only runs if the user chose "left" first.
    choice2 = input(
        'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()

    # Check if the user chose the "correct" path for branch 2.
    if choice2 == "wait":

        # --- BRANCH 3: The Doors (Nested inside "wait") ---
        # This code only runs if the user chose "left" AND THEN "wait".
        choice3 = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()

        # Check the final set of choices.
        if choice3 == "red":
            # Game Over path
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            # Winning path!
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            # Game Over path
            print("You enter a room of beasts. Game Over.")
        else:
            # This 'else' catches any invalid door choice (e.g., "green", "purple").
            print("You chose a door that doesn't exist. Game Over.")

    # This 'else' pairs with 'if choice2 == "wait"'.
    else:
        # This is the "swim" path (a Game Over).
        print("You get attacked by an angry trout. Game Over.")

# This 'else' pairs with the first 'if choice1 == "left"'.
else:
    # This is the "right" path (a Game Over).
    print("You fell into a hole. Game Over.")