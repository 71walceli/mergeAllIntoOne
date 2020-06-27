import MergeAllIntoOne
import wx

class wxBlock(wx.Button):
  def __init__(self, client, position, *args, **kwargs):
    self.position = position
    self.client = client
    #gameBlock = client.game.getGrid()[y][x]
    wx.Button.__init__(self, client, wx.ID_ANY, *args, **kwargs)
    self.update()

  def update(self):
    x, y = self.position[1], self.position[0]
    self.SetLabel(str(self.client.game.getGrid()[x][y])
      +" " + str(self.position)  # For debugging
    )

class wxClient(wx.Frame):
  def __init__(self, game, *args, **kwargs):
    self.game = game
    wx.Frame.__init__(self, *args, **kwargs)
    gameSizer = wx.BoxSizer(wx.VERTICAL)
    # TODO 7 Implement a function that can load the full grid representation.
    self.createGrid()
    gameSizer.Add(self.gamePanel, 0, wx.ALL, 10)
    #self.AddChild(gameSizer)

  def createGrid(self):
    self.gamePanel = wx.GridBagSizer(3, 3)
    for y in range(len(self.game.getGrid())):
      for x in range(len(self.game.getGrid()[y])):
        self.gamePanel.Add(wxBlock(self, (x,y)), pos=(x,y), span=(1,1), flag=wx.EXPAND)  # BUG 8 Only one of the buttons
        # actually show up, instead of showing all the tiles.


  def updateGrid(self):
    for y in range(self.game):
      for x in range(self.game[row]):
        pass

width, height = 5, 7

app = wx.App()
game = MergeAllIntoOne.MergeAllIntoOne(grid=(width, height))  
frame = wxClient(game, None, title="Hello World")
frame.Show()
app.MainLoop()
