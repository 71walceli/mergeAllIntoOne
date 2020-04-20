import MergeAllIntoOne

def play(game):
  """
  Manages all the gameplay logic.
  """
  while not game.isGridFull():
    # TODO: Handle all excpetions
    block = game.nextBlock()
    print(f"Block: {block}")
    print(f"Score: {game._score}")
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
  for row in game._grid:
    for cell in row:
      print(cell, end=" ")
    print()
  print()


width, height = 5, 7

if __name__ == "__main__":
  game = MergeAllIntoOne.MergeAllIntoOne(width, height)
  play(game)
