#!/usr/bin/env python3

board = [
  ["-","-","-"],
  ["-","-","-"],
  ["-","-","-"],
]

player_one_turn = True
player_one_character = "X"
player_two_character = "O"
game_over = False

def printBoard():
  rowTemplate = "| {} | {} | {} |"
  for row in board:
    print(rowTemplate.format(row[0], row[1], row[2]))

def updateBoard(x, y, character):
  board[x-1][y-1] = character

def isValidMove(x, y):
  if board[x-1][y-1] is "-":
    return True
  else:
    return False

def isGameOver():
  winning_conditions = (
    ((0,0), (0,1), (0,2)),
    ((1,0), (1,1), (1,2)),
    ((2,0), (2,1), (2,2)),
    ((0,0), (1,0), (2,0)),
    ((0,1), (1,1), (2,1)),
    ((0,2), (1,2), (2,2)),
    ((0,0), (1,1), (2,2)),
    ((0,2), (1,1), (2,0)),
  )

  for condition in winning_conditions:
    a = condition[0]
    b = condition[1]
    c = condition[2]

    A = board[a[0]][a[1]]
    B = board[b[0]][b[1]]
    C = board[c[0]][c[1]]

    if A == "X" or A == "O":
      if A == B and B == C:
        return True
    else:
      continue
  return False

while game_over is False:
  player_id = 0
  if player_one_turn is True:
    player_id = 1
  else:
    player_id = 2
  print("Player {}'s turn!".format(player_id))
  printBoard()
  print("Make your move")
  x = int(input("Select the row: "))
  y = int(input("Select the column: "))
  if x not in range(4) or y not in range(4):
    continue
  if isValidMove(x, y) is False:
    print("That spot is taken! Illegal move...")
    continue
  if player_one_turn == True:
    updateBoard(x, y, player_one_character)
  else:
    updateBoard(x, y, player_two_character)
  input("Press any key to pass turn to next player! ")
  if isGameOver():
    print("Player {} won!".format(player_id))
    printBoard()
    break
  player_one_turn = not player_one_turn