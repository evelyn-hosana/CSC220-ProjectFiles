#!/usr/local/bin/python3

# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.

# Evelyn Hosana

import cgi, cgitb
cgitb.enable()

print ("Content-type: text/html\n")

# retrieve form.html data
form = cgi.FieldStorage()
# if not text was submitted in html, stop process
if 'text' not in form:
    print ("No input was provided, please try again")
# get text from form
text = form.getvalue('text')
# split text by new lines
formatted_text = text.splitlines()
# set an empty dictionary for memory dump
memory = {}

# function that prints my name if input is NAME
def name_action():
    print ("<br>Evelyn Hosana")

# function that prints dumped variables if input is DUMP
def dump_action():
    # loop through split text
    print ("<br><br>Memory Dump Below:")
    print ("<br> ---------------- ")
    for var, val in memory.items():
        # print variables and values as a table
        print ("<tr><th><br>{}</th>&emsp;|&emsp;<th>{}</th></tr><br>".format(var, val))
        print (" ---------------- ")

# loop through text
for f_text in formatted_text:
    # if the input is NAME
    if (f_text == "NAME"):
        # call name_action function that prints my name
        name_action()
    # if the input is DUMP
    elif (f_text == "DUMP"):
        # call dump_action function that prints memory
        dump_action()
    # all other inputs
    else:
        # assign variable and value 'variables' to keep track of input after being split by assignment operator
        # strip in case of whitespaces
        var, val = f_text.strip().split(":=")
        # ensure floats are possible, else throw errors
        if val[0].islower():
            if val in memory:
                memory[var] = memory[val]
            else:
                raise NameError(f"Unassigned value: '{val}'.")
        else:
            try:
                val = float(val)
                memory[var] = val
            except ValueError:
                if val in memory:
                    memory[var] = memory[val]
                else:
                    raise ValueError(f"Unassigned variable: {var}.")

# print line to double check if code ran properly
# THIS WORKS HEHE
# print("<br><br>" + "Code done executing")
