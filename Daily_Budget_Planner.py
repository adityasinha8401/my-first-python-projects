print("WELCOME TO YOUR DAILY BUDGET TRACKER !!")
total_spent=0
expense_count=0
print("Type your expenses one by one")
print("When you are done, type 'EXIT' to see your total expenses.")
while True:
    expense=input("Enter your expense or type 'EXIT':")
    if expense=="EXIT":
        print("\nStopping Data Collection...")
        break
    else:
        amount=float(expense)
        total_spent+=amount
        expense_count+=1
print("\nYour Financial Summmary For The Day is :")
print("Total Expenses Recorded:",total_spent)
print("Total Number of Expenses Recorded:",expense_count)




