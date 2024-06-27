print("Welcome to place the rabbit")
field=[["🌿", "🌿" ,"🌿"],["🌿", "🌿", "🌿"],["🌿", "🌿", "🌿"]]
print(f"{field[0]}\n{field[1]}\n{field[2]}")
print("Where should the rabbit go?🐇")
position=input("Please choose a row and a column: ").split(", ")
row=int(position[0])
column=int(position[1])
field[row-1][column-1]="🐇"
print("Success....")
print(f"{field[0]}\n{field[1]}\n{field[2]}")