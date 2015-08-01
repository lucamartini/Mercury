#!/usr/bin/python

import frame.MercuryFrame as mf

app = mf.wx.App(False)
mercury = mf.MainFrame(None, "Mercury System")
app.MainLoop()
