from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
from numpy import arange, sin, cos, pi
import pyqtgraph as pg
import sys

class Plot2D():
    def __init__(self, array):
        self.traces = dict()
        self.len = len(array[0])
        self.array = array
        #QtGui.QApplication.setGraphicsSystem('raster')
        self.app = QtGui.QApplication([])
        #mw = QtGui.QMainWindow()
        #mw.resize(800,800)

        self.win = pg.GraphicsWindow(title="Basic plotting examples")
        self.win.resize(1000,600)
        self.win.setWindowTitle('pyqtgraph example: Plotting')

        # Enable antialiasing for prettier plots
        pg.setConfigOptions(antialias=True)
        self.canvas = self.win.addPlot(title="Pytelemetry")

    def start(self):
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()

    def trace(self,name,dataset_y):
        if name in self.traces:
            self.traces[name].setData(range(self.len),dataset_y)
        else:
            self.traces[name] = self.canvas.plot(pen='y')




## Start Qt event loop unless running in interactive mode or using pyside.
# if __name__ == '__main__':
#     p = Plot2D()
#     i = 0

#     def update():
#         global p, i
#         p.trace("sin",p.array[i])
#         i += 1

#     timer = QtCore.QTimer()
#     timer.timeout.connect(update)
#     timer.start(50)

#     p.start()