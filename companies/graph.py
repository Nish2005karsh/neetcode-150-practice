# Implement dfs and bfs
# from collections import defaultdict
# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list)
#     def add_edge(self, u, v):
#         self.graph[u].append(v)
#     def dfs(self, start, visited=None):
#         if visited is None:
#             visited = set()
#         visited.add(start)
#         print(start, end=" ")
#         for neighbour in self.graph[start]:
#             if neighbour not in visited:
#                 self.dfs(neighbour, visited)
# g = Graph()
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 2)
# g.add_edge(2, 0)
# g.add_edge(2, 3)
# g.add_edge(3, 3)

# print("DFS starting from node 2:")
# g.dfs(2)

# BFS
# from collections import defaultdict, deque
# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list)
#     def add_edge(self, u, v):
#         self.graph[u].append(v)
#     def bfs(self, start):
#         visited = set()
#         queue = deque([start])
#         visited.add(start)
#         while queue:
#             node = queue.popleft()
#             print(node, end=" ")

#             for neighbour in self.graph[node]:
#                 if neighbour not in visited:
#                     visited.add(neighbour)
#                     queue.append(neighbour)


# # Example usage
# g = Graph()
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 2)
# g.add_edge(2, 0)
# g.add_edge(2, 3)
# g.add_edge(3, 3)

# print("BFS starting from node 2:")
# g.bfs(2)

# Dijkastra
# import heapq
# from collections import defaultdict

# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list)  # adjacency list {u: [(v, w), ...]}

#     def add_edge(self, u, v, w):
#         self.graph[u].append((v, w))
#         self.graph[v].append((u, w))  # if undirected graph, include this line

#     def dijkstra(self, start):
#         # Min-heap (priority queue)
#         pq = [(0, start)]  # (distance, node)
#         distances = {node: float('inf') for node in self.graph}
#         distances[start] = 0

#         while pq:
#             curr_dist, node = heapq.heappop(pq)

#             # Skip if we already found a better path
#             if curr_dist > distances[node]:
#                 continue

#             for neighbor, weight in self.graph[node]:
#                 distance = curr_dist + weight
#                 if distance < distances[neighbor]:
#                     distances[neighbor] = distance
#                     heapq.heappush(pq, (distance, neighbor))

#         return distances

# g = Graph()
# g.add_edge("A", "B", 4)
# g.add_edge("A", "C", 2)
# g.add_edge("B", "C", 5)
# g.add_edge("B", "D", 10)
# g.add_edge("C", "E", 3)
# g.add_edge("E", "D", 4)
# g.add_edge("D", "F", 11)
# start_node = "A"
# shortest_paths = g.dijkstra(start_node)
# print(f"Shortest paths from {start_node}: {shortest_paths}")

# Prims algo
# import heapq
# from collections import defaultdict

# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list)

#     def add_edge(self, u, v, w):
#         self.graph[u].append((w, v))
#         self.graph[v].append((w, u))  # undirected

#     def prims(self, start):
#         visited = set()
#         min_heap = [(0, start)]  # (weight, node)
#         mst_weight = 0
#         mst_edges = []

#         while min_heap and len(visited) < len(self.graph):
#             weight, node = heapq.heappop(min_heap)
#             if node in visited:
#                 continue
#             visited.add(node)
#             mst_weight += weight

#             if weight != 0:  # skip the starting node edge
#                 mst_edges.append((node, weight))

#             for edge_weight, neighbor in self.graph[node]:
#                 if neighbor not in visited:
#                     heapq.heappush(min_heap, (edge_weight, neighbor))

#         return mst_weight, mst_edges


# # Example Usage
# g = Graph()
# g.add_edge("A", "B", 2)
# g.add_edge("A", "C", 3)
# g.add_edge("B", "C", 1)
# g.add_edge("B", "D", 4)
# g.add_edge("C", "D", 5)

# mst_weight, mst_edges = g.prims("A")
# print("Prim's MST Weight:", mst_weight)
# print("Prim's MST Edges:", mst_edges)
# Kruskal algo
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # path compression
        return self.parent[u]
    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            if self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            elif self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1
            return True
        return False
def kruskal(n, edges):
    # edges = (weight, u, v)
    edges.sort()
    ds = DisjointSet(n)
    mst_weight = 0
    mst_edges = []

    for w, u, v in edges:
        if ds.union(u, v):
            mst_weight += w
            mst_edges.append((u, v, w))

    return mst_weight, mst_edges
# Example Usage
edges = [
    (2, 0, 1),
    (3, 0, 2),
    (1, 1, 2),
    (4, 1, 3),
    (5, 2, 3)
]
n = 4  # number of nodes (0,1,2,3)
mst_weight, mst_edges = kruskal(n, edges)
print("Kruskal's MST Weight:", mst_weight)
print("Kruskal's MST Edges:", mst_edges)

