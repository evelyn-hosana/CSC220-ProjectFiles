#!/usr/local/bin/python3

# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.

# Evelyn Hosana

print ("Content-type: text/html\n")

print ('<html><head></head><body>')
print ('<svg height="1000" width="1000">')

# call a user defined function that prints the circle
print ('<circle cx="50" cy="50" r="40" style="fill:rgb(135,192,255);stroke:rgb(100,30,45);stroke-width:10" />')
# call a user defined function that prints the rectangle
print ('<rect x="650" y="5" width="300" height="100" style="fill:rgb(135,192,255);stroke-width:3;stroke:rgb(100,30,45)" />')
# call a user defined function that prints your name in the rectangle
print ('<text x="770" y="60" fill:rgb(0,0,0)> Evelyn!</text>')

print ('</svg>')
print ('</body></html>')



