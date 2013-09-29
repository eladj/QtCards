PyQt custom widget for creating card games

This package contains the following classes:
============================================
cardTableWidget
---------------
inherits: QtGui.QWidget
Description: A default area for creating the card game

CardItem
--------
inherits: QtSvg.QGraphicsSvgItem
Description: A default card class that handles the graphics of the cards.
All the cards are displayed in svg format, so they can be rescaled without damaging the resolution. 