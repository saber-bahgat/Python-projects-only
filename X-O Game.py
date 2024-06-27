def check_winner(field, player):
  # Check rows
  for row in field:
      if all(cell == player for cell in row):
          return True
  # Check columns
  for col in range(3):
      if all(field[row][col] == player for row in range(3)):
          return True
  # Check diagonals
  if all(field[i][i] == player for i in range(3)) or all(field[i][2 - i] == player for i in range(3)):
      return True
  return False

print("Welcome to X-O Game")
field = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
print(f"{field[0]}\n{field[1]}\n{field[2]}")

current_player = "X"
while True:
  print(f"Where should the {current_player} be placed?")

  position = input("Enter the number 1 to 9: ")
  if position not in [str(i) for i in range(1, 10)]:
      print("Error! Invalid position. Please try again.")
      continue

  row = (int(position) - 1) // 3
  col = (int(position) - 1) % 3

  if field[row][col] in ["X", "O"]:
      print("Error! That cell is already taken. Please try again.")
      continue

  field[row][col] = current_player
  print(f"{field[0]}\n{field[1]}\n{field[2]}")

  if check_winner(field, current_player):
      print(f"Player {current_player} wins!")
      break

  if all(cell in ["X", "O"] for row in field for cell in row):
      print("It's a draw!")
      break

  current_player = "O" if current_player == "X" else "X"