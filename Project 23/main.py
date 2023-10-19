#!/usr/local/bin/python3 

# I honor Parkland's core values by affirming that I have        
# followed all academic integrity guidelines for this work.     

# Evelyn Hosana

import cgi, cgitb
from graph import Graph
from mst import MST_PrimJarnik, MST_Kruskal
cgitb.enable()

print("Content-type: text/html\n")

# Retrieve form data
form = cgi.FieldStorage()
text = form.getvalue('text')

if text:
    def parse_input(text):
        vertices = []
        edges = []
        lines = text.strip().replace('\r', '').split('\n')
        end_idx = lines.index("#end")

        for vertex in lines[:end_idx]:
            vertices.append(vertex.strip())

        for line in lines[end_idx+1:]:
            parts = line.split(',')
            v1 = parts[0].strip()
            v2 = parts[1].strip()
            weight = float(parts[2].strip())
            edges.append((v1, v2, weight))
        
        return vertices, edges

    def construct_graph(vertices, edges):
        graph = Graph()
        vertex_map = {}  # To store the mapping of vertex names to their corresponding Vertex objects

        for vertex in vertices:
            v = graph.insert_vertex(vertex)
            vertex_map[vertex] = v

        for v1, v2, weight in edges:
            u = vertex_map[v1]
            v = vertex_map[v2]
            graph.insert_edge(u, v, weight)

        return graph

    def format_edges(mst_edges):
        formatted_edges = []
        total_weight = 0

        for edge in mst_edges:
            u, v = edge.endpoints()
            weight = edge.element()
            total_weight += weight
            formatted_edges.append("{}, {}, {}".format(u.element(), v.element(), weight))

        return formatted_edges, total_weight

    vertices, edges = parse_input(text)
    graph = construct_graph(vertices, edges)

    # Compute Minimum Spanning Trees
    prim_jarnik_mst = MST_PrimJarnik(graph)
    kruskal_mst = MST_Kruskal(graph)

    # Format the MST edges and total weights
    prim_jarnik_formatted_edges, prim_jarnik_total_weight = format_edges(prim_jarnik_mst)
    kruskal_formatted_edges, kruskal_total_weight = format_edges(kruskal_mst)

    # Print the output
    print("<h3>Minimum Spanning Tree - Prim-Jarnik</h3>")
    print("<pre>")
    for edge in prim_jarnik_formatted_edges:
        print(edge)
    print("Total Weight: {}".format(prim_jarnik_total_weight))
    print("</pre>")

    print("<h3>Minimum Spanning Tree - Kruskal</h3>")
    print("<pre>")
    for edge in kruskal_formatted_edges:
        print(edge)
    print("Total Weight: {}".format(kruskal_total_weight))
    print("</pre>")
else:
    print("Error: No input found")
