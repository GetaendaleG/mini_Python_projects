import random

top_of_range = input('Enter the top range: ')

if  top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print('Next time enter larger number than zero')
        quit()
else:
    print('Next time enter a number')
    quit()

score = 0

while True:
    random_no = random.randint(0,top_of_range)
    guessed_no = input("Guess the number (Enter quit if you want to quit): ")
    if guessed_no == "quit":
        quit()
    else:
        guessed_no = int(guessed_no)
        if guessed_no == random_no:
            score += 1
            print("You have guessed right the number is: "+ str(guessed_no))
            print("Score = "+ str(score))
        else:
            print("Incorrect, The number was : "+ str(random_no))
            print("Score = "+ str(score))    
    

