"""
Golds all the test logic to ensore the game and all its components work as expected.

TODO Refactor all test logic to support objects.
"""

from random import randint
import unittest
import game


class BaseTestLogic(unittest.TestCase):
  def play(self, gameGrid, block, column):
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
  
  def setUp(self):
    self.gameGrid = game.buildGameGrid(width, height)

  def tearDown(self):
    print()
    game.printGrid(self.gameGrid)

class MergeTesting(BaseTestLogic):
  def test_mergingDown1(self):
    column = 0
    self.play(self.gameGrid, 1, column)
    self.play(self.gameGrid, 1, column)
    self.assertEqual(self.gameGrid[0][column], 2)
  
  def test_mergingDown2(self):
    column = 2
    self.play(self.gameGrid, 1, column)
    self.play(self.gameGrid, 1, column)
    self.assertEqual(self.gameGrid[0][column], 2)
  
  def test_mergingDown3(self):
    column = 4
    self.play(self.gameGrid, 1, column)
    self.play(self.gameGrid, 1, column)
    self.assertEqual(self.gameGrid[0][column], 2)
  
  def test_mergingAtTop1(self):
    column = 3
    self.play(self.gameGrid, 1, column)
    self.play(self.gameGrid, 2, column)
    self.play(self.gameGrid, 1, column)
    self.play(self.gameGrid, 2, column)
    self.play(self.gameGrid, 1, column)
    self.play(self.gameGrid, 2, column)
    self.play(self.gameGrid, 3, column)  # stack at top of grid
    self.play(self.gameGrid, 3, column)  # shoot and merge. This is wanted to work
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
    self.play(self.gameGrid, 3, 2)
    self.play(self.gameGrid, 1, 2)
    self.play(self.gameGrid, 3, 1)
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
    self.play(self.gameGrid, 3, 2)
    self.play(self.gameGrid, 1, 2)
    self.play(self.gameGrid, 2, 2)
    self.play(self.gameGrid, 3, 1)
    self.assertEqual(self.gameGrid, expectedOutcome)

  def test_multipleMerge1(self):
    self.play(self.gameGrid, 7, 1)
    self.play(self.gameGrid, 4, 1)
    self.play(self.gameGrid, 7, 3)
    self.play(self.gameGrid, 4, 3)
    self.play(self.gameGrid, 4, 2)
    self.play(self.gameGrid, 4, 2)
    self.assertEquals(self.gameGrid[0][2], 9)
  
  def test_multipleMerge2(self):
    expectedBottomRow = [0,1,9,1,0]
    self.play(self.gameGrid, 7, 1)
    self.play(self.gameGrid, 4, 1)
    self.play(self.gameGrid, 1, 1)
    self.play(self.gameGrid, 7, 3)
    self.play(self.gameGrid, 4, 3)
    self.play(self.gameGrid, 1, 3)
    self.play(self.gameGrid, 4, 2)
    self.play(self.gameGrid, 4, 2)
    self.assertEquals(self.gameGrid[0], expectedBottomRow)
    
class miscGameplayTesting(BaseTestLogic):
  class IsGridFullTest(BaseTestLogic):
    def setUp(self):
      pass

    def test_isGridFull1(self):
      self.gameGrid = [[randint(1, 9) for x in range(width)] for y in range(height)]
      self.assertTrue(game.isGridFull(self.gameGrid))

    def tearDown(self):
      pass

  def test_nextBlockIsNotThrownIfNotPut(self):
    self.play(self.gameGrid, 1, 2)
    self.play(self.gameGrid, 2, 2)
    self.play(self.gameGrid, 3, 2)
    self.play(self.gameGrid, 4, 2)
    self.play(self.gameGrid, 5, 2)
    self.play(self.gameGrid, 6, 2)
    self.play(self.gameGrid, 7, 2)
    self.assertEquals(game.blockTemp, 7)
    

width, height = 5, 7


if __name__ == "__main__":
  unittest.main()
