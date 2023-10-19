#!/usr/local/bin/python3

# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.

# Evelyn Hosana

import cgi, cgitb
from avl_tree import AVLTreeMap
cgitb.enable()


print("Content-type: text/html\n")

# get data from form
form = cgi.FieldStorage()
text = form.getvalue('text')

# Online dictionary that must be used
filename = "/home/staff/kurban/public/lists/web2.txt"
dictionary = AVLTreeMap()  # create instance of AVLTreeMap

# Load the dictionary
dictionary.load_dictionary(filename)

# create a list of misspelled words
misspelled_words = []

# Method in case of no misspelled words
def smarty_pants():
    print("Good job smartypants, looks like you know how to spell!")
    print("<br> No Misspelled Words Detected")

# ensure submit in form the prevent NoneType errors
if 'submit' in form:
    # split text into words and check for misspelled words
    words = text.split()
    for word in words:
        word = word.strip().lower()
        if word not in dictionary:
            misspelled_words.append(word)

# output the results here
if not misspelled_words:
    smarty_pants()
else:
    print("What a bummer... looks like we have to review some words you can't seem to spell correctly :(")
    print("<h3>Misspelled Words:</h3>")
    print("<ul>")
    for word in misspelled_words:
        print("<li>{}</li>".format(word))
    print("</ul>")
