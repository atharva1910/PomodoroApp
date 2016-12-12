from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QLCDNumber, QVBoxLayout, QBoxLayout
from PyQt5.QtCore import QTimer
import sys

# QApplication -> only one instance , manage events
# manages the GUI app control flow and main settings.\n"
# QWidget -> Base class for applicatios
# sys -> system module Gives system specific parameters and function
# QPushButton -> Button Class


class App(QWidget):
    """
    Main class of the app defines the window title,size atm.
    """
    def __init__(self):
        super().__init__()

        # set the window title
        self.title = 'Pomodoro'

        # set the window co-ords
        self.start = 10
        self.ht, self.wt = 200, 320
        self.number = 100

        # Create horizontal layout and buttons
        self.layout = QHBoxLayout()
        self.HorizontalLayout()

        # Create a lcd timer
        self.num = QLCDNumber()
#        self.LCDupdate()

        # Create a main vertial layout
        self.Vlayout = QVBoxLayout()
        self.Vlayout.addWidget(self.num)
        self.Vlayout.addLayout(self.layout)
        self.setLayout(self.Vlayout)

        # call the main function which will init the app
        self.initUI()

    def initUI(self):
        """
        Initialize the window with the parameters given in __init__
        """
        self.setWindowTitle(self.title)
        self.setGeometry(self.start, self.start, self.wt, self.ht)
        self.show()

    def HorizontalLayout(self):
        """
        Create a horizontal layout and add start and stop buttons
        """
        # Create the two buttons
        buttonStart = QPushButton('Start', self)
        buttonStop = QPushButton('Stop', self)

        # Add buttons to the layout
        self.layout.addWidget(buttonStart)
        self.layout.addWidget(buttonStop)

    def LCDupdate(self):
        """
        Call the update funtion to decrement the value and
        display the updated value
        """
        self.num.display(self.number)
        self.update()

    def update(self):
        """
        Update the timer on the LCDdisplay
        """
        if (self.number == 0):
            self.number = 100
        else:
            self.number -= 1


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # create a object of the class APP
    ex = App()
    sys.exit(app.exec_())
