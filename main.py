# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui  import *
import cardstable

# extending CardItem
class CardItem(cardstable.CardItem):
    def __init__(self, suit, rank, position, angle=0, scale=(1,1)):
        super(CardItem, self).__init__(suit, rank, position, angle, scale)
        self.name = suit + "_" + rank
        self.setAcceptHoverEvents(True) #by default it is set to False
        #self.setFlag(QGraphicsItem.ItemIsSelectable)
        #self.setFlag(QGraphicsItem.ItemIsMovable)
        
        
    # when mouse enter a card
    def hoverEnterEvent(self, event):
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(15)
        effect.setColor(Qt.blue)        
        effect.setOffset(QPointF(-5,0))
        self.setGraphicsEffect(effect)        
    
        
    def mousePressEvent(self, event):
        #self.update()
        print(self.name)
        #print(event.pos().x())
        #print(event.pos().y())
        #print(self.isSelected())
        self.animateMoveCardToPos(QPointF(300,300))        
        
        
        
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # create widgets             
        self.label1 = QLabel("Bla Bla")
        self.cardsTable = cardstable.cardTableWidget()

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
        
        #self.cardsTable.test2()
        defScaleX=0.5
        defScaleY=0.5
        c1 = CardItem('club','K',(10,10), scale=(defScaleX,defScaleY))
        c2 = CardItem('joker','',(100,10), scale=(defScaleX*1.197,defScaleY*1.03))
        c3 = CardItem('back','1',(10,100), scale=(defScaleX,defScaleY))
        self.cardsTable.addCard(c1)
        self.cardsTable.addCard(c2)
        self.cardsTable.addCard(c3)
     
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.resize(640, 480)
    widget.show()
    sys.exit(app.exec_())

