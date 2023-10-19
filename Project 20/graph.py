# I honor Parkland's core values by affirming that I have        
# followed all academic integrity guidelines for this work.     

# Evelyn Hosana

class Graph:
    def __init__(self):
        self.vertices = {}
        self.visited = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = []

    def add_edge(self, src, dest):
        self.vertices[src].append(dest)

    def is_cyclic(self, v):
        self.visited[v] = True
        for neighbor in self.vertices[v]:
            if neighbor in self.visited:
                return True
            elif neighbor not in self.visited:
                if self.is_cyclic(neighbor):
                    return True
        del self.visited[v]
        return False

    def check_cyclic(self):
        for vertex in self.vertices:
            if vertex not in self.visited:
                if self.is_cyclic(vertex):
                    return "cyclic"
        return "acyclic"
