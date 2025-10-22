import random

def roll():
    max_no = 6
    min_no = 1
    roll = random.randint(min_no,max_no)
    return roll
score = 0


while True:
    players = input("Enter no of Players (2-4)")
    if players.isdigit():
        players = int(players)
        if 2<=players<=4:
            break
        else:
            print("No of players must be between 2 and 4")
    else:
        print("Invalid Input")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores)< max_score:
    should_roll = input("would you like to roll(y)? ")
    if should_roll.lower() != "y":
        break
    
    value = roll()
    if value == 1 :
        print("your rolled a 1 Turn done!")
    else:
        cureent_score == value
        print("you rolled a:")
    
