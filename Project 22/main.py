#!/usr/local/bin/python3 

# I honor Parkland's core values by affirming that I have        
# followed all academic integrity guidelines for this work.     

# Evelyn Hosana

import cgi
import cgitb
from collections import defaultdict
import heapq

cgitb.enable()

print("Content-type: text/html\n")

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex]

    def add_edge(self, start, end, weight):
        self.graph[start].append((end, weight))

    def dijkstra(self, start, end):
        distance = {vertex: float('inf') for vertex in self.graph}
        distance[start] = 0
        previous = {vertex: None for vertex in self.graph}
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distance[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance_to_neighbor = current_distance + weight
                if distance_to_neighbor < distance[neighbor]:
                    distance[neighbor] = distance_to_neighbor
                    previous[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance_to_neighbor, neighbor))

        return self.construct_path(start, end, previous), distance[end]

    def construct_path(self, start, end, previous):
        path = []
        current_vertex = end
        while current_vertex != start:
            path.insert(0, (previous[current_vertex], current_vertex))
            current_vertex = previous[current_vertex]
        return path

def parse_input(input_str):
    graph = Graph()
    lines = input_str.replace('\r', '').split('\n')

    end_of_vertices_index = -1
    for idx, line in enumerate(lines):
        if line.strip() == "#end":
            end_of_vertices_index = idx
            break

    if end_of_vertices_index == -1:
        raise ValueError("Invalid input format: '#end' not found")

    for vertex in lines[:end_of_vertices_index]:
        graph.add_vertex(vertex.strip())

    for edge in lines[end_of_vertices_index + 1:]:
        data = edge.strip().split(',')
        if len(data) == 3:
            start, end, weight = data
            try:
                weight = float(weight)
                if weight != 0:  # Add edge only if weight is non-zero
                    graph.add_edge(start.strip(), end.strip(), weight)
            except ValueError:
                continue

    return graph

def parse_form_input(form):
    textarea_data = form.getvalue("graph_data", "")
    return textarea_data

def main():
    form = cgi.FieldStorage()
    graph_data = parse_form_input(form)

    if graph_data:
        try:
            graph = parse_input(graph_data)

            start = "START"
            end = "END"

            path, total_weight = graph.dijkstra(start, end)

            if path:
                print("Path:<br><br>")
                for edge in path:
                    print("&emsp;{}, {}, {}<br>".format(edge[0], edge[1], graph.graph[edge[0]][0][1]))
                print("<br>Total weight is: {}".format(total_weight))
            else:
                print("No path found from START to END")
        except ValueError as ve:
            print("Error: {}".format(ve))
    else:
        print("Unfortunately, there was no input provided.<br>")
        print("Please try again.")

if __name__ == "__main__":
    main()
