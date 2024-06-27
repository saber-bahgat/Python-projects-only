print("Welcome in makeing user name!")
email = input("Enter your email: ").lower()
if email == '':
    print("Error!, Please try again...")
else:
    user_name = email.split("@")
    print(f"Your user name is: '{user_name[0]}'")