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
        #self.scene.setSceneRect(0, 0, 640, 480)
        self.view = QGraphicsView(self.scene)
        self.view.setRenderHint(QPainter.Antialiasing)        
        layout = QHBoxLayout()
        layout.addWidget(self.view)
        self.setLayout(layout)
        self.setBackgroundColor(QColor('green'))     
        # special properties
        self.svgCardsPath = "svg"
        self.cardsList = [] #holds all the cards names
        self.cardsGraphItems = [] #holds all the cards items
        self.defInsertionPos = QPointF(0,0)
        self.defAngle = 0
        self.defScale = 0.7
        self.deckBackSVG = 'back_1'
        self.numOfPlayers = 4
        self.playersHandsPos = [(-300,150,90),(-100,0,180),(300,100,270),(-100,300,0)] #(x,y,angle)
        self.defHandSpacing = 24
        #self.test1()


    # add background color
    def setBackgroundColor(self, color):
        brush = QBrush(color)
        self.scene.setBackgroundBrush(brush)
        self.scene.backgroundBrush() 


    def cardSvgFile(self, name):
        """ get card svg file from card name 
        name = 'c_4','d_Q',...
        for jokers name = 'j_r' or 'j_b'
        for back name = 'back_1', 'back_2', ...
        """
        fn = os.path.join(self.svgCardsPath,name + ".svg")        
        return fn

            
    def addCard(self, name, faceDown=False, player=0):
        """ adds CardGraphicsItem graphics to board.
        also updates the total cards list
        """        
        # svg file of the card graphics
        if faceDown:
            svgFile = self.cardSvgFile(self.deckBackSVG)            
        else:
            svgFile = self.cardSvgFile(name)
        
        self.cardsList.append(CardItem(name,self.value(name),player,faceDown))
        ind = len(self.cardsGraphItems) + 1
        position = self.defInsertionPos
        angle = self.defAngle        
        scale = self.defScale
        tmp = CardGraphicsItem(name, ind, position, svgFile, angle, scale)
        tmp.setZValue(ind) # set ZValue as index (last in is up)
        self.cardsGraphItems.append(tmp)
        self.scene.addItem(self.cardsGraphItems[-1])
        
        # sanity check
        self.checkLists()

        #print("num of cards=" + str(len(self.cardsList)))

    def removeCard(self, cardIndex):
        """ removes CardGraphicsItem graphics from board 
        also removes from the total cards list
        """
        self.scene.removeItem(self.cardsGraphItems[cardIndex])
        self.cardsGraphItems.pop(cardIndex)        
        self.cardsList.pop(cardIndex)
        self.checkLists()
        #print("num of cards=" + str(len(self.cardsList)))


    # replaces CardGraphicsItem
    def changeCard(self, cardIndRemove, nameToAdd, faceDown=False):       
        """ replace CardGraphicsItem         
        keeps same index and ZValue !
        """
        
        zValueTmp = self.cardsGraphItems[cardIndRemove].zValue()
        position = self.cardsGraphItems[cardIndRemove].pos()
        angle = self.cardsGraphItems[cardIndRemove].rotation()
        scale = self.cardsGraphItems[cardIndRemove].scale()
        self.scene.removeItem(self.cardsGraphItems[cardIndRemove])
        self.cardsGraphItems.pop(cardIndRemove)
        player = self.cardsList[cardIndRemove].player
        self.cardsList.pop(cardIndRemove)

        # svg file of the card graphics
        if faceDown:
            svgFile = self.cardSvgFile(self.deckBackSVG)            
        else:
            svgFile = self.cardSvgFile(nameToAdd)

        ind = cardIndRemove
        self.cardsList.insert(ind,CardItem(nameToAdd,self.value(nameToAdd),player,faceDown))        
        tmp = CardGraphicsItem(nameToAdd, ind, position, svgFile, angle, scale)
        tmp.setZValue(zValueTmp) # set ZValue as previous
        self.cardsGraphItems.insert(ind, tmp)
        self.scene.addItem(self.cardsGraphItems[ind])
        self.checkLists()


    def checkLists(self):
        """ sanity check """
        if len(self.cardsList) != len(self.cardsGraphItems):
            print("WARNING !!! -> cardsList != cardsGraphItems")


    def getCardsList(self):
        """ prints cards list """
        print("Cards List:")
        n=1
        for item in self.cardsList:
            print("Ind=%3d | Name=%4s | Value= %3d | Player=%d | faceDown=%r " % \
                 (n, item.name, item.value, item.player, item.faceDown) )
            n += 1


    def suit(self, name):
        """ get card suit type """    
        return name.split("_")[0]
    
    
    def rank(self, name):    
        """ get card rank type """        
        return name.split("_")[1]
        
    
    def value(self, name):        
        """ return card value in number, by their rank """
        if self.suit(name)=='j':
            return 99
        rank = self.rank(name)
        if rank == 'A':
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
        

    def buildDeckList(self,with_joker=False):
        suits = ['c','d','h','s']
        ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        l = list()
        for suit in suits:
            for rank in ranks:
                l.append(suit + '_' + rank)
        if with_joker:
            l.append('j_b')
            l.append('j_r')            
        return l

    
    def dealDeck(self):
        d = self.buildDeckList()        
        random.shuffle(d)
        print(d)
        playerNum=1
        n=1
        c2=0
        dx = [0,self.defHandSpacing,0,self.defHandSpacing]
        dy = [self.defHandSpacing,0,self.defHandSpacing,0]        
        x, y, ang = self.playersHandsPos[playerNum-1]
        for card in d:            
            self.addCard(card,player=playerNum)
            self.cardsGraphItems[-1].setPos(x+dx[playerNum-1]*c2,
                                            y+dy[playerNum-1]*c2)
            self.cardsGraphItems[-1].rotate(ang)
            if n % (52 / self.numOfPlayers) == 0:
                playerNum += 1                
                if playerNum > self.numOfPlayers:
                    break
                x, y, ang = self.playersHandsPos[playerNum-1]
                c2=0
            n += 1
            c2 += 1

        
    def test1(self):
        c = CardGraphicsItem('club','3',(50,5),-20)
        self.scene.addItem(c)
        c2 = CardGraphicsItem('heart','Q',(200,100),100,1.5)
        self.scene.addItem(c2)
        
        
    def test2(self):
        types = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        x=100
        for name in types:
            self.scene.addItem(CardGraphicsItem('club',name,(x,10),scale=0.7))
            x += 40
        #self.view.show()
    

