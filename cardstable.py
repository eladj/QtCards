# -*- coding: utf-8 -*-
import sys
import os
from PyQt4.QtCore import *
from PyQt4.QtGui  import *
from PyQt4 import QtSvg


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
    
    def addCard(self, CardItem):
        self.cardsList.append(CardItem)
        self.scene.addItem(self.cardsList[-1])
        #self.update()
        print "num of cards=" + str(len(self.cardsList))
        
        
    def test1(self):
        c = CardItem('club','3',(50,5),-20)
        self.scene.addItem(c)
        c2 = CardItem('heart','Q',(200,100),100,(1.5,1.5))
        self.scene.addItem(c2)
        
        
    def test2(self):
        types = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        x=100
        for name in types:
            self.scene.addItem(CardItem('club',name,(x,10),scale=(0.7,0.7)))
            x += 40
        #self.view.show()
    

class CardItem(QtSvg.QGraphicsSvgItem):
    def __init__(self, suit, rank, position, angle=0, scale=(1,1)):
        super(CardItem, self).__init__(self.cardImgFile(suit,rank))        
        self.setPos(position[0],position[1])
        self.rotate(angle)
        self.scale(scale[0],scale[1])               
        self.name = suit + "_" + rank
        self.setAcceptHoverEvents(True) #by default it is set to False
        #self.setFlag(QGraphicsItem.ItemIsMovable)      

    
    def cardImgFile(self,suit,rank):
        path = "svg"
        fn = os.path.join(path,suit + "_" + rank + ".svg")
        #print fn
        return fn

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

