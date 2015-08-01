from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy

import wx


class CanvasPanel(wx.Panel):
    def __init__(self, parent, data, fs):
        wx.Panel.__init__(self, parent)
        self.data = data
        t = numpy.array(range(len(data)))
        self.t = t/float(fs)

        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)

        self.canvas = FigureCanvas(self, -1, self.figure)

    def draw(self):
        self.axes.plot(self.t, self.data)
