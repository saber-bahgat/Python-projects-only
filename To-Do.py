to_do = input("Enter your tasks for today seperated by a comma: ").split(", ")
done = []
not_done = []
for task in to_do:
  print(f"\n'{task}'\n")
  x = input("Did you finish it? (yes/no): ").lower()
  if x == "yes":
    print("Nice job")
    done.append(task)
  else:
    print("Try not to put it off")
    not_done.append(task)
  print("-"*7)
progress = input("Do you want to see your progress? (yes/no): ").lower()
if progress == "yes":
  print("\n********* Done Tasks **********\n")
  print(done)
else:
  print("Thanks for using our program")