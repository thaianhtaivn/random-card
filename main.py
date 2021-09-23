# Application for controlling Relay box 4 channel
# THT5HC

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import datetime
import random
import time
# GUI FILE
from ui_main import Ui_MainWindow
import threading
import openpyxl
# IMPORT FUNCTIONS

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.thread = None
        self.alive = threading.Event()
        self.GenerateThread = threading.Thread(target=self.GenerateThread)

        ## REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.excel_file = 'data.xlsx'
        self.topic = 0

        wb = openpyxl.load_workbook(self.excel_file)
        sheet = wb['Sheet1']
        self.data = [[cell.value for cell in row] for row in sheet]
        

        self.show()
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.updateUI)
        self.timer.start()
        

        self.StartGenerateThread()

        # MINIMIZE
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())
        # CLOSE APPLICATION
        self.ui.closeAppBtn.clicked.connect(lambda: self.close())
        # SETTING
        self.ui.settingsTopBtn.clicked.connect(lambda:self.random_generate_topic())
        # self.ui.card_1.hide()

        # MOVE WINDOW
        self.ui.title_bar.mouseMoveEvent = self.moveWindow


        #  READ DATA FILE (EXCEL)

    def updateUI(self):
        self.ui.label_time.setText(datetime.datetime.now().strftime("%I:%M:%S %p"))
        
    
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def moveWindow(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()
    
    def random_generate_topic(self, topic=100):
        # self.read_data(self.excel_file)
        self.topic = len(self.data)
            
    def StartGenerateThread(self):
        """Start the receiver thread"""
        
        self.GenerateThread.setDaemon(1)
        self.alive.set()
        self.GenerateThread.start()

        print ('Start Thread')

    def StopGenerateThread(self):
        """Stop the receiver thread, wait until it's finished."""
        if self.GenerateThread is not None:
            self.alive.clear()          # clear alive event for thread
            self.GenerateThread = None
            print('StopThread --> Note: Notworking')
        else:
            print('No Thread')
    
    def GenerateThread(self):
        while True:
            if(self.topic>0):
                font = QtGui.QFont()
                # font.setFamily("Verdana")
                font.setPointSize(30)
                # font.setBold(False)
                self.ui.label_number.setFont(font)
                self.ui.label_number.setStyleSheet("QLabel{\n""color: rgba(52, 225, 55, 206);\n""background-color: none;\n""}")
                for i in range(4):
                    self.display_topic()
                    time.sleep(0.3)

                for i in range(10):
                    self.display_topic()
                    time.sleep(0.1)

                for i in range(6):
                    self.display_topic()
                    time.sleep(i/10)

                time.sleep(0.2)
                self.display_topic()
                font.setPointSize(45)
                # font.setBold(False)
                self.ui.label_number.setFont(font)
                self.ui.label_number.setStyleSheet("QLabel{\n""color: rgb(255, 15, 55);\n""background-color: none;\n""}")

                self.topic=0

    def display_topic(self):
        number = random.randint(1, self.topic-1)
        self.ui.label_number.setText(str(number))
        self.ui.label_card_1.setText(str(self.data[number][1]))


    def read_data(self, path):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())