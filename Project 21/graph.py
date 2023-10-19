# I honor Parkland's core values by affirming that I have        
# followed all academic integrity guidelines for this work.     

# Evelyn Hosana

from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
    
    def find_path_bfs(self, start, end):
        queue = deque()
        queue.append([start])
        visited = set()

        while queue:
            path = queue.popleft()
            last_vertex = path[-1]

            if last_vertex == end:
                return path
            
            if last_vertex not in visited:
                visited.add(last_vertex)
                for vertex in self.graph.get(last_vertex, []):
                    new_path = list(path)
                    new_path.append(vertex)
                    queue.append(new_path)

        return None
