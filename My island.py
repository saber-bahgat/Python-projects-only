print(".・。.・゜✭・.  ☠  Welcome to my island ☠︎  .・。.・゜✭・.")
print()
print()
print()
color_door=input("""There are two doors.🚪a red door and 🚪a blue door\n Whitch door do you want to open?\n""").lower()
if color_door=="red":
  print("Great! now you entered a room.")
  boxes= input("""You found three boxes: 🎁 White, 🎁 Black, 🎁 Green \n Witch box do you open?\n""").lower()
  if boxes=="black":
    print("Congratulations! You found the treasure! 💰💰💰")
  elif boxes=="green":
    print("Oops! You opend a box filled with snakes 🐍🐍🐍")
  elif boxes=="white":
    print("Oops! You opend a box filled with spiders 🕷 🕷 🕷")
  else:
    print("Invalid choice! 🤷‍♂️🤷‍♂️🤷‍♂️")

elif color_door=="blue":
  print("Oops! you chose the croccodille door.\n GAME OVER!🐊🐊🐊")
else:
  print(f"Sorry! [{color_door}] is not an option.🤷‍♂️🤷‍♂️🤷‍♂️")
  print("Try agian!")