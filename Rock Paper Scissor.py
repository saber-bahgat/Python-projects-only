import random
print("Welcome in my game")
user_choise=input("Plese enter your choise: Rock, Paper, Scissors: ").lower()
computer_choise=random.choice(["Rock", "Paper", "Scissors"]).lower()
print("             ")
print("Computer Chiose:",computer_choise)
if user_choise==computer_choise:
  print("Draw!")
elif user_choise=="rock" and computer_choise=="scissors" or user_choise=="paper" and computer_choise=="rock" or user_choise=="scissors" and computer_choise=="paper":
  print("You Win!")
elif  user_choise=="scissors" and computer_choise=="rock" or user_choise=="rock" and computer_choise=="paper" or user_choise=="paper" and computer_choise=="scissors":
  print("Sorry,You luse!")
print("Thanks for playing")