class CardGraphicsItem(QtSvg.QGraphicsSvgItem):
    """ Extends QtSvg.QGraphicsSvgItem for card items graphics """ 
    def __init__(self, name, ind, position, svgFile, angle=0, scale=1):
        super(CardGraphicsItem, self).__init__(svgFile)
        # special properties
        self.name = name        
        self.ind = ind
        self.svgFile = svgFile
        # default QGraphicsSvgItem properties
        self.setPos(position)
        self.rotate(angle)
        self.setScale(scale)        
        self.setAcceptHoverEvents(True) #by Qt default it is set to False
        #self.setFlag(QGraphicsItem.ItemIsMovable)              
       
    
    def getSuit(self):
        """ get card suit type """    
        return self.name.split("_")[0]
    
    
    def getRank(self):    
        """ get card rank type """        
        return self.name.split("_")[1]
        
    
    def getValue(self):        
        """ return card value in number, by their rank """
        if self.getSuit()=='j':
            return 99
        rank = self.getRank()
        if rank == 'A':
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

    
    def hoverEnterEvent(self, event):
        """ event when mouse enter a card """    
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(15)
        effect.setColor(Qt.red)        
        effect.setOffset(QPointF(-5,0))
        self.setGraphicsEffect(effect)        
    
      
    def hoverLeaveEvent(self, event):
        """ event when mouse leave a card """    
        self.setGraphicsEffect(None) 


    def moveToPos(self, QPointF):
        """ move card to QPointF(x,y), without animation """    
        self.setPos(QPointF)


    def animateCardToPos(self, QPointF):
        """ animate card to QPointF(x,y), with animation """    
        print('Animating..')               
        anim = QPropertyAnimation(self, 'pos')        
        anim.setDuration(150)
        #anim.setStartValue(self.pos())
        anim.setEndValue(QPointF)        
        #self.QObject.connect(anim, SIGNAL("finished()"), anim, SLOT("deleteLater()"))        
        anim.start() #QAbstractAnimation.DeleteWhenStopped)       
        anim.finished() #FUTURE - fix error message
        print('Finish animating..')

class CardItem(object):
    """ holds cards item logical details (no graphics here) """
    def __init__(self, name, value, player=0, faceDown=False):
        self.name = name
        self.value = value
        self.player = player
        self.faceDown = faceDown        
        
        
def main():
    app = QApplication(sys.argv)
    form = cardTableWidget()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()

