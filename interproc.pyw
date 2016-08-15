#! /usr/bin/env python3
#

import sys
from PyQt4 import QtCore, QtGui
import interprocGUI
import socket

def main():
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('Demo')
    form = interprocGUI.interprocGUI()
    form.showMaximized()
    app.exec()

if __name__ == "__main__":
	sys.exit(main())
