import random
print("Welcome in my game!")
while True:
    rulse = input("Do you want to know the rules? (Y/N): ").lower()
    if rulse == "y":
        print("The rules come on: \n**you choose a number between 1 and 10 and the computer is like you, and if you expect the same computer number, you win**")
    elif rulse == "n":
      ...
    else:
        print("Error!,Please enter 'Y' or 'N'")
    user_choice = int(input("Enter your choice from 1 to 10: "))
    computer_choice = random.randint(1,10)
    if user_choice == computer_choice:
        print(f"Your Choice is {user_choice}")
        print(f"Computer Choice is {computer_choice}")
        print("You Win!")
    else:
        print(f"Your Choice is {user_choice}")
        print(f"Computer Choice is {computer_choice}")
        print("You Lose!")
    exit = input("Do you want to go out? (Y/N): ").lower()
    if exit == "y":
        print("Thx for using my game")
        break
    elif exit == "n":
        print("Welcome Back!")
        continue
    else:
        print("Error!, Please enter 'Y' or 'N'")
