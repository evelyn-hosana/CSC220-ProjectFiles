#!/usr/local/bin/python3

# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.

# Evelyn Hosana

import cgi, cgitb, heapq
cgitb.enable()

print ("Content-type: text/html\n")

form = cgi.FieldStorage()
text = form.getvalue('text')

# create empty dictionaries
frequency = {} # one holds the amount of times the character occurs
codemap = {} # the other holds the characters output as binary code in a tree

# Node class for huffman coding trees (textbook)
class Node:
    # initializer
    def __init__(self, frequency, character):
        self.frequency = frequency
        self.character = character
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.frequency < other.frequency

# function that will take the text from HTML input and encode as desired
# in this case, count how many characters occur
def characters_found(character):
    # loop through text
    for ch in text:
        # count variable
        count = text.count(ch)
        # if count is greater than 0, insert into dictionary
        if (count > 0):
            frequency[ch] = frequency.get(ch, 0) + 1
    return frequency

# function that implements huffman coding process via heaps (textbook)
def huffman(frequency):
    heap = []
    for char, freq in frequency.items():
        heapq.heappush(heap, Node(freq, char))
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(node1.frequency + node2.frequency, '')
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)
    return heap[0]

# function calls
frequency = characters_found(text)
huffman_tree = huffman(frequency)

# generate codemap function
def traverse_tree(node, code=''):
    if node is None:
        return
    if node.character:
        codemap[node.character] = code
    traverse_tree(node.left, code + '0')
    traverse_tree(node.right, code + '1')

# function call again
traverse_tree(huffman_tree)

# print frequency map and code map as a table
print("<table>")
print("<tr><th>Character</th><th>Frequency</th><th>Tree Code</th></tr>")
for char, freq in frequency.items():
    code = codemap[char]
    print("<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(char, freq, code))
print("</table>")
