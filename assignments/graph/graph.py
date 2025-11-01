"""
Graph Data Structure Implementation

This module provides complete implementations of graph structures:
Undirected Graph, Directed Graph, Weighted Graph, and graph algorithms.

Author: Data Structure Course
Date: 2024
"""

from collections import deque, defaultdict
import heapq


class Graph:
    """
    Undirected unweighted graph using adjacency list.
    
    Efficient for sparse graphs.
    All operations are optimized for typical graph algorithms.
    """
    
    def __init__(self):
        """Initialize an empty graph."""
        self.adj_list = {}
        self._num_edges = 0
    
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        
        Args:
            vertex: The vertex to add
            
        Time Complexity: O(1)
        """
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
    
    def add_edge(self, u, v):
        """
        Add an undirected edge between two vertices.
        
        Args:
            u: First vertex
            v: Second vertex
            
        Time Complexity: O(1)
        """
        # Add vertices if they don't exist
        self.add_vertex(u)
        self.add_vertex(v)
        
        # Add edge in both directions (undirected)
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
            self._num_edges += 1
        
        if u not in self.adj_list[v]:
            self.adj_list[v].append(u)
    
    def remove_edge(self, u, v):
        """
        Remove an edge between two vertices.
        
        Args:
            u: First vertex
            v: Second vertex
            
        Returns:
            bool: True if edge was removed, False if it didn't exist
            
        Time Complexity: O(degree)
        """
        if u not in self.adj_list or v not in self.adj_list:
            return False
        
        removed = False
        
        if v in self.adj_list[u]:
            self.adj_list[u].remove(v)
            removed = True
        
        if u in self.adj_list[v]:
            self.adj_list[v].remove(u)
        
        if removed:
            self._num_edges -= 1
        
        return removed
    
    def has_edge(self, u, v):
        """
        Check if an edge exists between two vertices.
        
        Args:
            u: First vertex
            v: Second vertex
            
        Returns:
            bool: True if edge exists, False otherwise
            
        Time Complexity: O(degree)
        """
        if u not in self.adj_list:
            return False
        return v in self.adj_list[u]
    
    def get_neighbors(self, vertex):
        """
        Get all neighbors of a vertex.
        
        Args:
            vertex: The vertex to query
            
        Returns:
            list: List of neighboring vertices
            
        Time Complexity: O(1)
        """
        return self.adj_list.get(vertex, [])
    
    def get_vertices(self):
        """Get all vertices in the graph."""
        return list(self.adj_list.keys())
    
    def num_vertices(self):
        """Get the number of vertices."""
        return len(self.adj_list)
    
    def num_edges(self):
        """Get the number of edges."""
        return self._num_edges
    
    def degree(self, vertex):
        """
        Get the degree of a vertex.
        
        Args:
            vertex: The vertex to query
            
        Returns:
            int: Degree of the vertex
        """
        return len(self.adj_list.get(vertex, []))
    
    def bfs(self, start):
        """
        Perform breadth-first search from a starting vertex.
        
        Args:
            start: Starting vertex
            
        Returns:
            list: Vertices in BFS order
            
        Time Complexity: O(V + E)
        """
        if start not in self.adj_list:
            return []
        
        visited = set([start])
        queue = deque([start])
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start):
        """
        Perform depth-first search from a starting vertex.
        
        Args:
            start: Starting vertex
            
        Returns:
            list: Vertices in DFS order
            
        Time Complexity: O(V + E)
        """
        if start not in self.adj_list:
            return []
        
        visited = set()
        result = []
        
        def dfs_recursive(vertex):
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)
        
        dfs_recursive(start)
        return result
    
    def shortest_path(self, start, end):
        """
        Find shortest path between two vertices using BFS.
        
        Args:
            start: Starting vertex
            end: Ending vertex
            
        Returns:
            list: Shortest path from start to end, or None if no path exists
            
        Time Complexity: O(V + E)
        """
        if start not in self.adj_list or end not in self.adj_list:
            return None
        
        if start == end:
            return [start]
        
        visited = {start}
        queue = deque([(start, [start])])
        
        while queue:
            vertex, path = queue.popleft()
            
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    
                    if neighbor == end:
                        return new_path
                    
                    visited.add(neighbor)
                    queue.append((neighbor, new_path))
        
        return None
    
    def is_connected(self):
        """
        Check if the graph is connected.
        
        Returns:
            bool: True if connected, False otherwise
            
        Time Complexity: O(V + E)
        """
        if not self.adj_list:
            return True
        
        start = next(iter(self.adj_list))
        visited = set(self.bfs(start))
        
        return len(visited) == len(self.adj_list)
    
    def find_components(self):
        """
        Find all connected components.
        
        Returns:
            list: List of components, each component is a list of vertices
            
        Time Complexity: O(V + E)
        """
        visited = set()
        components = []
        
        for vertex in self.adj_list:
            if vertex not in visited:
                component = self.bfs(vertex)
                visited.update(component)
                components.append(component)
        
        return components
    
    def has_cycle(self):
        """
        Check if the graph has a cycle.
        
        Returns:
            bool: True if cycle exists, False otherwise
            
        Time Complexity: O(V + E)
        """
        visited = set()
        
        def dfs_cycle(vertex, parent):
            visited.add(vertex)
            
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    if dfs_cycle(neighbor, vertex):
                        return True
                elif neighbor != parent:
                    return True  # Back edge found
            
            return False
        
        for vertex in self.adj_list:
            if vertex not in visited:
                if dfs_cycle(vertex, None):
                    return True
        
        return False
    
    def __str__(self):
        """String representation of the graph."""
        return f"Graph(vertices={self.num_vertices()}, edges={self.num_edges()})"
    
    def __repr__(self):
        """Developer representation of the graph."""
        return self.__str__()


class DirectedGraph:
    """
    Directed unweighted graph using adjacency list.
    
    Edges have direction: u -> v does not imply v -> u.
    """
    
    def __init__(self):
        """Initialize an empty directed graph."""
        self.adj_list = {}
        self._num_edges = 0
    
    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
    
    def add_edge(self, u, v):
        """
        Add a directed edge from u to v.
        
        Args:
            u: Source vertex
            v: Destination vertex
        """
        self.add_vertex(u)
        self.add_vertex(v)
        
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
            self._num_edges += 1
    
    def remove_edge(self, u, v):
        """Remove a directed edge from u to v."""
        if u not in self.adj_list:
            return False
        
        if v in self.adj_list[u]:
            self.adj_list[u].remove(v)
            self._num_edges -= 1
            return True
        
        return False
    
    def has_edge(self, u, v):
        """Check if edge u -> v exists."""
        if u not in self.adj_list:
            return False
        return v in self.adj_list[u]
    
    def get_neighbors(self, vertex):
        """Get all outgoing neighbors of a vertex."""
        return self.adj_list.get(vertex, [])
    
    def get_vertices(self):
        """Get all vertices."""
        return list(self.adj_list.keys())
    
    def num_vertices(self):
        """Get number of vertices."""
        return len(self.adj_list)
    
    def num_edges(self):
        """Get number of edges."""
        return self._num_edges
    
    def out_degree(self, vertex):
        """Get out-degree of a vertex."""
        return len(self.adj_list.get(vertex, []))
    
    def in_degree(self, vertex):
        """Get in-degree of a vertex."""
        count = 0
        for v in self.adj_list:
            if vertex in self.adj_list[v]:
                count += 1
        return count
    
    def bfs(self, start):
        """Perform BFS from starting vertex."""
        if start not in self.adj_list:
            return []
        
        visited = set([start])
        queue = deque([start])
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start):
        """Perform DFS from starting vertex."""
        if start not in self.adj_list:
            return []
        
        visited = set()
        result = []
        
        def dfs_recursive(vertex):
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)
        
        dfs_recursive(start)
        return result
    
    def has_cycle(self):
        """
        Check if directed graph has a cycle using DFS with colors.
        
        Returns:
            bool: True if cycle exists
        """
        WHITE, GRAY, BLACK = 0, 1, 2
        color = {vertex: WHITE for vertex in self.adj_list}
        
        def dfs_cycle(vertex):
            color[vertex] = GRAY
            
            for neighbor in self.adj_list[vertex]:
                if color[neighbor] == GRAY:
                    return True  # Back edge (cycle)
                if color[neighbor] == WHITE and dfs_cycle(neighbor):
                    return True
            
            color[vertex] = BLACK
            return False
        
        for vertex in self.adj_list:
            if color[vertex] == WHITE:
                if dfs_cycle(vertex):
                    return True
        
        return False
    
    def topological_sort(self):
        """
        Perform topological sort (only for DAG).
        
        Returns:
            list: Vertices in topological order, or None if cycle exists
        """
        if self.has_cycle():
            return None
        
        in_deg = {v: self.in_degree(v) for v in self.adj_list}
        queue = deque([v for v in self.adj_list if in_deg[v] == 0])
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor in self.adj_list[vertex]:
                in_deg[neighbor] -= 1
                if in_deg[neighbor] == 0:
                    queue.append(neighbor)
        
        return result if len(result) == len(self.adj_list) else None
    
    def __str__(self):
        """String representation."""
        return f"DirectedGraph(vertices={self.num_vertices()}, edges={self.num_edges()})"


class WeightedGraph:
    """
    Weighted undirected graph using adjacency list.
    
    Edges have associated weights/costs.
    """
    
    def __init__(self):
        """Initialize an empty weighted graph."""
        self.adj_list = {}
        self._num_edges = 0
    
    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
    
    def add_edge(self, u, v, weight):
        """
        Add a weighted undirected edge.
        
        Args:
            u: First vertex
            v: Second vertex
            weight: Edge weight
        """
        self.add_vertex(u)
        self.add_vertex(v)
        
        # Add edge in both directions with weight
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))
        self._num_edges += 1
    
    def get_neighbors(self, vertex):
        """Get neighbors with weights."""
        return self.adj_list.get(vertex, [])
    
    def get_vertices(self):
        """Get all vertices."""
        return list(self.adj_list.keys())
    
    def num_vertices(self):
        """Get number of vertices."""
        return len(self.adj_list)
    
    def num_edges(self):
        """Get number of edges."""
        return self._num_edges
    
    def dijkstra(self, start, end=None):
        """
        Find shortest paths from start using Dijkstra's algorithm.
        
        Args:
            start: Starting vertex
            end: Optional ending vertex
            
        Returns:
            dict: Distances from start to all vertices (or distance to end)
            
        Time Complexity: O((V + E) log V)
        """
        if start not in self.adj_list:
            return {} if end is None else float('inf')
        
        dist = {vertex: float('inf') for vertex in self.adj_list}
        dist[start] = 0
        pq = [(0, start)]
        visited = set()
        
        while pq:
            d, vertex = heapq.heappop(pq)
            
            if vertex in visited:
                continue
            
            visited.add(vertex)
            
            if end and vertex == end:
                return d
            
            for neighbor, weight in self.adj_list[vertex]:
                if neighbor not in visited:
                    new_dist = d + weight
                    if new_dist < dist[neighbor]:
                        dist[neighbor] = new_dist
                        heapq.heappush(pq, (new_dist, neighbor))
        
        return dist if end is None else dist.get(end, float('inf'))
    
    def shortest_path(self, start, end):
        """
        Find shortest path between two vertices.
        
        Returns:
            tuple: (path, distance) or (None, inf) if no path
        """
        if start not in self.adj_list or end not in self.adj_list:
            return None, float('inf')
        
        dist = {vertex: float('inf') for vertex in self.adj_list}
        dist[start] = 0
        prev = {vertex: None for vertex in self.adj_list}
        pq = [(0, start)]
        visited = set()
        
        while pq:
            d, vertex = heapq.heappop(pq)
            
            if vertex in visited:
                continue
            
            visited.add(vertex)
            
            if vertex == end:
                # Reconstruct path
                path = []
                current = end
                while current is not None:
                    path.append(current)
                    current = prev[current]
                return path[::-1], d
            
            for neighbor, weight in self.adj_list[vertex]:
                if neighbor not in visited:
                    new_dist = d + weight
                    if new_dist < dist[neighbor]:
                        dist[neighbor] = new_dist
                        prev[neighbor] = vertex
                        heapq.heappush(pq, (new_dist, neighbor))
        
        return None, float('inf')
    
    def __str__(self):
        """String representation."""
        return f"WeightedGraph(vertices={self.num_vertices()}, edges={self.num_edges()})"


class UnionFind:
    """
    Union-Find (Disjoint Set Union) data structure.
    
    Used for detecting cycles and finding connected components efficiently.
    """
    
    def __init__(self, vertices):
        """
        Initialize Union-Find structure.
        
        Args:
            vertices: List of vertices
        """
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}
        self.num_components = len(vertices)
    
    def find(self, x):
        """
        Find the root of x with path compression.
        
        Time Complexity: O(α(n)) amortized (nearly constant)
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """
        Union two sets containing x and y.
        
        Returns:
            bool: True if union was performed, False if already in same set
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        self.num_components -= 1
        return True
    
    def connected(self, x, y):
        """Check if x and y are in the same set."""
        return self.find(x) == self.find(y)
    
    def count_components(self):
        """Get number of connected components."""
        return self.num_components
