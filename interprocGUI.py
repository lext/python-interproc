from PyQt4 import QtCore, QtGui, uic
import os
from time import gmtime, strftime
import socket



class interprocGUI(QtGui.QMainWindow):

    def __init__(self):
        # UI
        super(interprocGUI, self).__init__()
        uic.loadUi("GUI.ui", self)

        self.pbSendCmd.clicked.connect(self.send_cmd_slot)

    def send_cmd_slot(self):
        try:
            clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientsocket.connect(('localhost', 8080))
            res = clientsocket.recv(2)
            if res.decode('utf-8') == 'CN':
                self.teLog.appendPlainText('['+strftime("%Y-%m-%d %H:%M:%S", gmtime())+'] '+'Connected.')
            else:
                raise ValueError('Wrong response from the remote component')
            
            clientsocket.send(self.leCmd.text().encode())
            self.teLog.appendPlainText('['+strftime("%Y-%m-%d %H:%M:%S", gmtime())+'] '+'Command '+self.leCmd.text()+' has been sent.')
            res = clientsocket.recv(2)
            if len(res) > 0:
                self.teLog.appendPlainText('['+strftime("%Y-%m-%d %H:%M:%S", gmtime())+'] '+'Command has been executed.')
            clientsocket.close()
        except Exception as e:
            msgbox = QtGui.QMessageBox();
            msgbox.setText(str(e))
            self.teLog.appendPlainText('['+strftime("%Y-%m-%d %H:%M:%S", gmtime())+'] '+str(e))
            msgbox.exec()
    
