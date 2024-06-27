# Welcome message
print("Welcome to Python Assistant!")

# Main loop for menu options
while True:
    # Display menu options
    print("1. Learning started")
    print("2. What Python Assistant does")
    print("3. Exit")
    
    # User input for menu choice
    choice_list_1 = input("Enter your choice from 1 to 3: ")

    # Handling choice 1: Learning started
    if choice_list_1 == "1":
         print("-"*30)
         print("# Learning started!")
         print("1. Basics")
         print("2. Data type")
         print("3. Variables")
         print("4. List")
         print("5. Loops and If")
         print("6. Function")
         
         # Sub-menu for learning topics
         choice_list_2 = input("Enter your choice from 1 to 6: ")

         if choice_list_2 == "1":
             # Handling choice 1: Basics
             print("-"*30)
             print("# Basics!")
             print("1. Print")
             print("2. Input")
             print("3. Comments")
             print("4. Debugging")
             basics_choice = input("Enter your choice from 1 to 4, *99 to choose all*: ")

             # Handling choices for basic topics
             if basics_choice == "1":
                print("-"*10)
                print("Print: To print words in your project")
                print("EX:")
                print('print("HI")  # output: HI')
             elif basics_choice == "2":
                print("-"*10)
                print("Input: You can ask the user a question to build the application on it")
                print("EX:")
                print("x = input('how are you?')")
             elif basics_choice == "3":
                print("-"*10)
                print("Comments: When you see the code you understand what it does")
                print("EX:")
                print("# This is comment!")
             elif basics_choice == "4":
                print("-"*10)
                print("Debugging: The word 'Debugging' denotes the resolution of programming errors such as 'Indication' and 'Syntax'")
                print("EX:")
                print("print(Hi bro)")
                print("Problem solving...")
                print("The right way: print('Hi bro')")
             elif basics_choice == "99":
                 print("-"*10)
                 print("Print: To print words in your project")
                 print("EX:")
                 print('print("HI")  # output: HI')
                 print("-"*10)
                 print("Input: You can ask the user a question to build the application on it")
                 print("EX:")
                 print("x = input('how are you?')")
                 print("-"*10)
                 print("Comments: When you see the code you understand what it does")
                 print("EX:")
                 print("# This is comment!")
                 print("-"*10)
                 print("Debugging: The word 'Debugging' denotes the resolution of programming errors such as 'Indication' and 'Syntax'")
                 print("EX:")
                 print("print(Hi bro)")
                 print("Problem solving...")
                 print("The right way: print('Hi bro')")
             else:
                print("Invalid choice!, please enter a number from 1 to 4 or *99 to choose all*")

         elif choice_list_2 == "2":
             # Handling choice 2: Data types
             print("-"*30)
             print("# Data type!")
             print("1. INT")
             print("2. STR")
             print("3. FLOAT")
             print("4. BOOL")
             print("5. COMPLEX")
             choice_data_type = input("Enter your choice from 1 to 5, *99 to choose all*: ")

             # Handling choices for data types
             if choice_data_type == "1":
                 print("-"*30)
                 print("Int: This is the data type dedicated to whole numbers such as '1' and '7'")
                 print("EX:")
                 print('my_age = 25')
                 print("print(type(my_age))  # Output: <class 'int'>")
             elif choice_data_type == "2":
                 print("-"*30)
                 print("STR: Custom data type for sentences like 'Hello World'")
                 print("EX:")
                 print('my_name = "Python Assistant"')
                 print("print(type(my_name))  # Output: <class 'str'>")
             elif choice_data_type == "3":
                 print("-"*30)
                 print("FLOAT: Data type for Decimal numbers such as '1.4 and 8.9'")
                 print("EX:")
                 print('pi_value = 3.14')
                 print("print(type(pi_value))  # Output: <class 'float'>")
             elif choice_data_type == "4":
                 print("-"*30)
                 print("BOOL: Type of data that means 'Yes or No'")
                 print("EX:")
                 print("""print(10 > 9)  # Output: True
print(10 == 9)  # Output: False
print(10 < 9)  # Output: False""")                 
             elif choice_data_type == "5":
                 print("-"*30)
                 print("COMPLEX: It is the type of data that means unreal arithmetic values like '4j'")
                 print("EX:")
                 print("complex_num = 1 + 2j")
                 print("print(type(complex_num))  # Output: <class 'complex'>")
             elif choice_data_type == "99":
                 print("-"*30)
                 print("Int: This is the data type dedicated to whole numbers such as '1' and '7'")
                 print("EX:")
                 print('my_age = 25')
                 print("print(type(my_age))  # Output: <class 'int'>")
                 print("-"*10)
                 print("STR: Custom data type for sentences like 'Hello World'")
                 print("EX:")
                 print('my_name = "Python Assistant"')
                 print("print(type(my_name))  # Output: <class 'str'>")
                 print("-"*10)
                 print("FLOAT: Data type for Decimal numbers such as '1.4 and 8.9'")
                 print("EX:")
                 print('pi_value = 3.14')
                 print("print(type(pi_value))  # Output: <class 'float'>")
                 print("-"*10)
                 print("BOOL: Type of data that means 'Yes or No'")
                 print("EX:")
                 print("""print(10 > 9)  # Output: True
print(10 == 9)  # Output: False
print(10 < 9)  # Output: False""")
                 print("-"*10)
                 print("COMPLEX: It is the type of data that means unreal arithmetic values like '4j'")
                 print("EX:")
                 print("complex_num = 1 + 2j")
                 print("print(type(complex_num))  # Output: <class 'complex'>")
             else:
                 print("Invalid choice!, please enter a number from 1 to 5 or *99 to choose all*")

         elif choice_list_2 == "3":
             # Handling choice 3: Variables
             print("-"*30)
             print("# Variables!")
             print("Variables: Used to store items of one type for example user age or user name")
             print("EX:")
             print("age = 15")
             print('print(age)  #Output: 15')         
         elif choice_list_2 == "4":
             # Handling choice 4: Lists
             print("-"*30)
             print("# List!")
             print("List: Used to store stuff of several types like '3', 'saber' and '5.9'")
             print("EX:")
             print("""fruits = ["apple", "banana", "cherry"]
print(type(fruits))  # Output: <class 'list'>""")
             print("Methods for List:")
             print("1. Append")
             print("2. Pop")
             print("3. Insert")
             print("4. Remove")
             print("5. Sort")
             print("6. Index")
             list_choice = input("Enter your choice from 1 to 6, *99 to choose all*: ")

             # Handling choices for list methods
             if list_choice == "1":
                 print("-"*10)
                 print(".append(): To add an item at the end of the list")
                 print("EX:")
                 print('''fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']''')
             elif list_choice == "2":
                 print("-"*10)
                 print(".pop(): To remove an item in a specific place in the list")
                 print("EX:")
                 print('''fruits = ['apple', 'banana', 'cherry']
removed_fruit = fruits.pop(1)
print(fruits)  # Output: ['apple', 'cherry']
print("Removed fruit:", removed_fruit)  # Output: Removed fruit: banana''')
             elif list_choice == "3":
                 print("-"*10)
                 print(".insert(): To add an item in a specific place in the list")
                 print("EX:")
                 print('''prime_numbers = [2, 3, 5, 7]
prime_numbers.insert(4, 11)  # Insert 11 at index 4
print("List:", prime_numbers) # Output: List: [2, 3, 5, 7, 11]''')
             elif list_choice == "4":
                 print("-"*10)
                 print(".remove(): To delete a selected item from the list")
                 print("EX:")
                 print("""fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")  # Removes the first occurrence of "banana"
print(fruits)  # Output: ['apple', 'cherry']""")
             elif list_choice == "5":
                 print("-"*10)
                 print(".sort(): To sort items alphabetically")
                 print("EX:")
                 print("""colors = ["red", "green", "blue"]
colors.sort()
print(colors)  # Output: ['blue', 'green', 'red']""")
             elif list_choice == "6":
                 print("-"*10)
                 print(".index(): To know the index of the element")
                 print("EX:")
                 print("""animals = ['cat', 'dog', 'rabbit', 'horse']
index_of_dog = animals.index('dog')
print("Index of 'dog':", index_of_dog) #Output: Index of 'dog': 1""")
             elif list_choice == "99":
                 print("-"*10)
                 print(".append(): To add an item at the end of the list")
                 print("EX:")
                 print('''fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']''')
                 print("-"*10)
                 print(".pop(): To remove an item in a specific place in the list")
                 print("EX:")
                 print('''fruits = ['apple', 'banana', 'cherry']
removed_fruit = fruits.pop(1)
print(fruits)  # Output: ['apple', 'cherry']
print("Removed fruit:", removed_fruit)  # Output: Removed fruit: banana''')
                 print("-"*10)
                 print(".insert(): To add an item in a specific place in the list")
                 print("EX:")
                 print('''prime_numbers = [2, 3, 5, 7]
prime_numbers.insert(4, 11)  # Insert 11 at index 4
print("List:", prime_numbers) # Output: List: [2, 3, 5, 7, 11]''')
                 print("-"*10)
                 print(".remove(): To delete a selected item from the list")
                 print("EX:")
                 print("""fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")  # Removes the first occurrence of "banana"
print(fruits)  # Output: ['apple', 'cherry']""")
                 print("-"*10)
                 print(".sort(): To sort items alphabetically")
                 print("EX:")
                 print("""colors = ["red", "green", "blue"]
colors.sort()
print(colors)  # Output: ['blue', 'green', 'red']""")
                 print("-"*10)
                 print(".index(): To know the index of the element")
                 print("EX:")
                 print("""animals = ['cat', 'dog', 'rabbit', 'horse']
index_of_dog = animals.index('dog')
print("Index of 'dog':", index_of_dog) #Output: Index of 'dog': 1""")
             else:
                 print("Invalid choice!, please enter a number from 1 to 6, *99 to choose all*")

         elif choice_list_2 == "5":
             # Handling choice 5: Loops and If
             print("-"*30)
             print("# Loops and If!")
             print("Loop: Expresses the repetition of something")
             print("Type of loops and If:")
             print("1. While Loop")
             print("2. For Loop")
             print("3. If")
             print("4. Else")
             print("5. Elif")
             loop_choice = input("Enter your choice from 1 to 5, *99 to choose all*: ")

             # Handling choices for loops and if conditions
             if loop_choice == "1":
                 print("-"*10)
                 print("While Loop: To repeat something infinitely")
                 print("EX:")
                 print('''# Calculate the sum of numbers until the user enters 0
number = int(input('Enter a number: '))
total = 0

# Iterate until the user enters 0
while number != 0:
    total += number
    number = int(input('Enter a number: '))

print('The sum is', total)''')
             elif loop_choice == "2":
                 print("-"*10)
                 print("For Loop: To repeat something for a specific period of time")
                 print("EX:")
                 print('''# Example 1: Looping through a list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
# Output:
# apple
# banana
# cherry''')
             elif loop_choice == "3":
                 print("-"*10)
                 print("If: For the manufacture of application algorithms ")
                 print("EX:")
                 print('''# Example of using 'if' in Python
# Define a variable
age = 25

# Check if the age is greater than or equal to 18
if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")
                       #Output: You are an adult''')
             elif loop_choice == "4":
                 print("-"*10)
                 print("Else: For the manufacture of application algorithms ")
                 print("EX:")
                 print('''x = 5
try:
    x > 10
except:
    print("Something went wrong")
else:
    print("The 'Try' code was executed without raising any errors!") #Output: The 'Try' code was executed without raising any errors!''')
             elif loop_choice == "5":
                 print("-"*10)
                 print("Elif: It is a mixture between If and Else, and is used to make application algorithms ")
                 print("EX:")
                 print('''# Example: Checking if a number is positive, negative, or zero
number = 0

if number > 0:
    print("Positive number")
elif number == 0:
    print("Zero")
else:
    print("Negative number") #Output: Zero''')
             elif loop_choice == "99":
                 print("-"*10)
                 print('''# Calculate the sum of numbers until the user enters 0
number = int(input('Enter a number: '))
total = 0

# Iterate until the user enters 0
while number != 0:
    total += number
    number = int(input('Enter a number: '))

print('The sum is', total)''')
                 print("-"*10)
                 print("For Loop: To repeat something for a specific period of time")
                 print("EX:")
                 print('''# Example 1: Looping through a list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
# Output:
# apple
# banana
# cherry''')
                 print("-"*10)
                 print("If: For the manufacture of application algorithms ")
                 print("EX:")
                 print('''# Example of using 'if' in Python
# Define a variable
age = 25

# Check if the age is greater than or equal to 18
if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")
                       #Output: You are an adult''')
                 print("-"*10)
                 print("Else: For the manufacture of application algorithms ")
                 print("EX:")
                 print('''x = 5
try:
    x > 10
except:
    print("Something went wrong")
else:
    print("The 'Try' code was executed without raising any errors!") #Output: The 'Try' code was executed without raising any errors!''')
                 print("-"*10)
                 print("Elif: It is a mixture between If and Else, and is used to make application algorithms ")
                 print("EX:")
                 print('''# Example: Checking if a number is positive, negative, or zero
number = 0

if number > 0:
    print("Positive number")
elif number == 0:
    print("Zero")
else:
    print("Negative number") #Output: Zero''')
             else:
                 print("Invalid choise!, please enter a number from 1 to 5, *99 to choice all*")

         elif choice_list_2 == "6":
             # Handling choice 6: Function
             print("-"*30)
             print("# Function!")
             print("Function: We use it to shorten the size of the code and make it more beautiful")
             print("EX:")
             print("""def greet():
    print('Hello World!')
# application 
greet()  #Output: Hello World!""")
         else:
             print("Invalid choise!, please enter a number from 1 to 5")
         print("-"*30)

    elif choice_list_1 == "2":
        # Handling choice 2: What Python Assistant does
        print("# What Python Assistant does!")
        print("**'Python Assistant' is an application that helps you learn Python")
        print("Or if you know Python and are proficient in it, it helps you remember the codes if you need")
        print("-"*7)
        print("<# Made by SABER JR #>")
        print("My Insta Username >> sab.er_jr")
        print("-"*30)

    # Exiting
    elif choice_list_1 == "3":
        print("Thank you for trying our application!")
        break 
    else:
        print("Invalid choise!, please enter a number from 1 to 3")
        