from PyQt4 import QtCore, QtGui, uic
import os
from time import time


class interprocGUI(QtGui.QMainWindow):

    def __init__(self):
        # UI
        super(interprocGUI, self).__init__()
        uic.loadUi("GUI.ui", self)

