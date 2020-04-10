"""
X2 Block clone
https://play.google.com/store/apps/details?id=com.inspiredsquare.blocks

TODO refactor all code to be polymorphic

Version 0.1

"""

from random import randint  # Needed in order to generate all numbers

class X2BlocksCloneCliImpl:
  """
  Command Line Interface implementation of X2BlocksClone
  """

  def __init__(self, width, height, block_highest=5, grid=None):
    """
    Instances a new game. Constructs game grid of given width and height.

    blockHighest allows to set up to what number can be randomly generated.
    """

    # General game grid attributes
    self._width = width
    self._height = height
    if grid == None:
      self._grid = [[0 for x in range(width)] for y in range(height)]
    else:
      self._grid = grid

    # Other gameplay properties
    self._block_highest = block_highest  # TODO implement logic to look for the
    # highest in the grid.
    self._storedBlock   = 0

  def aimAt(self):
    try:
      return int(input(f"Where to shoot?\t"))
    except ValueError:
      return -1

  # May no longer be needed as __init__ constructor can build the grid.
  #def buildself._grid(self, width: int, height: int):
  #  """
  #  Constructs game grid of given width and height
  #  """
  #  return [[0 for x in range(width)] for y in range(height)] 

  def fall(self):
    """
    Makes the blocks fall into the empty spaces (the zeroes) until all blocks have
    fallen to the very bottom of the grid and stack one over others that are below
    in the same column.

    TODO Separate logic to make each column fall independently, as one column's
    falling is independent, except for merging.
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
    return a percentage of how much of self._grid is full, that is, all of its cells
    have non-zero values.
    """
    factor = 1 /(self._width *self._height)
    percentage = 0

    for row in self._grid:
      for cell in row:
        if cell != 0:
          percentage += factor
    
    return round(percentage, ndigits=2)

  def isGridFull(self):
    """
    Checks if self._grid is full by checking if the top-most row is full of blocks.
    """
    topmostRow = self._height -1  # index fir topmost row
    count = width

    for block in self._grid[topmostRow]:
      if block != 0:
        count -= 1     # count down for every used space.
    return count == 0  # returns trie if the top row is full.

  # Unused
  def makeMerges(self, column):
    """
    Makes all the merges in a column happen. The merging occurs in this way:

    TODO 2 Refactor this routine to do all posible merges in the given column
    """

  def merge(self, row, column):
    """
    Causes a block to merge as many times as it can. The prosess by which this      
    happens is the following:

    1. A block's value is polled and stored.
    2. The stored value is compared for equality to the left block's value, and
    merged into the block whose value was stored.
    3. As in the previous step, the block on the right is merged if the stored and
    the block's value match.
    4. The block over the one checked is merged downward as explained.
    
    The result is a block incremented once for every successful merge, at the same
    position as the block whose value is taken, unless it was above another piece
    that had equal value, in which case, it will be one place below. All merges can
    happen at once.
    """
    checkBlock  = self._grid[row][column]
    if checkBlock == 0:
      return  # Merging doesn't happen if piece in this position is zero.
    
    # Indexes to check surrounding blocks
    columnLeft  = column -1
    columnRight = column +1
    rowBelow    = row -1

    if column != 0                       and self._grid[row][columnLeft] == checkBlock :
      self._grid[row][column]      += 1
      self._grid[row][columnLeft]   = 0
      #self.merge(row, column)
    
    if columnRight != len(self._grid[row]) and self._grid[row][columnRight] == checkBlock:
      self._grid[row][column]      += 1
      self._grid[row][columnRight]  = 0
      #self.merge(row, column)
    
    if row != 0 and self._grid[rowBelow][column] == checkBlock:
      actualBlock                  = self._grid[row][column] +1
      self._grid[rowBelow][column] = actualBlock
      self._grid[row][column]      = 0
      self.merge(rowBelow, column)

  def nextBlock(self):
    """
    Generate next block to be shot

    TODO implement more dynamism according to the highest number there is in the
    grid.

    TODO When block can't be put in grid, preserve it to not throw it away.
    """
    #if self._storedBlock == 0:
    #  return randint(1, blockHighest)
    #return self._storedBlock
    return randint(1, self._block_highest)

  def play(self):
    """
    Manages all the gameplay logic.
    """
    while not self.isGridFull():
      # TODO: Tidy up logic for every turn
      # TODO: Handle all excpetions
      self.takeTurn()
      self.printGrid()

  def printGrid(self):
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
    for row in self._grid:
      for cell in row:
        print(cell, end=" ")
      print()
    print()

  def shoot(self, block, column):
    """
    Puts blocks in the bottom most row
    """
    row = -1  # Tracks what row to put blocks in. It is incremented in the following
    # loop.
    # _row os just an index to move though the column. The following loop stops when
    # it finds the bottom most empty spot to put block in.
    for _row in range(len(self._grid)):
      row += 1
      if self._grid[_row][column] == 0:
        break
    
    # Put the block in the bottom most blank
    if self._grid[row][column] == 0:
      #self._grid[row][column] == 0
      self._grid[row][column] = block
      #self._storedBlock = 0
    elif self._grid[row][column] == block:
      self._grid[row][column] += 1
      #self._storedBlock = 0
    else:
      return None
      #self._storedBlock = block
      #raise ValueError("The column is full. Can't shoot!")
      # TODO: Throw custom exception for the game
    
    return (row, column)

  def takeTurn(self):
    """
    Play a turn every time. Lets exceptions spread, which the main game loop should
    handle and act accordingly.
    """
    block = self.nextBlock()
    print(f"Block: {block}")
    column = self.aimAt()    # what column to shoot at?
    if column in range(width):  # range() domain is [0, width -1]
      shotPosition = self.shoot(block, column)  # FIXME when block isn't shot, return #
      # the previous one, to prevent the player from thowing away blocks.
      # TODO Improve self-arranging logic to fall() and merge() when it must
      if shotPosition != None:
        self.merge(shotPosition[0], shotPosition[1])    # TODO more testing!
      self.fall()
    else:
      print("Invalid input")
      self._storedBlock = block

width, height = 5, 7

"""
stores the highest block in the board. 
"""

if __name__ == "__main__":
  game = X2BlocksCloneCliImpl(width, height)
  game.play()

