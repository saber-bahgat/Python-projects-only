print("Welcome to my Calculator")
while True:
    while True:
        try:
            first_num = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input!, Please enter a number")

    while True:
        try:
            operation = input("Enter the operation: ")
            if operation in ("*", "/", "//", "**", "+", "-", "%"):
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid operator, Please enter *, **, +, -, /, //, %")

    while True:
        try:
            second_num = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input!, Please enter a number")

    if operation == "+":
      result = first_num + second_num
    elif operation == "-":
      result = first_num - second_num
    elif operation == "/":
      if second_num == 0:
          print("Cannot divide by zero!")
          continue
      else:
          result = first_num / second_num
    elif operation == "*":
      result = first_num * second_num
    elif operation == "**":
      result = first_num ** second_num
    elif operation == "%":
      result = first_num % second_num
    elif operation == "//":
      result = first_num // second_num
    else:
      result = None
    if result is not None:
        print("Result is:", result)

    repeat = input("Do you want to perform another operation (Yes/No): ").lower()
    if repeat == "no":
      print("Program exited!")
      break
    elif repeat == "yes":
      continue
    else:
     print("Invalid input, Please enter yes or no next time")
     break