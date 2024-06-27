import random
print("Welcome to 'whose wallet?'")
print("You will give me a list of names, and I will pick a person to pay")
names = input("If you're ready, enter the names separated by a comma: ")
names_list = names.split(", ")
random_number = random.randint(0, len(names_list) - 1)
print("plaese ask", names_list[random_number],
      "to take his wallet out. Dinner is on him")
