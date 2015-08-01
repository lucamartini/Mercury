import wx


class MMenuBar(wx.MenuBar):
    def __init__(self):
        filemenu = wx.Menu()
        self.menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", " Open a wav file to analyze")
        self.menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program")
        self.menuExit = filemenu.Append(wx.ID_EXIT, "E&xit", " Terminate the program")
        self.menuBar = wx.MenuBar()
        self.menuBar.Append(filemenu, "&File")  # Adding the "filemenu" to the MenuBar


if __name__ == '__main__':

    app = wx.App()
    MMenuBar()
