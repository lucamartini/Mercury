import wx
import MenuBar as MB

import analyzer.Analyzer as ana
import PanelTime
import PanelFFT


class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MainFrame, self).__init__(parent,
                                        title=title)
        self.openfiles = 0
        self.dirname = ''
        self.filename = ''

        self.Move((0, 0))
        self.Maximize()

        self.MMenuBar = MB.MMenuBar()
        self.SetMenuBar(self.MMenuBar.menuBar)

        self.initEvents()

        self.Show()

    def initEvents(self):
        self.Bind(wx.EVT_MENU, self.OnOpen, self.MMenuBar.menuOpen)
        self.Bind(wx.EVT_MENU, self.OnExit, self.MMenuBar.menuExit)
        self.Bind(wx.EVT_MENU, self.OnAbout, self.MMenuBar.menuAbout)

    def OnExit(self, e):
        self.Close(True)  # Close the frame.

    def OnAbout(self, e):
        # Create a message dialog box
        dlg = wx.MessageDialog(self, "Mercury System wav analyzer", "About Mercury System", wx.OK)
        dlg.ShowModal()  # Shows it
        dlg.Destroy()  # finally destroy it when finished.

    def OnOpen(self, e):
        """ Open a file"""
        dlg = wx.FileDialog(self, "Choose a wav file", self.dirname, "", "*.wav", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            print 'opening', self.filename, self.dirname
            self.analyzer = ana.Analyzer(self.dirname + '/' + self.filename)
            self.openfiles = self.openfiles + 1
            self.fftuple = self.analyzer.ms_tuple
        dlg.Destroy()

        print self.analyzer.data
        print self.fftuple

        self.panelTime = PanelTime.CanvasPanel(self, self.analyzer.data, self.analyzer.fs)
        self.panelTime.draw()

        self.panelFFT = PanelFFT.CanvasPanel(self, self.fftuple)
        self.panelFFT.draw()
        # self.panelFFT.Refresh()

        # self.SetSizerAndFit(self.sizer)

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.grid = wx.GridBagSizer(hgap=2, vgap=1)
        self.hSizer = wx.BoxSizer(wx.HORIZONTAL)

        #        if self.openfiles == 1:

        self.grid.Add(self.panelTime, pos=(0, 0))
        self.grid.Add(self.panelFFT, pos=(0, 1))
        self.hSizer.Add(self.grid, 0, wx.ALL, 2)
        self.mainSizer.Add(self.hSizer, 0, wx.ALL, 2)
        self.SetSizer(self.mainSizer)
        self.Fit()
#        self.Maximize()


if __name__ == '__main__':

    app = wx.App()
    MainFrame(None, title="Mercury System")
    app.MainLoop()
