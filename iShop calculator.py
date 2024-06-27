print("***** Welcome to iShop calculator *****")
number=int(input("How many items are there in your basket today?\n"))
basket=[]
price=[]
print("Let's get to counting them ....")
for i in range(1,number+1):
  item=input("Please tell me the name of the item number "+str(i)+": ")
  basket.append(item)
  price_item=float(input("What is the price of "+item+"$: "))
  price.append(price_item)
see_basket=input("Would you like to see your entired basket items? (yes/no): ").lower()
if see_basket=="yes":
  print(basket)
see_price=input("Would you like to see how much it'll cost? (yes/no): ").lower()
if see_price=="yes":
  print(sum(price))
else:
  print("Okay, thank you for using our app")