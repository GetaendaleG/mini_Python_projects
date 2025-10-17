print('Welcome to my computer Quiz')

playing = input("Do you want to play: ").lower()

if playing != "yes":
    print("Bye :(")
else :
    print("Let's play :)")

score = 0

answer = input("What does cpu stands for?: ").lower()
if answer == "central processing unit":
    print("correct")
    score +=1
else:
    print('wrong')

answer = input("What does ram stands for?: ").lower()
if answer == "random access memory":
    print("correct")
    score +=1
else:
    print('wrong')

answer = input("What does gpu stands for?: ").lower()
if answer == "graphical processing unit":
    print("correct")
    score +=1
else:
    print('wrong')

answer = input("What does psu stands for?: ").lower()
if answer == "power supply unit":
    print("correct")
    score +=1
else:
    print('wrong')

print("your score will be: "+ str(score))
