import MergeAllIntoOne

def play(game):
  """
  Manages all the gameplay logic.
  """
  while not game.isGridFull():
    # TODO 4 Handle all excpetions
    block = game.nextBlock()
    print(f"Block: {block}")
    print(f"Score: {game.getScore()}")
    column = int(input(f"What column to put block at?\t"))
    game.playTurn(column, block)
    printGrid(game)

def printGrid(game):
  """
  Prints the actual grid to the terminal in the following format:

  ```
  0 0 0 . . .
  0 0 0 . . .
  0 0 0 . . .
  . . . .    
  . . .   .  
  . . .     . 
  ```
  """
  print()
  for row in game.getGrid():
    for cell in row:
      print(cell, end=" ")
    print()
  print()


width, height = 5, 7

if __name__ == "__main__":
  game = MergeAllIntoOne.MergeAllIntoOne(grid=(width, height))
  play(game)
