print("Welcome To Your Fitness Target Tracker!!")
target_steps=int(input("Enter your target steps for the day:"))
total_steps_walked=0
print("The target steps for the day is:", target_steps)
while total_steps_walked<target_steps:
    remaining_steps=target_steps-total_steps_walked
    print("You Have", remaining_steps, "Steps Remaining To Reach Your Target!!")
    steps_walked=int(input("Enter the number of steps walked:"))
    if steps_walked<0:
        print("Please enter a valid number of steps.")
        continue
    else:
        print("You have walked", steps_walked, "steps.")
        total_steps_walked+=steps_walked
        print("Total steps walked so far:", total_steps_walked)
print("CONGRATULATIONS!! You have reached your target steps for the day!!")
print("Total Steps Walked:", total_steps_walked)
input("Press Enter to exit the program...")


    

