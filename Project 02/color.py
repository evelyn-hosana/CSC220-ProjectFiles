# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.

# Evelyn Hosana

class Color:
    def __init__(self, red = 0, green = 0, blue = 0):
        self._red = red
        self._green = green
        self._blue = blue
    def setRed(self, red):
        self._red = red
    def setGreen(self, green):
        self._green = green
    def setBlue(self, blue):
        self._blue = blue
    def getRed(self):
        return self._red
    def getGreen(self):
        return self._green
    def getBlue(self):
        return self._blue
    def SVG(self):
        return "rgb({},{},{})".format(self.getRed(), self.getGreen(), self.getBlue())
