#!/usr/local/bin/python3

# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidlines for this work.

# Evelyn Hosana
import cgi, cgitb
import random
from rectangle import Rectangle
from color import Color
from point import Point
cgitb.enable()
print ("Content-type: text/html\n")

# Initialize rectangle_list
rectangle_list = []
# Code that creates 1000 or so objects and puts them in rectangle_list
for count in range(0,1000):
    # Code that generates Point and Color objects and add to list
    width = random.randint(1, 100)
    height = random.randint(1, 100)
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    across = random.randint(0, 900)
    down = random.randint(0, 900)
    point = Point(across, down)
    color = Color(red, green, blue)
    rectangle = Rectangle(point, width, height, color)
    rectangle_list.append(rectangle)

print ('<html><head></head><body>')
print ('<svg height="1000" width="1000">')
for rectangle in rectangle_list:
    print (rectangle.SVG())
print ('</svg>')
print ('</body></html>')

