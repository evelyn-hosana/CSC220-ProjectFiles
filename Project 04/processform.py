#!/usr/local/bin/python3

# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.

# Evelyn Hosana

import cgi, cgitb
cgitb.enable()

print ("Content-type: text/html\n")

form = cgi.FieldStorage()
textarea = form.getvalue('textarea')
submit = form.getvalue('submit')

# define a function that splits and sorts input words
def splitAndSort(input_data):
    words = input_data.split()
    unsorted_words = input_data.split()
    words.sort()
    average_length = None
    total_length = 0
    for w in words:
        total_length += len(w)
    average_length = total_length / len(words)
    print("Unsorted Words: ", unsorted_words, "<br><br>")
    print("Sorted Words: ", words, "<br>")
    print("<br>Words in 10 columns:<br>")
    for i in range(0, len(words), 10):
        print(" ".join(words[i:i+10]))
        print("<br>")
    print("<br>There are " + str(len(words)) + " words<br>")
    print("The average word length is " + str(round(average_length,4)))
    return

# Function call on any input in textbox
splitAndSort(textarea)
