"""
Holds all the test logic to ensore the game and all its components work as expected.
"""

import unittest
from random import randint

import MergeAllIntoOne


class BaseTestLogic(unittest.TestCase):
  def play(self, block, column):
    """
    Play a turn for testing purposes. Lets exceptions spread, which the main game loop should
    handle and act accordingly.
    """
    self.game.playTurn(column, block)
  
  def mergingDown1(self):
    column = 0
    self.play(1, column)
    self.play(1, column)

  def mergingAtTop1(self):
    """
    Initial state:

    ```
    0 0 0 1 0
    0 0 0 2 0
    0 0 0 1 0
    0 0 0 2 0
    0 0 0 1 0
    0 0 0 2 0
    0 0 0 3 0
          ^
          3
    ```
    """
    column = 3
    self.play(1, column)
    self.play(2, column)
    self.play(1, column)
    self.play(2, column)
    self.play(1, column)
    self.play(2, column)
    self.play(3, column)  # stack at top of grid
    self.play(3, column)  # shoot and merge. This is expected to work.

  def mergeAndFall2(self):
    self.play(3, 2)
    self.play(1, 2)
    self.play(2, 2)
    self.play(3, 1)

  def multipleMerge2(self):
    """
    Initial state:

    ```
    0 7 4 7 0
    0 4 4 4 0
    0 1 0 1 0
    0 0 0 0 0
    0 0 0 0 0
    0 0 0 0 0
    0 0 0 0 0
    ```
    """
    self.play(7, 1)
    self.play(4, 1)
    self.play(1, 1)
    self.play(7, 3)
    self.play(4, 3)
    self.play(1, 3)
    self.play(4, 2)
    self.play(4, 2)

  def setUp(self):
    self.game = MergeAllIntoOne.MergeAllIntoOne(width, height)

  #def tearDown(self):
  #  self.MergeAllIntoOne.printGrid()

class IsGridFullTest(BaseTestLogic):
  def setUp(self):
    grid = [[randint(1, 9) for x in range(width)] for y in range(height)]
    self.game = MergeAllIntoOne.MergeAllIntoOne(0, 0, grid=grid)

  def test_isGridFull1(self):
    self.assertTrue(self.game.isGridFull())

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
    self.mergingDown1()
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
    self.mergingAtTop1()
    expected = [
      [0,0,0,1,0],
      [0,0,0,2,0],
      [0,0,0,1,0],
      [0,0,0,2,0],
      [0,0,0,1,0],
      [0,0,0,2,0],
      [0,0,0,4,0]
    ]
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
    self.mergeAndFall2()
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
    self.multipleMerge2()
    self.assertEquals(self.game._grid[0], expectedBottomRow)
    
class MiscGameplayTesting(BaseTestLogic):
  def test_blockNotThrownAwayIfNotPut(self):
    self.play(1, 2)
    self.play(2, 2)
    self.play(3, 2)
    self.play(4, 2)
    self.play(5, 2)
    self.play(6, 2)
    self.play(7, 2)
    self.play(8, 2)
    self.assertEquals(self.game.nextBlock(), 8)

class ScoreTests(BaseTestLogic):
  def test_ScoreAfterMerging1(self):
    self.mergingAtTop1()
    self.assertEqual(self.game._score, 9)
  
  def test_ScoreAfterMerging2(self):
    self.mergeAndFall2()
    self.assertEqual(self.game._score, 5)

  def test_ScoreAfterMerging3(self):
    self.multipleMerge2()
    self.assertEqual(self.game._score, 13)

  def test_ScoreAfterPuttingBlocks(self):
    blocks = 10
    for block in range(blocks):
      self.game.playTurn(randint(0, 4), block)
    self.assertEqual(self.game._score, blocks)
  

width, height = 5, 7

if __name__ == "__main__":
  unittest.main()
