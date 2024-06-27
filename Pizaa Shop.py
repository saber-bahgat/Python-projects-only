import random
import datetime

order_number = random.randint(10000, 99999)
current_datetime = datetime.datetime.now()



def Order_number(order_number):
    print(f"Your order number is: {order_number}")

def Current_datatime(current_datetime):
    formatted_date = current_datetime.strftime("%Y-%m-%d")
    formatted_time = current_datetime.strftime("%H:%M:%S")
    print(f"Date of Order: {formatted_date}" )
    print(f"Time of Order: {formatted_time}")

def pizza_info(name, price, ingredients):
    print(f"Name: {name}")
    print(f"Price: ${float(price)} for each one")
    print("Ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")
small_size = 0
medium_size = 0
large_size = 0
# ------------------------------------------------------------------------------------------------

while True:
    customer_name= input("Please Enter your name: ")
    if customer_name:
        print(f"Welcome '{customer_name}' in Pizza Shop!")
        print("Types of Pizza:")
        print("1.Margherita Pizza")
        print("2.Pepperoni Pizza")
        print("3.Hawaiian Pizza")
        print("4.Special Pizza")
        choice = (input("Enter your choice from 1 to 4: "))
                    
        # ---------------------------------------------------------------------------------
        if choice == "1":
            while True:
                print("-"*25)
                print("#Margherita Pizza!")
                print('1.Information about Pizza')
                print("2.Order this pizza")
                choice_Margherita = input("Enter your choice 1 or 2: ")
                if choice_Margherita == '1':
                    print("-"*15)
                    pizza_info(name='Margherita Pizza', price = 45 ,ingredients= ["Pizza dough","Tomato sauce","Mozzarella cheese","Fresh basil leaves","Olive oil","Salt"])
                elif choice_Margherita == '2':
                    print("-"*15)
                    print(f"okay, It's price is '45.0'")
                    print("-"*5)
                    while True:
                        num_of_margherita= input("How many pizzas do you want: ")
                        if num_of_margherita.isdigit() and int(num_of_margherita) > 0:
                            num_of_margherita = int(num_of_margherita)
                            break
                        else:
                            print("Enter a valid number, try again")
                            customer_name = 'Saber'
                    while True:
                        small_size = int(input("How many of the 'Small Size' do you want: "))
                        if small_size < num_of_margherita:
                            medium_size = int(input("How many of the 'Medium Size' do you want: "))
                            if medium_size + small_size < num_of_margherita:
                                large_size = int(input("How many of the 'Large Size' do you want: "))
                                if large_size + medium_size + small_size < num_of_margherita:
                                    print("Error in the order, please try again!")
                                elif large_size + medium_size + small_size == num_of_margherita:
                                    break
                                else:
                                    print("The quantity of the large size is greater than the order. There is an error in the amount,try again!")
                                    continue
                            elif medium_size + small_size == num_of_margherita:
                                break
                            else:
                                print("The quantity of the large size is greater than the order. There is an error in the amount,try again!")
                                continue
                            break
                        elif small_size == num_of_margherita:
                            break
                        else:
                            print("The quantity of the large size is greater than the order. There is an error in the amount,try again!")
                            continue
                    small_margherita_price = 0
                    large_margherita_price = 0   
                    margherita_price = num_of_margherita * float(45)
                    small_margherita_price = margherita_price -( small_size * 5)
                    large_margherita_price = margherita_price + ( large_size * 5)
                    all_margherita_price = (num_of_margherita * 45) - (small_size * 5) + (large_size * 5)
                    print(f"Alright, its price will be '{all_margherita_price}'")
                    address = input("Where do you want the pizza? (Your address): ")
                    Complete_order = input("Press Enter to complete the order...")
                    print("-"*5)
                    print(f"You will receive {num_of_margherita} Margherita pizzas: {small_size} Small, {medium_size} Medium, and {large_size} Large to '{address}' within 25 minutes.")
                    Order_number(order_number)
                    Current_datatime(current_datetime)
                    print(f"Thank you '{customer_name}' for being part of Pizza Shop!")
                    break
                else:
                    print("Error!, Please enter 1 or 2")
            break
        # -------------------------------------------------------------------------------------------
        elif choice == "2":
            while True:
                print("-"*25)
                print("#Pepperoni Pizza!")
                print('1.Information about Pizza')
                print("2.Order this pizza")
                choice_Pepperoni = input("Enter your choice 1 or 2: ")
                if choice_Pepperoni == "1":
                    print("-"*15)
                    pizza_info(name='Pepperoni Pizza', price = 50 ,ingredients= ["Pizza dough","Tomato sauce","Mozzarella cheese","Pepperoni slices","Olive oil","Grated Parmesan cheese","Dried oregano"])
                elif choice_Pepperoni == "2":
                    print("-"*15)
                    print(f"okay, It's price is '50.0'")
                    print("-"*5)
                    while True:
                        num_of_Pepperoni = input("How many pizzas do you want: ")
                        if num_of_Pepperoni.isdigit() and int(num_of_Pepperoni) > 0:
                            num_of_Pepperoni = int(num_of_Pepperoni)
                            break
                        else:
                            print("Enter a valid number, try again")
                    while True:
                        small_size = int(input("How many of the 'Small Size' do you want: "))
                        if small_size < num_of_Pepperoni:
                            medium_size = int(input("How many of the 'Medium Size' do you want: "))
                            if medium_size + small_size < num_of_Pepperoni:
                                large_size = int(input("How many of the 'Large Size' do you want: "))
                                if large_size + medium_size + small_size < num_of_Pepperoni:
                                    print("Error in the order, please try again!")
                                elif large_size + medium_size + small_size == num_of_Pepperoni:
                                    break
                                else:
                                    print("The quantity of the large size is greater than the order. There is an error in the amount,try again!")
                                    continue
                            elif medium_size + small_size == num_of_Pepperoni:
                                break
                            else:
                                print("The quantity of the large size is greater than the order. There is an error in the amount,try again!")
                                continue
                            break
                        elif small_size == num_of_Pepperoni:
                            break
                        else:
                            print("The quantity of the large size is greater than the order. There is an error in the amount,try again!")
                            continue
                    Pepperoni_price = (num_of_Pepperoni * 50) - (small_size * 5) + (large_size * 5)
                    print(f"Alright, its price will be '{Pepperoni_price}'")
                    address = input("Where do you want the pizza? (Your address): ")
                    Complete_order = input("Press Enter to complete the order...")
                    print("-"*5)
                    print(f"You will receive {num_of_Pepperoni} Pepperoni pizzas: {small_size} Small, {medium_size} Medium, and {large_size} Large to '{address}' within 25 minutes.")
                    Order_number(order_number)
                    Current_datatime(current_datetime)
                    print(f"Thank you '{customer_name}' for being part of Pizza Shop!")
                    break
                else:
                    print("Error!, Please enter 1 or 2")
            break

        elif choice == "3":
            while True:
                print("-"*25)
                print("#Hawaiian Pizza!")
                print('1.Information about Pizza')
                print("2.Order this pizza")
                choice_Hawaiian = input("Enter your choice 1 or 2: ")
                if choice_Hawaiian == "1":
                    print("-"*15)
                    pizza_info(name='Hawaiian Pizza', price = 60 ,ingredients= ["Pizza dough","Tomato sauce","Mozzarella cheese","Chicken pieces","Olive oil","Pineapple chunks","Dried oregano"])
                elif choice_Hawaiian == "2":
                    print("-"*15)
                    print(f"okay, It's price is '60.0'")
                    print("-"*5)
                    while True:
                        num_of_Hawaiian = input("How many pizzas do you want: ")
                        if num_of_Hawaiian.isdigit() and int(num_of_Hawaiian) > 0:
                            num_of_Hawaiian = int(num_of_Hawaiian)
                            break
                        else:
                            print("Enter a valid number, try again")
                    while True:
                        small_size = int(input("How many of the 'Small Size' do you want: "))
                        if small_size < num_of_Hawaiian:
                            medium_size = int(input("How many of the 'Medium Size' do you want: "))
                            if medium_size + small_size < num_of_Hawaiian:
                                large_size = int(input("How many of the 'Large Size' do you want: "))
                                if large_size + medium_size + small_size < num_of_Hawaiian:
                                    print("Error in the order, please try again!")
                                elif large_size + medium_size + small_size == num_of_Hawaiian:
                                    break
                                else:
                                    print("The quantity of the large size is greater than the order. There is an error in the amount,try again!")
                                    continue
                            elif medium_size + small_size == num_of_Hawaiian:
                                break
                            else:
                                print("The quantity of the large size is greater than the order. There is an error in the amount,try again!")
                                continue
                            break
                        elif small_size == num_of_Hawaiian:
                            break
                        else:
                            print("The quantity of the large size is greater than the order. There is an error in the amount,try again!")
                            continue
                    Hawaiian_price = (num_of_Hawaiian * 60) - (small_size * 5) + (large_size * 5)
                    print(f"Alright, its price will be '{Hawaiian_price}'")
                    address = input("Where do you want the pizza? (Your address): ")
                    Complete_order = input("Press Enter to complete the order...")
                    print("-"*5)
                    print(f"You will receive {num_of_Hawaiian} Hawaiian pizzas: {small_size} Small, {medium_size} Medium, and {large_size} Large to '{address}' within 25 minutes.")
                    Order_number(order_number)
                    Current_datatime(current_datetime)
                    print(f"Thank you '{customer_name}' for being part of Pizza Shop!")
                    break
                else:
                    print("Error!, Please enter 1 or 2")
            break

        # ---------------------------------------------------------------
        elif choice == "4":
            print("-"*25)
            print("#Special Pizza!")
            select_ingredients = []
            not_select_ingredients = []
            Special_price = 10
            all_ingredients = ["Pizza dough","Tomato sauce","Mozzarella cheese","Olive oil","Fresh basil leaves","Pepperoni slices","Grated Parmesan cheese","Dried oregano","Pineapple chunks","Salt"]
            for item in all_ingredients:
                special_ingredients = input(f"Do you want '{item}' in your pizza? (Y/N): ").lower()
                if special_ingredients == "y":
                    select_ingredients.append(item)
                    Special_price += 5
                elif special_ingredients == "n":
                    not_select_ingredients.append(item)
                else:
                    print("Unknown input!, please enter 'Y' for Yes or 'N' for No..")
            while True:
                print("-"*25)
                print('1.Information about Pizza')
                print("2.Order this pizza")
                choice_Special = input("Enter your choice 1 or 2: ")
                if choice_Special == "1":
                    print("-"*15)
                    pizza_info(name='Special Pizza', price = Special_price ,ingredients= select_ingredients)
                elif choice_Special == "2":
                    print("-"*15)
                    print(f"okay, It's price is '{Special_price}'")
                    print("-"*5)
                    while True:
                        num_of_Special = input("How many pizzas do you want: ")
                        if num_of_Special.isdigit() and int(num_of_Special) > 0:
                            num_of_Special = int(num_of_Special)
                            break
                        else:
                            print("Enter a valid number, try again")
                    while True:
                        small_size = int(input("How many of the 'Small Size' do you want: "))
                        if small_size < num_of_Special:
                            medium_size = int(input("How many of the 'Medium Size' do you want: "))
                            if medium_size + small_size < num_of_Special:
                                large_size = int(input("How many of the 'Large Size' do you want: "))
                                if large_size + medium_size + small_size < num_of_Special:
                                    print("Error in the order, please try again!")
                                elif large_size + medium_size + small_size == num_of_Special:
                                    break
                                else:
                                    print("The quantity of the large size is greater than the order. There is an error in the amount,try again!")
                                    continue
                            elif medium_size + small_size == num_of_Special:
                                break
                            else:
                                print("The quantity of the large size is greater than the order. There is an error in the amount,try again!")
                                continue
                            break
                        elif small_size == num_of_Special:
                            break
                        else:
                            print("The quantity of the large size is greater than the order. There is an error in the amount,try again!")
                            continue
                    Special_price = (num_of_Special * Special_price) - (small_size * 5) + (large_size * 5)
                    print(f"Alright, its price will be '{Special_price}'")
                    address = input("Where do you want the pizza? (Your address): ")
                    Complete_order = input("Press Enter to complete the order...")
                    print("-"*5)
                    print(f"You will receive {num_of_Special} Special pizzas: {small_size} Small, {medium_size} Medium, and {large_size} Large to '{address}' within 25 minutes.")
                    Order_number(order_number)
                    Current_datatime(current_datetime)
                    print(f"Thank you '{customer_name}' for being part of Pizza Shop!")
                    break
                else:
                    print("Error!, Please enter 1 or 2")
            break