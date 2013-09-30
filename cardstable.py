from __future__ import print_function
import sys
import os
from PyQt4.QtCore import *
from PyQt4.QtGui  import *
from PyQt4 import QtSvg
import random

class cardTableWidget(QWidget):     
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)       
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 640, 480)
        self.view = QGraphicsView(self.scene)
        self.view.setRenderHint(QPainter.Antialiasing)        
        layout = QHBoxLayout()
        layout.addWidget(self.view)
        self.setLayout(layout)
        self.setBackgroundColor(QColor('green'))     
        self.cardsList = [] #holds all the cards items
        #self.test1()


    # add background color
    def setBackgroundColor(self, color):
        brush = QBrush(color)
        self.scene.setBackgroundBrush(brush)
        self.scene.backgroundBrush() 


    def cardSvgFile(self, suit, rank):
        path = "svg"        
        fn = os.path.join(path,suit + "_" + rank + ".svg")        
        return fn

        
    # adds CardItem to board    
    def addCard(self, CardItem):
        self.cardsList.append(CardItem)
        self.scene.addItem(self.cardsList[-1])        
        #print("num of cards=" + str(len(self.cardsList)))


    # removes card from board    
    def removeCard(self, cardIndex):
        self.scene.removeItem(self.cardsList[cardIndex])
        #print("num of cards=" + str(len(self.cardsList)))


    # replaces CardItem
    def changeCard(self, cardItemRemove, cardItemAdd):       
        cardItemAdd.setZValue(cardItemRemove.zValue())
        self.scene.removeItem(cardItemRemove)
        self.scene.addItem(cardItemAdd)

       

    def getCardsList(self):
        print("Cards List:")        
        for item in self.scene.items():
            try:
                print("Value= %3d, Name=%s" % (item.getValue(),item.getName()))
            except:
                pass


    def sortByRankAndValue(self):
        pass
        

    def buildCardDict(self,with_joker=False):
        suits = ['club','diamond','heart','spade']
        ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        n = 1
        d = dict()
        for suit in suits:
            for rank in ranks:
                d[n] = (suit,rank)
                n+=1
        if with_joker:
            d[n] = ('black','joker')
            n+=1 
            d[n] = ('red','joker')
        return d

    
    def dealDeck(self, numOfPlayes, numOfCardsToEach):
        random.randrange([1,52])

        
    def test1(self):
        c = CardItem('club','3',(50,5),-20)
        self.scene.addItem(c)
        c2 = CardItem('heart','Q',(200,100),100,1.5)
        self.scene.addItem(c2)
        
        
    def test2(self):
        types = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        x=100
        for name in types:
            self.scene.addItem(CardItem('club',name,(x,10),scale=0.7))
            x += 40
        #self.view.show()
    

class CardItem(QtSvg.QGraphicsSvgItem):
    def __init__(self, suit, rank, position, angle=0, scale=1, svgFile=None):
        super(CardItem, self).__init__(svgFile)        
        self.setPos(position[0],position[1])
        self.rotate(angle)
        self.setScale(scale)        
        self.suit = suit
        self.rank = rank
        self.pos = position
        self.angle = angle
        self.scale = scale
        #self.faceDown = faceDown   # set if card is showen or the back
        self.setAcceptHoverEvents(True) #by Qt default it is set to False
        #self.setFlag(QGraphicsItem.ItemIsMovable)      

        
       
    
    # return card value in number, by their rank
    def getValue(self):
        rank = self.rank
        if rank == 'joker':
            value = 99
        elif rank == 'A':
            value = 14
        elif rank == 'K':
            value = 13
        elif rank == 'Q':
            value = 12            
        elif rank == 'J':
            value = 11
        else:
            value = int(rank)        
        return value
            

    def getName(self):
        return self.suit + "_" + self.rank


    # FUTURE: change the card type
    def changeCardType(self, suit, rank):
        pass

    # when mouse enter a card
    def hoverEnterEvent(self, event):
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(15)
        effect.setColor(Qt.red)        
        effect.setOffset(QPointF(-5,0))
        self.setGraphicsEffect(effect)        
    
    
    # when mouse leaves a card    
    def hoverLeaveEvent(self, event):    
        self.setGraphicsEffect(None) 


    # move card to QPointF(x,y), without animation
    def moveCardToPos(self, QPointF):
        self.setPos(QPointF)


    # animate card to QPointF(x,y), with animation
    def animateCardToPos(self, QPointF):
        print('Animating..')               
        anim = QPropertyAnimation(self, 'pos')        
        anim.setDuration(150)
        #anim.setStartValue(self.pos())
        anim.setEndValue(QPointF)        
        #self.QObject.connect(anim, SIGNAL("finished()"), anim, SLOT("deleteLater()"))        
        anim.start() #QAbstractAnimation.DeleteWhenStopped)       
        anim.finished() #FUTURE - fix error message
        print('Finish animating..')

        
def main():
    app = QApplication(sys.argv)
    form = cardTableWidget()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()

