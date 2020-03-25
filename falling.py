"""
Development program for falling logic.

Here are the bare minimun dependencies for the grid.
"""
def fall(_gameGrid):
  """
  Makes the blocks fall into the empty spaces (the zeroes) until all blocks have
  fallen to the very bottom of the grid and stack one over others that are below
  in the same column.
  """
  for row1 in range(len(_gameGrid) -1, 0, -1):
    row2 = row1 -1  # row1 is at the top- while row2 is closer to the bottom.
    for column in range(len(_gameGrid[row1])):
      if _gameGrid[row1][column] != 0 and _gameGrid[row2][column] == 0:
        _gameGrid[row2][column] = _gameGrid[row1][column]  # copy block downward
        _gameGrid[row1][column] = 0           # put a space in its previous place.

def buildGameGrid(_width: int, _height: int):
  """
  Constructs game grid of given _width and _height
  """
  return [[0 for x in range(_width)] for y in range(_height)] 

def printGrid(_gameGrid):
  for row in _gameGrid:
    for cell in row:
      print(cell, end=" ")
    print()
  print()

def shoot(_gameGrid, _block, _aim):
  _gameGrid[height -1][_aim] = _block

width, height = 5, 7
gameGrid = buildGameGrid(width, height)


shoot(gameGrid, 1, 2)
fall(gameGrid)
shoot(gameGrid, 2, 2)
fall(gameGrid)
shoot(gameGrid, 3, 4)
fall(gameGrid)
shoot(gameGrid, 4, 4)
fall(gameGrid)
shoot(gameGrid, 5, 0)
fall(gameGrid)
shoot(gameGrid, 6, 1)
fall(gameGrid)
shoot(gameGrid, 7, 3)
fall(gameGrid)
printGrid(gameGrid)    # It shown how this is WORKING.
