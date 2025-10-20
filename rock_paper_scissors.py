import random

options = ["rock","paper","scissor"]
compuer_score = 0
user_score = 0

while True:
    user_input = input("Enter Rock/Paper/Scissor or 'q' to quit: ").lower()
    if user_input == "q":
        break
    elif user_input not in options:
        continue
    
    computer_picked = options[random.randint(0,2)]
    print("Computer Picked:",computer_picked)
    if user_input == "rock" and computer_picked == "scissor":
        print("You Won!")
        user_score +=1 
        continue
    elif user_input == "paper" and computer_picked == "rock":
        print("You Won!")
        user_score +=1
        continue
    elif user_input == "scissor" and computer_picked == "paper":
        print("You Won!")
        user_score +=1
        continue
    else:
        print('You lose')
        compuer_score += 1
print("Your score is:",user_score)
print("Compuer score is:",compuer_score)
print("Bye!")