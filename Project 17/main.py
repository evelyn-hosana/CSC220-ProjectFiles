#!/usr/local/bin/python3 

# I honor Parkland's core values by affirming that I have        
# followed all academic integrity guidelines for this work.     

# Evelyn Hosana

import cgi, cgitb
cgitb.enable()

print ("Content-type: text/html\n") 

form = cgi.FieldStorage()
text = form.getvalue('text')
pattern = form.getvalue('pattern')

def KMP_match(pattern, text):
    prefix = [-1] * len(pattern)
    for i in range(1, len(pattern)):
        j = prefix[i - 1]
        while j >= 0 and pattern[j + 1] != pattern[i]:
            j = prefix[j]
        if pattern[j + 1] == pattern[i]:
            prefix[i] = j + 1
    j = -1
    for i in range(len(text)):
        while j >= 0 and pattern[j + 1] != text[i]:
            j = prefix[j]
        if pattern[j + 1] == text[i]:
            j += 1
        if j == len(pattern) - 1:
            return i - j
    return -1

result = KMP_match(pattern, text)
if result == -1:
    print("Unfortunately, the word you were looking for was not found<br>")
    print("Please try another word... if you dare")
else:
    print("Congragulations!<br>")
    print("Your desired word was found at position:", result)
