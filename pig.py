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
        