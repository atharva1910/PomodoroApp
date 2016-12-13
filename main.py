from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QLCDNumber, QVBoxLayout
from PyQt5.QtCore import pyqtSlot, QTimer, QTime
import sys


class App(QWidget):
    """
    Main class of the app defines the window title,size and Layouts
    """
    def __init__(self):
        super().__init__()

        # set the window co-ords
        self.start = 10
        self.ht, self.wt = 200, 320
        self.number = 31*60
        self.hours = 00
        self.minutes = 31
        self.seconds = 00

        # Create Timer
        self.timer = QTimer()

        # Create horizontal layout and buttons
        self.Hlayout = QHBoxLayout()

        # Add Buttons to the HorizontalLayout
        self.addButtonsHlayout()

        # Create a lcd timer
        self.num = QLCDNumber()
        self.num.setNumDigits(8)

        # Create a main vertial layout
        self.Vlayout = QVBoxLayout()

        # Add LCDTimer to the layout
        self.Vlayout.addWidget(self.num)

        # Add HorizontalLayout to Layout
        self.Vlayout.addLayout(self.Hlayout)

        # Set the layout of the App
        self.setLayout(self.Vlayout)

        # call the main function which will init the app
        self.initUI()

    def initUI(self):
        """
        Initialize the window with the parameters given in __init__
        """
        self.setWindowTitle("Pomodoro")
        self.setGeometry(self.start, self.start, self.wt, self.ht)
        self.show()

    def addButtonsHlayout(self):
        """
        Add Buttons to the horizontal layout
        """
        # Create the two buttons
        buttonStart = QPushButton('Start', self)
        buttonStop = QPushButton('Stop', self)

        # buttonClicked
        buttonStart.clicked.connect(self._startClicked)
        buttonStop.clicked.connect(self._stopClicked)

        # Add buttons to the layout
        self.Hlayout.addWidget(buttonStart)
        self.Hlayout.addWidget(buttonStop)

    def updateLCD(self):
        """
        Update the timer on the LCDdisplay
        """
        self.num.display(str(self.minutes) + ":" + str(self.seconds).zfill(2))
        if(self.number != 0):
            self.timer.singleShot(1000, self.updateLCD)

    @pyqtSlot()
    def _startClicked(self):
        """
        When Button is clicked Start the countDown
        """
        self.timer.singleShot(1000, self.updateLCD)

    @pyqtSlot()
    def _stopClicked(self):
        """
        When stop Button is clicked exit app
        """
        sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # create a object of the class APP
    ex = App()

    # Execute the App
    sys.exit(app.exec_())
