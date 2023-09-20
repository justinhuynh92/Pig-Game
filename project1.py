import random

#create function for rolling a die
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

#enter the required number of players using a while loop
while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    #error handling
    else:
        print("Invalid, try again.")

#make a list comprehension that puts a 0 inside the list for every player we have
max_score = 50
player_scores = [0 for _ in range(players)]
#keep going as long as no one's reached the max score
while max(player_scores) < max_score:

    current_score = 0

    should_roll = input("Would you like to roll (y)? ")
    #check if its lower case before proceeding
    if should_roll.lower() != "y":
        break

    value = roll()
    if value == 0:
        print("You rolled a 1! Turn done!")
    else:
        print("You rolled a:", value)
