"""
X2 Block clone

TODO make game object-oriented to solve all variable assignment issues

TODO refactor all code to be polymorphic

Version 0.1

https://play.google.com/store/apps/details?id=com.inspiredsquare.blocks
"""

from random import randint  # Needed in order to generate all numbers

class X2BlocksCloneCliImpl:
  """
  Command Line Interface implementation of X2BlocksClone
  """

  def __init__(width, height, block_highest=5):
    """
    Instances a new game. Constructs game grid of given width and height.

    blockHighest allows to set up to what number can be randomly generated.
    """

    # General game grid attributes
    self._width = width
    self._height = height
    self._grid = [[0 for x in range(width)] for y in range(height)]

    # Other gameplay propertied
    self._block_highest = block_highest

  def aimAt(self):
    try:
      return int(input(f"Where to shoot?\t"))
    except ValueError:
      return -1

  # May no longer be needed as __init__ constructor can build the grid.
  #def buildGameGrid(self, width: int, height: int):
  #  """
  #  Constructs game grid of given width and height
  #  """
  #  return [[0 for x in range(width)] for y in range(height)] 

  def fall(self):
    """
    Makes the blocks fall into the empty spaces (the zeroes) until all blocks have
    fallen to the very bottom of the grid and stack one over others that are below
    in the same column.
    """

    for column in range(self._width):
      blocksInColumn = [self._grid[cell][column] for cell in range(self._height) 
          if self._grid[cell][column] != 0]  # get only actual blocks
      newColumn = blocksInColumn +[0 for zero in range(self._height -len(blocksInColumn))]
      # Join blocksInColumn and fill the rest of the column with zeros as 
      # blocksInColumn already has all blocks filtered at the bottom.

      # assign the actual column from mewColumn
      for cell in range(self._height):
        self._grid[cell][column] = newColumn[cell]

  def howFullIsGrid(self):
    """
    return a percentage of how much of gameGrid is full, that is, all of its cells
    have non-zero values.
    """
    factor = 1 /(self._width *self._height)
    percentage = 0

    for row in self._grid:
      for cell in row:
        if cell != 0:
          percentage += factor
    
    return round(percentage, ndigits=2)

  def isGridFull(self, gameGrid):
    """
    Checks if gameGrid is full by checking if the top-most row is full of blocks.
    """
    topmostRow = len(gameGrid) -1
    count = len(gameGrid[topmostRow])

    for block in gameGrid[topmostRow]:
      if block != 0:
        count -= 1
    return count == 0

  def makeMerges(self, gameGrid, column):
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

  def nextBlock(self, ):
    """
    Generate next block.

    TODO implement more dynamism according to the highest number there is in the
    grid.

    TODO When block can't be put in grid, preserve it to not throw it away.-
    """
    if blockTemp == 0:
      return randint(1, blockHighest)
    return blockTemp

  def play(self, gameGrid):
    """
    Manages all the gameplay logic.
    """
    while not isGridFull(gameGrid):
      # TODO: Tidy up login for every turn
      # TODO: Handle all excpetions
      takeTurn(gameGrid)
      printGrid(gameGrid)

  def printGrid(self, gameGrid):
    for row in gameGrid:
      for cell in row:
        print(cell, end=" ")
      print()
    print()

  def shoot(self, gameGrid, block, column):
    """
    Puts blocks in the bottom most row
    """
    row = -1  # Tracks what row to put blocks in. It is incremented in the following
    # loop.
    # _row os just an index to move though the column. The following loop stops when
    # it finds the bottom most empty spot to put block in.
    for _row in range(len(gameGrid)):
      row += 1
      if gameGrid[_row][column] == 0:
        break
    
    # Put the block in the bottom most blank
    if gameGrid[row][column] == 0:
      #gameGrid[row][column] == 0
      gameGrid[row][column] = block
      blockTemp = 0
    elif gameGrid[row][column] == block:
      gameGrid[row][column] += 1
      blockTemp = 0
    else:
      blockTemp = block
      #raise ValueError("The column is full. Can't shoot!")
      # TODO: Throw custom exception for the game


  def takeTurn(self, gameGrid):
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
      fall(gameGrid)
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
  game = X2BlocksCloneCliImpl(width, height)
  game.play()

