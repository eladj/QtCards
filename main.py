# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui  import *
import cardstable
import random
      
        
class CardTableWidgetExtend(cardstable.cardTableWidget):
    """ extension of CardTableWidget """
    def __init__(self):
        super(CardTableWidgetExtend, self).__init__()

        
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # create widgets             
        self.label1 = QLabel("Bla Bla")
        self.label1.setFont(QFont('Andalus', 24))        
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setMaximumHeight(30)        
        self.label1.setStyleSheet("QLabel { background-color : blue; color : white; font: bold }")
        self.cardsTable = CardTableWidgetExtend()
        
        # main layout
        self.mainLayout = QVBoxLayout()
        
        # add all widgets to the main vLayout
        self.mainLayout.addWidget(self.label1)
        self.mainLayout.addWidget(self.cardsTable)
        
        # central widget
        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.mainLayout)        
#        
#        # set central widget
        self.setCentralWidget(self.centralWidget)
        
        # PLAYGROUND        
        self.cardsTable.dealDeck()
        #self.cardsTable.addCard('c_K')
        #self.cardsTable.getCardsList()[0].setPos(0,0)        
#        self.cardsTable.addCard('d_8')
#        self.cardsTable.addCard('j_r')
#        self.cardsTable.changeCard(1,'h_J', faceDown=True)
#        self.cardsTable.removeCard(51)
        
        self.cardsTable.getCardsList()               
#        self.cardsTable.deal1()

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.setWindowTitle("My Title")
    widget.setWindowIcon(QIcon('icon.png'))    
    widget.show()
    sys.exit(app.exec_())

