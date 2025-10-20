import random

top_of_number = input('Enter the top range: ')

if  top_of_number.isdigit():
    top_of_number = int(top_of_number)
    if top_of_number <= 0:
        print('Next time enter larger number than zero')
        quit()
else:
    print('Next time enter a number')
    quit()
print(top_of_number)
