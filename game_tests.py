"""
Holds all the test logic to ensore the game and all its components work as expected.

TODO Refactor all test logic to support objects.
"""

from random import randint
import unittest
import game


class BaseTestLogic(unittest.TestCase):
  def play(self, block, column):
    """
    Play a turn for testing purposes. Lets exceptions spread, which the main game loop should
    handle and act accordingly.
    """
    if column in range(width):  # range() domain is [0, width -1]
      shotPosition = self.game.shoot(block, column)
      if shotPosition != None:
        self.game.merge(shotPosition[0], shotPosition[1])  # testing needed!
      self.game.fall()
    else:
      raise IndexError(f"Invalid column index: {column}")
  
  def setUp(self):
    self.game = game.X2BlocksCloneCliImpl(width, height)

  def tearDown(self):
    self.game.printGrid()

class MergeTesting(BaseTestLogic):
  def test_mergingDown1(self):
    expected = [
      [2,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0]
    ]
    column = 0
    self.play(1, column)
    self.play(1, column)
    self.assertEqual(self.game._grid, expected)
  
  def test_mergingDown2(self):
    column = 2
    self.play(1, column)
    self.play(1, column)
    self.assertEqual(self.game._grid[0][column], 2)
  
  def test_mergingDown3(self):
    column = 4
    self.play(1, column)
    self.play(1, column)
    self.assertEqual(self.game._grid[0][column], 2)
  
  def test_mergingAtTop1(self):
    column = 3
    """
    Initial state:

    0 0 0 1 0
    0 0 0 2 0
    0 0 0 1 0
    0 0 0 2 0
    0 0 0 1 0
    0 0 0 2 0
    0 0 0 3 0
          ^
          3
    """
    expected = [
      [0,0,0,1,0],
      [0,0,0,2,0],
      [0,0,0,1,0],
      [0,0,0,2,0],
      [0,0,0,1,0],
      [0,0,0,2,0],
      [0,0,0,4,0]
    ]
    self.play(1, column)
    self.play(2, column)
    self.play(1, column)
    self.play(2, column)
    self.play(1, column)
    self.play(2, column)
    self.play(3, column)  # stack at top of grid
    self.play(3, column)  # shoot and merge. This is wanted to work
    self.assertEqual(self.game._grid, expected)

  def test_mergeAndFall1(self):
    expected = [
        [0,4,1,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
      ]
    self.play(3, 2)
    self.play(1, 2)
    self.play(3, 1)
    self.assertEqual(self.game._grid, expected)
  
  def test_mergeAndFall2(self):
    expected = [
        [0,4,1,0,0],
        [0,0,2,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
      ]
    self.play(3, 2)
    self.play(1, 2)
    self.play(2, 2)
    self.play(3, 1)
    self.assertEqual(self.game._grid, expected)

  def test_multipleMerge1(self):
    self.play(7, 1)
    self.play(4, 1)
    self.play(7, 3)
    self.play(4, 3)
    self.play(4, 2)
    self.play(4, 2)
    self.assertEquals(self.game._grid[0][2], 9)
  
  def test_multipleMerge2(self):
    expectedBottomRow = [0,1,9,1,0]
    self.play(7, 1)
    self.play(4, 1)
    self.play(1, 1)
    self.play(7, 3)
    self.play(4, 3)
    self.play(1, 3)
    self.play(4, 2)
    self.play(4, 2)
    self.assertEquals(self.game._grid[0], expectedBottomRow)
    
class miscGameplayTesting(BaseTestLogic):
  def test_highestBlockLogic1(self):
    self.play(1, 2)
    self.play(2, 2)
    self.play(3, 2)
    self.play(4, 2)
    self.play(5, 2)
    self.play(6, 2)
    self.play(7, 2)
    self.assertEquals(self.game._block_highest, 7)
    
class IsGridFullTest(BaseTestLogic):
  def setUp(self):
    grid = [[randint(1, 9) for x in range(width)] for y in range(height)]
    self.game = game.X2BlocksCloneCliImpl(0, 0, grid=grid)

  def test_isGridFull1(self):
    self.assertTrue(self.game.isGridFull())


width, height = 5, 7

if __name__ == "__main__":
  unittest.main()
