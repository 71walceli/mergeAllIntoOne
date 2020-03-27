"""
X2 Block clone

Version 0.1

https://play.google.com/store/apps/details?id=com.inspiredsquare.blocks
"""

from random import randint  # Needed in order to generate all numbers

def aimAt(gameGrid):
  try:
    return int(input(f"Where to shoot?\t"))
  except ValueError:
    return -1
    
def buildGameGrid(width: int, height: int):
  """
  Constructs game grid of given width and height
  """
  return [[0 for x in range(width)] for y in range(height)] 

def fall(gameGrid):
  """
  Makes the blocks fall into the empty spaces (the zeroes) until all blocks have
  fallen to the very bottom of the grid and stack one over others that are below
  in the same column.
  """

  for column in range(len(gameGrid[0])):
    for row in range(len(gameGrid) -1):
      rowAbove = row +1
      if gameGrid[rowAbove][column] != 0 and gameGrid[row][column] == 0:
        gameGrid[row][column]      = gameGrid[rowAbove][column]
        gameGrid[rowAbove][column] = 0


def howFullIsGrid(gameGrid):
  """
  return a percentage of how much of gameGrid is full, that is, all of its cells
  have non-zero values.
  """
  factor = 1 /(width *height)
  percentage = 0

  for row in gameGrid:
    for cell in row:
      if cell != 0:
        percentage += factor
  
  return round(percentage, ndigits=2)

def isGridFull(gameGrid):
  """
  Checks if gameGrid is full by checking if the top-most row is full of blocks.
  """
  topmostRow = len(gameGrid) -1
  count = len(gameGrid[topmostRow])

  for block in gameGrid[topmostRow]:
    if block != 0:
      count -= 1
  return count == 0

def makeMerges(gameGrid, column):
  row = -1
  for _row in range(len(gameGrid)):
    if gameGrid[_row][column] != 0:
      row += 1
    else:
      break

  checkBlock  = gameGrid[row][column]
  columnLeft  = column -1
  columnRight = column +1
  rowBelow    = row -1

  if column != 0                       and gameGrid[row][columnLeft] == checkBlock :
    gameGrid[row][column]      += 1
    gameGrid[row][columnLeft]   = 0
    makeMerges(gameGrid, column)
  
  if columnRight != len(gameGrid[row]) and gameGrid[row][columnRight] == checkBlock:
    gameGrid[row][column]      += 1
    gameGrid[row][columnRight]  = 0
    makeMerges(gameGrid, column)
  
  if row != 0 and gameGrid[rowBelow][column] == checkBlock:
    actualBlock                = gameGrid[row][column] +1
    gameGrid[rowBelow][column] = actualBlock
    gameGrid[row][column]      = 0
    makeMerges(gameGrid, column)

def nextBlock():
  """
  Generate next block.

  TODO implement more dynamism according to the highest number there is in the
  grid.

  TODO When block can't be put in grid, preserve it to not throw away.-
  """
  if blockTemp == 0:
    return randint(1, blockHighest)
  return blockTemp

def play(gameGrid):
  """
  Manages all the gameplay logic.
  """
  while not isGridFull(gameGrid):
    # TODO: Tidy up login for every turn
    # TODO: Handle all excpetions
    takeTurn(gameGrid)
    printGrid(gameGrid)

def printGrid(gameGrid):
  for row in gameGrid:
    for cell in row:
      print(cell, end=" ")
    print()
  print()

def shoot(gameGrid, block, column):
  """
  Puts blocks in the bottom most row
  """
  row = -1
  for _row in range(len(gameGrid)):
    row += 1
    if gameGrid[_row][column] == 0:
      break
  
  if gameGrid[row][column] == 0:
    gameGrid[row][column] == 0
    gameGrid[row][column] = block
  elif gameGrid[row][column] == block:
    gameGrid[row][column] += 1
  else:
    pass
    #raise ValueError("The column is full. Can't shoot!")
    # TODO: Throw custom exception for the game


def takeTurn(gameGrid):
  """
  Play a turn every time. Lets exceptions spread, which the main game loop should
  handle and act accordingly.
  """
  block = nextBlock()
  print(f"Block: {block}")
  column = aimAt(gameGrid)    # what column to shoot at?
  if column in range(width):  # range() domain is [0, width -1]
    shoot(gameGrid, block, column)  # FIXME when block isn't shot, return the 
    # previous one, to prevent the player from thowing away blocks.
    # TODO Improve self-arranging logic to fall() and merge() when it must
    makeMerges(gameGrid, column)    # TODO more testing!
    fall(gameGrid)  # FIXME it isn't making stacking blocks fall when lower blocks
    # merge.
  else:
    print("Invalid input")
    blockTemp = block

width, height = 5, 7

"""
stores a block when it couldn't be shot
"""
blockTemp = 0

"""
stores the highest block in the board. 

TODO implement logic to look for the highest in the grid.
"""
blockHighest = 5

if __name__ == "__main__":
  gameGrid = buildGameGrid(width, height)
  play(gameGrid)

