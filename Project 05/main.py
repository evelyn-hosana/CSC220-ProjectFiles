#!/usr/local/bin/python3

# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.

# Evelyn Hosana

import cgi, cgitb
cgitb.enable()

print ("Content-type: text/html\n")

# Retrieve form data

form = cgi.FieldStorage()
formatted_text = form.getvalue('textbox').split()
data = list(map(int, formatted_text))
passed = [False] * len(data)

# Recursive function for 'The Game'
def theGame(curr, data, passed, path_of_data):
    # CONDITIONALS HERE
    # if current position is out of bounds, beginning has value of 0, or position has been visited, return false
    if (curr >= len(data) or curr < 0 or data[0] == 0 or passed[curr]):
        return False, path_of_data
    # if the current position has been visited, return false
    if (passed[curr]):
        return False, path_of_data
    # if current position is the end, return true
    if (curr == len(data)-1):
        passed[curr] = True
        path_of_data.append(str(curr))
        return True, path_of_data
    # visit current position
    passed[curr] = True
    path_of_data.append(str(curr))
    # make recursive calls on both left and right sides
    win, path_of_data = theGame(curr - data[curr], data, passed, path_of_data)
    if not win:
        win, path_of_data = theGame(curr + data[curr], data, passed, path_of_data)
    if not win:
        path_of_data.pop()
        passed[curr] = False
    return win, path_of_data

# call function
win, path_of_data = theGame(0, data, passed, [])
if win:
    print(" --> ".join(path_of_data) + " --> Win")
else:
    print("There is no solution to the input you have given. Sorry, try another!")
