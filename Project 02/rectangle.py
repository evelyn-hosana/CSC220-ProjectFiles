# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.

# Evelyn Hosana

from color import Color
from point import Point

class Rectangle:
    def __init__(self, thepoint, width, height, fill):
        self._upperleft = thepoint
        self._width = width
        self._height = height
        self._fill = fill
    def setUpperLeft(self, thepoint):
        self._upperleft = thepoint
    def setWidth(self, width):
        self._width = width
    def setHeight(self, height):
        self._height = height
    def setFill(self, fill):
        self._fill = fill
    def getUpperLeft(self):
        return self._upperleft
    def getWidth(self):
        return self._width
    def getHeight(self):
        return self._height
    def getFill(self):
        return self._fill
    def SVG(self):
        return '<rect x="{}" y="{}" width="{}" height="{}" fill="{}"/>'.format(self._upperleft.getAcross(), self._upperleft.getDown(), self._width, self._height, self._fill.SVG())
