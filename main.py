# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui  import *
import cardstable
import random
      
        
class cardTableWidgetExtend(cardstable.cardTableWidget):
    def __init__(self):
        super(cardTableWidgetExtend, self).__init__()
      

    def test2(self):
        types = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        x=100
        for name in types:
            item = CardItemExtend('club',name,(x,10),scale=0.7,
                                  svgFile=self.cardSvgFile('club',name))
            self.scene.addItem(item)
            x += 40
        #self.view.show()        
        
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # create widgets             
        self.label1 = QLabel("Bla Bla")
        self.cardsTable = cardTableWidgetExtend()

        # main layout
        self.mainLayout = QVBoxLayout()

        # add all widgets to the main vLayout
        self.mainLayout.addWidget(self.label1)
        self.mainLayout.addWidget(self.cardsTable)
        
        # central widget
        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.mainLayout)        
        
        # set central widget
        self.setCentralWidget(self.centralWidget)
        
        # PLAYGROUND        
        self.cardsTable.dealDeck()
#        self.cardsTable.addCard('c_K')
#        self.cardsTable.addCard('d_8')
#        self.cardsTable.cardsGraphItems[1].setPos(234,120)
#        self.cardsTable.addCard('j_r')
#        self.cardsTable.cardsGraphItems[2].setPos(234,80)
#        self.cardsTable.changeCard(1,'h_J', faceDown=True)
#        self.cardsTable.removeCard(1)
        
        self.cardsTable.getCardsList()               
#        self.cardsTable.deal1()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.resize(640, 480)
    widget.show()
    sys.exit(app.exec_())

