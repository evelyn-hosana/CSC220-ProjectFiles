#!/usr/local/bin/python3 

# I honor Parkland's core values by affirming that I have        
# followed all academic integrity guidelines for this work.     

# Evelyn Hosana

import cgi, cgitb
from graph import Graph
cgitb.enable()

print ("Content-type: text/html\n") 

# Retrieve form data
form = cgi.FieldStorage()
text = form.getvalue('text')

# Process the form input and find the shortest path
# Ensure text in form to prevent NoneType Errors
if 'text' in form:
    graph = Graph()  # Create instance of graph class
    lines = text.strip().splitlines()  # Split by the correct newline character

    # Process the input to create the graph
    end_marker = False # Ensure no input is being read yet 
    for line in lines: # Loop through lines
        if line == "#end": # If end marker for vertice input is found, start reading edge markers and continue code
            end_marker = True
            continue
        if not end_marker: # Add vertices to graph before #end and read edges 
            vertex = line.strip()
            graph.add_vertex(vertex)
        else: # Otherwise, split edges and ensure conditionals are met before adding edges to graph
            edge = line.strip().split(", ")
            if len(edge) == 2:
                vertex1, vertex2 = edge
                graph.add_edge(vertex1, vertex2)
            else: # Ignore incorrectly formatted edges
                print("Ignoring invalid edge: {}<br>".format(line))
    
    # Find the path from START to END using BFS per requirements
    start_vertex = "START"
    end_vertex = "END"
    path = graph.find_path_bfs(start_vertex, end_vertex)

    # Output the result if path is found, otherwise tell user no path was found
    if path:
        print("The path from START to END is:<br><br>")
        print("&ensp; &#8594; &ensp;".join(path))
    else:
        print("Unfortunately, there was no path found from '{}' to '{}' in the graph provided.".format(start_vertex, end_vertex))
        print("<br>Please try a different graph input.")
# If there is no input, tell the user                
else:
    print("It seems like there has been no input provided.<br>")
    print("Please input the graph data in the textarea given.")
