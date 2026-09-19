import random
print("WELCOME TO ROCK,PAPER,SCISSORS!!")
print("Type 'rock','paper',or 'scissors' to play.")
print("Type 'quit' to exit the game.")
options=["rock","paper","scissors"]
while True:
    user_choice=input("Your Turn:").lower()
    if user_choice=="quit":
        print("Thanks For Playing!! Goodbye...")
        break
    if user_choice not in options:
        print("Oops!!Invalid Choice,choose 'rock','paper', or 'scissors'...")
        continue
    computer_choice=random.choice(options)
    print("Computer Choice:",computer_choice)
    if user_choice==computer_choice:
        print("Oooh!! It's a tie...")
    elif (user_choice=="rock" and computer_choice=="scissors") or \
         (user_choice=="paper" and computer_choice=="rock") or \
         (user_choice=="scissors" and computer_choice=="paper"):
        print("Yayy!! You win...")
    else:
        print("Computer Wins..Better Luck Next Time...")
    print("-"*30)
input("Press Enter to exit...")
