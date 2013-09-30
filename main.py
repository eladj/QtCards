# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui  import *
import cardstable
import random

# extending CardItem
class CardItemExtend(cardstable.CardItem):
    #def __init__(self, suit, rank, position, angle=0, scale=(1,1), svgFile=None):
        #super(CardItemExtend, self).__init__(suit, rank, position, angle, scale, svgFile=None)
        #self.setAcceptHoverEvents(True) #by Qt default it is set to False
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
        print(self.getName())
        #print(event.pos().x())
        #print(event.pos().y())
        #print(self.isSelected())
        self.animateCardToPos(QPointF(300,300))        
        
class cardTableWidgetExtend(cardstable.cardTableWidget):
    def __init__(self):
        super(cardTableWidgetExtend, self).__init__()
 
    # flips card faceDown
    def flipCard(self, cardItem, face='down'):
        if face=='down':
            tmp = CardItemExtend(cardItem.suit,cardItem.rank,cardItem.pos, 
                                 cardItem.angle, cardItem.scale,
                                 svgFile=self.cardSvgFile('back','1'))
        else:
            tmp = CardItemExtend(cardItem.suit,cardItem.rank,cardItem.pos, 
                                 cardItem.angle, cardItem.scale,
                                 svgFile=self.cardSvgFile(cardItem.suit,cardItem.rank))                                 
        self.changeCard(cardItem, tmp)       
        
    def deal1(self):
        defScale=0.5        
        d = self.buildCardDict()
        inds = range(1,53)
        random.shuffle(inds)
        positions = [(100,0),(5,100),(100,300),(300,0)]
        count = 0
        positionCounter = 0
        for n in inds:
            if count % 13 == 0:
                pos = positions[positionCounter]
                positionCounter+=1
                dx=0
            suit = d[n][0]
            rank = d[n][1]
            c = CardItemExtend(suit,rank,pos,scale=defScale, 
                                svgFile=self.cardSvgFile(suit,rank))
            c.setZValue(1)
            self.addCard(c)
            dx+=20
            count += 1
        
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
        
        #self.cardsTable.test2()      
        #self.cardsTable.changeCard(c2,c4)       
        #self.cardsTable.flipCard(c3, face='up')
        #self.cardsTable.removeCard(2)        
        #print(self.cardsTable.buildCardDict())        
        #self.cardsTable.scene.addRect(5,-50,140,140,QPen('black'))
        self.cardsTable.getCardsList()               
        self.cardsTable.deal1()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.resize(640, 480)
    widget.show()
    sys.exit(app.exec_())

