#!/usr/local/bin/python3 

# I honor Parkland's core values by affirming that I have        
# followed all academic integrity guidelines for this work.     

# Evelyn Hosana

import cgi, cgitb, math
from graph import Graph
cgitb.enable()

print("Content-type: text/html\n")

# get data from form.html
form = cgi.FieldStorage()
text = form.getvalue('text')

# Ensure text in form to preven NoneType Errors
if text:
    input_data = text.strip()
    # method to store data
    def parse_input_data(input_data):
        lines = input_data.strip().split('\n')
        vertices = []
        edges = []
        for line in lines:
            if line.strip() == "#end":
                break
            vertices.append(line.strip())
        for line in lines[len(vertices) + 1:]:
            edge = line.strip().split(',')
            if len(edge) == 2:
                edges.append((edge[0].strip(), edge[1].strip()))
        return vertices, edges

    # Method that fills graph
    def build_graph(vertices, edges):
        g = Graph()
        verts = {}
        for v in vertices:
            if v in verts:
                print("Error: Duplicate vertex name '{}'".format(v))
                return None
            verts[v] = g.insert_vertex(v)
        for edge in edges:
            src, dest = edge
            if src not in verts or dest not in verts:
                print("Error: Invalid edge '{} -> {}'".format(src, dest))
                continue
            g.insert_edge(verts[src], verts[dest])
        return g

    vertices, edges = parse_input_data(input_data)
    output_graph = build_graph(vertices, edges)

    # Basic output of my graph in HTML
    if output_graph:
        print("Below is an ouput of the graph you are describing:<br><br>")
        print("There are {} edges <br>".format(output_graph.edge_count()))
        print("There are {} vertices <br>".format(output_graph.vertex_count()))
        print("-----------------------------------<br>")
        print("Edges below:<br>")
        for e in output_graph.edges():
            print("Edge: {}<br>".format(e))
        print("-----------------------------------<br>")
        print("Vertices below:<br>")
        for v in output_graph.vertices():
            print("Vertex: {}<br>".format(v))
        print("-----------------------------------<br>")
        print("Vertices with their outgoing edges<br>")
        for v in output_graph.vertices():
            print("Vertex: {}<br>".format(v))
            for e in output_graph.incident_edges(v, True):
                print("  Connects to: {}<br>".format(e.opposite(v).element()))

    # EXTRA CREDIT - Export my graph as an SVG image
    print("<br> Here is a visual representation of your graph:<br>")
    # Calculate vertex positions on a circle
    num_vertices = output_graph.vertex_count()
    center_x, center_y = 500, 500
    radius = 300
    angle_increment = 2 * math.pi / num_vertices

    vertex_positions = []
    for i, vertex in enumerate(output_graph.vertices()):
        angle = i * angle_increment
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        vertex_positions.append((x, y))

    # Generate SVG code
    svg_code = '<html><head></head><body>'
    svg_code += '<svg height="1000" width="1000">'

    # Generate vertex circles
    for vertex, (x, y) in zip(output_graph.vertices(), vertex_positions):
        svg_code += f'<circle cx="{x}" cy="{y}" r="30" fill="lightblue" />'
        svg_code += f'<text x="{x}" y="{y + 40}" text-anchor="middle" dominant-baseline="middle">{vertex.element()}</text>'

    # Generate edges
    for edge in output_graph.edges():
        source_vertex = edge.endpoints()[0].element()
        target_vertex = edge.endpoints()[1].element()
        source_index = vertices.index(source_vertex)
        target_index = vertices.index(target_vertex)
        source_x, source_y = vertex_positions[source_index]
        target_x, target_y = vertex_positions[target_index]

        angle = math.atan2(target_y - source_y, target_x - source_x)
        arrow_size = 10  # Adjust the arrow size as desired

        line_code = f'<line x1="{source_x}" y1="{source_y}" x2="{target_x}" y2="{target_y}" stroke="black" stroke-width="2" />'
        arrowhead_code = f'<polygon points="{target_x},{target_y} ' \
                    f'{target_x - arrow_size * math.cos(angle - math.pi / 6)},{target_y - arrow_size * math.sin(angle - math.pi / 6)} ' \
                    f'{target_x - arrow_size * math.cos(angle + math.pi / 6)},{target_y - arrow_size * math.sin(angle + math.pi / 6)}" ' \
                    f'style="fill:black;" />'

        svg_code += line_code + arrowhead_code

        # Add a bidirectional arrowhead for the opposite direction
        reverse_arrowhead_code = f'<polygon points="{source_x},{source_y} ' \
                             f'{source_x + arrow_size * math.cos(angle - math.pi / 6)},{source_y + arrow_size * math.sin(angle - math.pi / 6)} ' \
                             f'{source_x + arrow_size * math.cos(angle + math.pi / 6)},{source_y + arrow_size * math.sin(angle + math.pi / 6)}" ' \
                             f'style="fill:black;" />'

        svg_code += reverse_arrowhead_code

        svg_code += f'<line x1="{source_x}" y1="{source_y}" x2="{target_x}" y2="{target_y}" stroke="black" stroke-width="2" />'

    svg_code += '</svg>'
    svg_code += '</body></html>'

    print(svg_code)

else:
    print("No input data provided.")
