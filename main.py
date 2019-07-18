board = [
  ["-","-","-"],
  ["-","-","-"],
  ["-","-","-"],
]

player_one_turn = False
character = "X"
game_over = False

def printBoard():
  rowTemplate = "| {} | {} | {} |"
  for row in board:
    print(rowTemplate.format(row[0], row[1], row[2]))

def updateBoard(x, y, character):
  board[x-1][y-1] = character

while game_over is False:
  printBoard()
  x = int(input("Select the row: "))
  y = int(input("Select the column: "))
  if player_one_turn is True:
    character = "X"
  else:
    character = "O"
  updateBoard(x, y, character)
  input("Press any key to pass turn to next player! ")