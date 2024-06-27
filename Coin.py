import random
print("Welcome to the coin toss game!")
user_choice=input("Enter the chose of your side, Head or Tail:")
com_choice=random.randint(0,1)
if com_choice==0:
  computer_choice="HEAD"
else:
  computer_choice="TAIL"
if user_choice.upper()==computer_choice:
  print("YOU WIN!")
else:
    print("YOU LOSE!")
print("Computer chose ["+computer_choice+"]")