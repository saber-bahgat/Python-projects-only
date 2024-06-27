def kirchhoff_equation():
  pass

def circuit_breaker_equation():
  ...
print("Welcome in my task, (Kirchoff & Circuit Breaker)")
print()
while True:
  print("1.Kirchhoff's Equation")
  print("2.Circuit Breaker Equation")
  print("3.Team Members")
  print("4.Exit")
  choice = input("Enter your choice from 1 to 4: ")
  if choice == "1":
    print("#Kirchhoff's Equation!")
    kirchhoff_equation()
    print("-"*30)
    
  elif choice == "2":
    print("#Circuit Breaker Equation!")
    circuit_breaker_equation()
    print("-"*30)

  elif choice == "3":
    print("#Team Members!")
    print("Saber Bahgat")
    print("Mostafa Abd El Moneim")
    print("Omar Hamdy")
    print("Mohamed Hesham")
    print("Kirullos Salah")
    print("-"*30)
    
  elif choice == "4":
    print("Thank you for trying our application!")
    break 
  else:
    print("Invalid choise!, please enter a number from 1 to 4")