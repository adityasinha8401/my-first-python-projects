print("-----WELCOME TO THE PASSWORD CREATION PORTAL-----" )
print("Rules: Your Password must be 8 characters, must contain a number, and a special character (!,@,#,<,>,=,*,%,$,^,~)." )
while True:
    Password=input("Create a Password:")
    if len(Password)<8:
        print("Error!! Your password must be 8 characters long.\n")
        continue
    has_number=False
    has_special=False
    for character in Password:
        if character.isdigit():
            has_number=True
        elif character in "!@#<>=*%$^~":
            has_special=True
    if has_number==False:
        print("Error!! Your Password Must Contain a Number.")
    elif has_special==False:
        print("Error!! Your Password Must Contain a Special Character.")
    else:
        print("Success!! Your Password Was Created Successfully...")
        break
            
