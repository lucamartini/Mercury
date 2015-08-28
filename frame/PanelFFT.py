from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure

import wx


class CanvasPanel(wx.Panel):
    def __init__(self, parent, fftuple):
        wx.Panel.__init__(self, parent)
        self.fftuple = fftuple

        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)

        self.canvas = FigureCanvas(self, -1, self.figure)

    def draw(self):
        # self.axes.set_yscale('log')
        self.axes.plot(self.fftuple[1], self.fftuple[0], 'r')


if __name__ == '__main__':

    app = wx.App()
    PanelDummyParent = wx.Frame(None)
    fftuple = [0, 1]

    CanvasPanel(PanelDummyParent, fftuple)
