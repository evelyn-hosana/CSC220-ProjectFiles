# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidlines for this work

# Evelyn Hosana

class Point:
    def __init__(self, across = 0, down = 0):
        self._across = across
        self._down = down
    def setAcross(self, across):
        self._across = across
    def setDown(self, down):
        self._down = down
    def getAcross(self):
        return self._across
    def getDown(self):
        return self._down
