import heapq
import sys


class Graph:

    def __init__(self, dict):
        self.vertices = dict

    def add_vertex(self, name, edges):
        self.vertices[name] = edges

    def add_vertices(self, dict):
        self.vertices = dict

    def shortest_path(self, start, finish):
        distances = {}  # Distance from start to node
        previous = {}  # Previous node in optimal path from source
        nodes = []  # Priority queue of all nodes in Graph

        for vertex in self.vertices:
            if vertex == start:  # Set root node as distance of 0
                distances[vertex] = 0
                heapq.heappush(nodes, [0, vertex])
            else:
                distances[vertex] = sys.maxsize
                heapq.heappush(nodes, [sys.maxsize, vertex])
            previous[vertex] = None

        while nodes:
            # Vertex in nodes with smallest distance in distances
            smallest = heapq.heappop(nodes)[1]
            if smallest == finish:  # If the closest node is our target we're done so print the path
                path = []
                # Traverse through nodes til we reach the root which is 0
                while previous[smallest]:
                    path.append(smallest)
                    smallest = previous[smallest]
                return path
            # All remaining vertices are inaccessible from source
            if distances[smallest] == sys.maxsize:
                break

            # Look at all the nodes that this vertex is attached to
            for neighbor in self.vertices[smallest]:
                # Alternative path distance
                alt = distances[smallest] + self.vertices[smallest][neighbor]
                # If there is a new shortest path update our priority queue (relax)
                if alt < distances[neighbor]:
                    distances[neighbor] = alt
                    previous[neighbor] = smallest
                    for n in nodes:
                        if n[1] == neighbor:
                            n[0] = alt
                            break
                    heapq.heapify(nodes)
        return distances

    def path_length(self, start, finish):
        path = self.shortest_path(start, finish)
        length = 0
        if hasattr(path, 'has_key'):
            return 0
        if path:
            # print path
            last_vert = start
            for vert in reversed(path):
                if start != vert:
                    length += self.vertices[last_vert][vert]
                last_vert = vert
        return length

    def __str__(self):
        return str(self.vertices)
