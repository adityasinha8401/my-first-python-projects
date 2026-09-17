import random
print("Welcome to the Number Guessing Game!!")
number=random.randint(1,100)
Attempts=0
while Attempts<=5:
    guess=int(input("Guess a number between 1 and 100:"))
    Attempts+=1
    if guess<number:
        print("Too low, try again.")
    elif guess>number:
        print("Too high,try again.")
    else:
        print("CONGRATULATIONS!! ")
        print("You Guessed The Number")
        break
