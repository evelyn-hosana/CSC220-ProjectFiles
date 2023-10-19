#!/usr/local/bin/python3

# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Evelyn Hosana

# Imports here
import cgi, cgitb
from graph import Graph
cgitb.enable()

print("Content-type: text/html\n")

# Get form data from form.html
form = cgi.FieldStorage()
text = form.getvalue('text')

# Check for text and prevent NoneType Error
if 'text' in form: 
    # Parse the input text to construct the graph
    lines = text.splitlines()
    print("Parsed input is:", lines)  # Debugging line to print the parsed lines

    vertices = set()
    edges = []
    end_index = lines.index("#end") if "#end" in lines else len(lines)

    for line in lines[:end_index]:
        vertices.add(line)

    for line in lines[end_index + 1:]:
        src, dest = line.split(", ")
        if src in vertices and dest in vertices:
            edges.append((src, dest))

    graph = Graph()
    for vertex in vertices:
        graph.add_vertex(vertex)

    for edge in edges:
        graph.add_edge(edge[0], edge[1])

    # Check if the graph is cyclic or acyclic
    result = graph.check_cyclic()

    # Print the result
    print("<br><br>Based on your input, your graph is: {}".format(result))
else:
    print("Sorry, no text was provided.<br>")
    print("Please try again")
