print("---USER LOGIN PANEL---")
while True:
    username=input("Enter your username:")
    password=input("Enter your password(atleast 6 characters):")
    if len(password)<6:
        print("Error!! Password must be atleast 6 characters long")
    else:
        print("Login Successful")
        print("Welcome to the system....",username)
        break
print("===USER LOGIN PANEL===")
attempts_left=3
while attempts_left>0:
    Login_Username=input("Enter your username:")
    Login_Password=input("Enter your password:")
    if Login_Username==username and Login_Password==password:
        print("Login Successful")
        break
    else:
        print("Error!! Invalid Username or Password")
        attempts_left-=1
        print("Attempts Left:",attempts_left)
if attempts_left==0:
    print("Error!! You have exceeded the maximum number of attempts. Please try again later.")



 
