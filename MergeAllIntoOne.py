"""
X2 Block clone
https://play.google.com/store/apps/details?id=com.inspiredsquare.blocks

TODO 1 Add getters and setters
Version 0.3
"""

from random import randint  # Used by nextBlock()

class MergeAllIntoOne:
  """
  Command Line Interface implementation of X2BlocksClone

  
  Parameters
  ----------
  blockHighest : int
    Allows to set up to what number can be randomly generated.
  grid : list[list]
    The game area abstraction
    
  TODO 2 Document the rest of members!
  """

  def __init__(self, block_highest=5, grid=None):
    """
    Instances a new game. Constructs game grid of given `grid`.z
    """
    if isinstance(grid, tuple):
      self.__width = grid[0]
      self.__height = grid[1]
      self.__grid = [[0 for x in range(self.__width)] for y in range(self.__height)]
    else:
      self.__grid   = grid
      self.__width  = len(self.__grid[0])
      self.__height = len(self.__grid)

    # Other gameplay properties
    self.__block_highest = block_highest  # TODO implement logic to look for the
    # highest in the grid.
    self._storedBlock   = 0
    self.__score = 0
    
  def fall(self):
    """
    Makes the blocks fall into the empty spaces (the zeroes) until all blocks have
    fallen to the very bottom of the grid and stack one over others that are below
    in the same column.

    TODO Separate logic to make each column fall independently, as one column's
    falling is independent, except for merging.
    """

    for column in range(self.__width):
      blocksInColumn = [self.__grid[cell][column] for cell in range(self.__height) 
          if self.__grid[cell][column] != 0]  # get only actual blocks
      newColumn = blocksInColumn +[0 for zero in range(self.__height -len(blocksInColumn))]
      # Join blocksInColumn and fill the rest of the column with zeros as 
      # blocksInColumn already has all blocks filtered at the bottom.

      # assign the actual column from mewColumn
      for cell in range(self.__height):
        self.__grid[cell][column] = newColumn[cell]

  def howFullIsGrid(self):
    """
    return a percentage of how much of self.__grid is full, that is, all of its cells
    have non-zero values.
    """
    factor = 1 /(self.__width *self.__height)
    percentage = 0

    for row in self.__grid:
      for cell in row:
        if cell != 0:
          percentage += factor
    
    return round(percentage, 2)

  def isGridFull(self):
    """
    Checks if self.__grid is full by checking if the top-most row is full of blocks.
    """
    topmostRow = self.__height -1  # index fir topmost row
    count = self.__width

    for block in self.__grid[topmostRow]:
      if block != 0:
        count -= 1     # count down for every used space.
    return count == 0  # returns true if the top row is full.

  # unused
  def makeMerges(self, column):
    """
    Makes all the merges in a column happen. The merging occurs in this way:

    TODO Refactor this routine to do all possible merges in the given column
    """

  def merge(self, row, column):
    """
    Causes a block to merge as many times as it can and increments the score for
    every merge. The prosess by which this happens is the following:

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
    checkBlock  = self.__grid[row][column]
    if checkBlock == 0:
      return  # Merging doesn't happen if piece in this position is zero.
    
    mergedLeft  = self.mergeLeft (checkBlock, row, column)
    mergedRight = self.mergeRight(checkBlock, row, column)
    mergedDown  = self.mergeDown (checkBlock, row, column)

    self.__score += mergedLeft +mergedRight +mergedDown 
  
  def mergeLeft(self, checkBlock, row, column):
    """
    TODO Document this!
    """
    doable = column != 0 and self.__grid[row][column -1] == checkBlock 
    if doable:
      self.__grid[row][column]   += 1
      self.__grid[row][column -1] = 0
    return doable
    
  def mergeRight(self, checkBlock, row, column):
    """
    TODO Document this!
    """
    doable = column +1 != len(self.__grid[row]) and self.__grid[row][column +1] == checkBlock
    if doable:
      self.__grid[row][column]   += 1
      self.__grid[row][column +1] = 0
    return doable
    
  def mergeDown(self, checkBlock, row, column):
    """
    TODO Document this!
    """
    doable = row != 0 and self.__grid[row -1][column] == checkBlock
    if doable:
      actualBlock                = self.__grid[row][column] +1
      self.__grid[row -1][column] = actualBlock
      self.__grid[row][column]    = 0
      self.merge(row -1, column)
    return doable

  def nextBlock(self):
    """
    Generate next block to be shot

    TODO implement more dynamism according to the highest number there is in the
    grid.
    """
    #if self._storedBlock == 0:
    #  return randint(1, blockHighest)
    #return self._storedBlock
    if self._storedBlock != 0:
      return self._storedBlock
    return randint(1, self.__block_highest)

  def playTurn(self, column, block):
    """
    Contains all the game logic to play a game turn. It implements all the internalls
    from putting a piece to counting the score and handling errors. 
    """
    shotPosition = self.shoot(block, column)  # FIXME when block isn't shot, return
    # the previous one, to prevent the player from thowing away blocks.
    # TODO Improve self-arranging logic to fall() and merge() when it must
    if shotPosition != None:
      self.merge(shotPosition[0], shotPosition[1])
      self._storedBlock = 0
      self.__score += 1  # The score will be incremented for every block put in board.
    else:
      self._storedBlock = block
    self.fall()

  def shoot(self, block, column):
    """
    Puts blocks in the bottom most cell of the grid and returns the position where it
    was put.

    TODO Throw errors if given block could not be put.
    """
    row = -1  # Tracks what row to put blocks in. It is incremented in the following
    # loop.
    # _row os just an index to move though the column. The following loop stops when
    # it finds the bottom most empty spot to put block in.
    for _row in range(len(self.__grid)):
      row += 1
      if self.__grid[_row][column] == 0:
        break
    
    # Put the block in the bottom most blank
    if self.__grid[row][column] == 0:
      #self.__grid[row][column] == 0
      self.__grid[row][column] = block
      #self._storedBlock = 0
    elif self.__grid[row][column] == block:
      # XXX 5 Looks like this could be handled by self.mergedDown()
      self.__grid[row][column] += 1
      self.__score += 1
      #self._storedBlock = 0
    else:
      #self._storedBlock = block
      return None
      #self._storedBlock = block
      #raise ValueError("The column is full. Can't shoot!")
      # TODO: Throw custom exception for the game
    
    return (row, column)

  # Getters and fetters
  def getHeight(self): return self.__height
  def getHighestBlock (self): return self.__block_highest
  def getGrid(self): return self.__grid
  def getScore(self): return self.__score
  def getWidth(self): return self.__width
