import unittest
import game

def play(gameGrid, block, column):
  """
  Play a turn for testing purposes. Lets exceptions spread, which the main game loop should
  handle and act accordingly.
  """
  if column in range(width):  # range() domain is [0, width -1]
    game.shoot(gameGrid, block, column)
    game.makeMerges(gameGrid, column)  # testing needed!
    game.fall(gameGrid)
  else:
    raise IndexError(f"Invalid column index: {column}")

class MergingTest(unittest.TestCase):
  def setUp(self):
    self.gameGrid = game.buildGameGrid(width, height)

  def test_mergingDown1(self):
    column = 0
    play(self.gameGrid, 1, column)
    play(self.gameGrid, 1, column)
    self.assertEqual(self.gameGrid[0][column], 2)
  
  def test_mergingDown2(self):
    column = 2
    play(self.gameGrid, 1, column)
    play(self.gameGrid, 1, column)
    self.assertEqual(self.gameGrid[0][column], 2)
  
  def test_mergingDown3(self):
    column = 4
    play(self.gameGrid, 1, column)
    play(self.gameGrid, 1, column)
    self.assertEqual(self.gameGrid[0][column], 2)
  
  def test_mergingAtTop3(self):
    column = 3
    play(self.gameGrid, 1, column)
    play(self.gameGrid, 2, column)
    play(self.gameGrid, 1, column)
    play(self.gameGrid, 2, column)
    play(self.gameGrid, 1, column)
    play(self.gameGrid, 2, column)
    play(self.gameGrid, 3, column)  # stack at top of grid
    play(self.gameGrid, 3, column)  # shoot and merge. This is wanted to work
    self.assertEqual(self.gameGrid[6][column], 4)

  def test_mergeAndFall1(self):
    expectedOutcome = [
        [0,4,1,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
      ]
    play(self.gameGrid, 3, 2)
    play(self.gameGrid, 1, 2)
    play(self.gameGrid, 3, 1)
    self.assertEqual(self.gameGrid, expectedOutcome)
  
  def test_mergeAndFall2(self):
    expectedOutcome = [
        [0,4,1,0,0],
        [0,0,2,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
      ]
    play(self.gameGrid, 3, 2)
    play(self.gameGrid, 1, 2)
    play(self.gameGrid, 2, 2)
    play(self.gameGrid, 3, 1)
    self.assertEqual(self.gameGrid, expectedOutcome)

  def tearDown(self):
    print()
    game.printGrid(self.gameGrid)
    
width, height = 5, 7

if __name__ == "__main__":
  unittest.main()
