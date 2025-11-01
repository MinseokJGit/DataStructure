# Graph Assignment

This assignment contains complete implementations of graph data structures and algorithms.

## Files Overview

### 1. `graph.py` - Core Implementation
Contains multiple graph implementations:
- **Graph**: Undirected unweighted graph using adjacency list
- **DirectedGraph**: Directed unweighted graph
- **WeightedGraph**: Weighted undirected graph with Dijkstra's algorithm
- **UnionFind**: Disjoint set union for efficient connectivity queries

### 2. `application.py` - Practical Applications
Demonstrates real-world use cases of graphs:
- **Basic Operations**: Add/remove vertices and edges, traversals
- **Directed Graph**: Topological sort, cycle detection
- **Weighted Graph**: Shortest path with Dijkstra's algorithm
- **Social Network**: Friend recommendations, degrees of separation, influencers
- **Route Map**: GPS navigation, shortest routes
- **Dependency Resolver**: Package dependencies, topological ordering
- **Connected Components**: Find disconnected parts
- **Union-Find**: Efficient connectivity queries
- **Cycle Detection**: Detect cycles in directed and undirected graphs
- **Performance Comparison**: Analyze algorithm efficiency

### 3. `test_graph.py` - Unit Tests
Comprehensive test suite covering:
- Basic graph operations (add/remove vertices and edges)
- BFS and DFS traversals
- Shortest path algorithms
- Connected components
- Cycle detection
- Directed graph operations (topological sort)
- Weighted graph operations (Dijkstra's)
- Union-Find operations
- Edge cases (empty graph, single vertex, large graphs)

## Key Concepts Demonstrated

### Graph Representations

#### Adjacency List (Used in this implementation)
```python
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}
```

**Advantages:**
- Space efficient: O(V + E)
- Fast neighbor iteration: O(degree)
- Best for sparse graphs

#### Adjacency Matrix (Alternative)
```python
matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0]
]
```

**Advantages:**
- O(1) edge lookup
- Best for dense graphs

### Graph Types

| Type | Edges | Example |
|------|-------|---------|
| Undirected | Bidirectional | Friendships, roads |
| Directed | One-way | Twitter follows, dependencies |
| Weighted | Have costs | Road distances, network latency |
| Unweighted | Equal cost | Simple connectivity |

### Algorithms Complexity

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| BFS | O(V + E) | O(V) |
| DFS | O(V + E) | O(V) |
| Dijkstra | O((V + E) log V) | O(V) |
| Topological Sort | O(V + E) | O(V) |
| Union-Find | O(α(n)) per op | O(V) |
| Cycle Detection | O(V + E) | O(V) |

## Running the Code

### Run the comprehensive demo:
```bash
python application.py
```

### Run the unit tests:
```bash
python test_graph.py
```

### Example Usage:

#### Undirected Graph:
```python
from graph import Graph

g = Graph()

# Add edges
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)

# Traversals
print(g.bfs(0))  # [0, 1, 2, 3]
print(g.dfs(0))  # [0, 1, 3, 2] or similar

# Shortest path
path = g.shortest_path(0, 3)
print(path)  # [0, 1, 3]

# Properties
print(g.is_connected())  # True
print(g.has_cycle())  # False
```

#### Directed Graph:
```python
from graph import DirectedGraph

dg = DirectedGraph()

# Add directed edges
dg.add_edge(0, 1)
dg.add_edge(0, 2)
dg.add_edge(1, 3)
dg.add_edge(2, 3)

# Topological sort (for DAG)
topo = dg.topological_sort()
print(topo)  # [0, 2, 1, 3] or similar valid order

# Cycle detection
print(dg.has_cycle())  # False
```

#### Weighted Graph:
```python
from graph import WeightedGraph

wg = WeightedGraph()

# Add weighted edges
wg.add_edge(0, 1, 4)
wg.add_edge(0, 2, 1)
wg.add_edge(2, 3, 2)

# Dijkstra's algorithm
distances = wg.dijkstra(0)
print(distances)  # {0: 0, 1: 4, 2: 1, 3: 3}

# Shortest path
path, dist = wg.shortest_path(0, 3)
print(path, dist)  # [0, 2, 3], 3
```

## Assignment Instructions for Students

When adapting this for student assignments:

1. **Hide Core Functions**: Remove implementations of key methods
2. **Provide Template**: Give students the class structure with empty method bodies
3. **Include Tests**: Provide the test file for verification
4. **Progressive Difficulty**: 
   - Start with basic operations (add vertex, add edge)
   - Implement BFS and DFS
   - Add shortest path
   - Advanced: Dijkstra's, topological sort

### Student Implementation Template:

#### Basic Graph Template:
```python
class Graph:
    def __init__(self):
        self.adj_list = {}
        self._num_edges = 0
    
    def add_vertex(self, vertex):
        # TODO: Add vertex to graph
        # Check if vertex already exists
        pass
    
    def add_edge(self, u, v):
        # TODO: Add undirected edge
        # 1. Add vertices if they don't exist
        # 2. Add v to u's neighbors
        # 3. Add u to v's neighbors (undirected)
        # 4. Update edge count
        pass
    
    def bfs(self, start):
        # TODO: Breadth-first search
        # 1. Use queue (deque)
        # 2. Track visited vertices
        # 3. Process level by level
        pass
    
    def dfs(self, start):
        # TODO: Depth-first search
        # 1. Use recursion or stack
        # 2. Track visited vertices
        # 3. Go deep before wide
        pass
    
    def shortest_path(self, start, end):
        # TODO: Find shortest path using BFS
        # 1. Use BFS with path tracking
        # 2. Return path when end is reached
        pass
```

## Learning Objectives

By completing this assignment, students will:
1. Understand graph representations (adjacency list vs matrix)
2. Implement basic graph operations
3. Master BFS and DFS traversal algorithms
4. Apply graphs to solve real-world problems
5. Understand directed vs undirected graphs
6. Implement shortest path algorithms
7. Detect cycles and find connected components
8. Analyze time and space complexity

## Common Pitfalls for Students

1. **Undirected edges**: Forgetting to add edge in both directions
2. **Visited set**: Not tracking visited vertices in traversals
3. **Cycle detection**: Incorrect parent tracking in undirected graphs
4. **Dijkstra's**: Not using priority queue correctly
5. **Topological sort**: Not checking for cycles first
6. **Edge cases**: Not handling disconnected graphs
7. **Infinite loops**: In DFS without visited set

## Key Algorithms

### 1. Breadth-First Search (BFS)
```python
def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result
```

### 2. Depth-First Search (DFS)
```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    
    return result
```

### 3. Dijkstra's Algorithm
```python
def dijkstra(graph, start):
    dist = {v: float('inf') for v in graph}
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, vertex = heapq.heappop(pq)
        
        if d > dist[vertex]:
            continue
        
        for neighbor, weight in graph[vertex]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    return dist
```

### 4. Cycle Detection (Undirected)
```python
def has_cycle(graph):
    visited = set()
    
    def dfs(vertex, parent):
        visited.add(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                if dfs(neighbor, vertex):
                    return True
            elif neighbor != parent:
                return True  # Back edge
        
        return False
    
    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, None):
                return True
    
    return False
```

## Real-World Applications

### 1. Social Networks
- **Vertices**: Users
- **Edges**: Friendships, follows
- **Algorithms**: Friend recommendations, influence analysis, community detection

### 2. Maps and Navigation
- **Vertices**: Locations, intersections
- **Edges**: Roads with distances
- **Algorithms**: Shortest path (Dijkstra's, A*), route planning

### 3. Web and Internet
- **Vertices**: Web pages, routers
- **Edges**: Hyperlinks, connections
- **Algorithms**: PageRank, web crawling, network routing

### 4. Dependency Management
- **Vertices**: Packages, tasks
- **Edges**: Dependencies
- **Algorithms**: Topological sort, cycle detection

### 5. Recommendation Systems
- **Vertices**: Users, items
- **Edges**: Interactions, similarities
- **Algorithms**: Collaborative filtering, graph-based recommendations

## Comparison: Adjacency List vs Matrix

| Feature | Adjacency List | Adjacency Matrix |
|---------|----------------|------------------|
| Space | O(V + E) | O(V²) |
| Add edge | O(1) | O(1) |
| Check edge | O(degree) | O(1) |
| Get neighbors | O(degree) | O(V) |
| Best for | Sparse graphs | Dense graphs |
| Memory (1M vertices, 5M edges) | ~40 MB | ~1 TB |

### When to Use Each:
- **Adjacency List**: Most real-world graphs (social networks, web, roads)
- **Adjacency Matrix**: Dense graphs, need O(1) edge lookup, matrix operations

## Testing Your Implementation

Run the tests to verify your implementation:
```bash
python test_graph.py
```

Expected output:
```
test_add_edge (__main__.TestGraph) ... ok
test_bfs (__main__.TestGraph) ... ok
test_shortest_path (__main__.TestGraph) ... ok
...
----------------------------------------------------------------------
Ran 45 tests in 0.XXXs

OK
```

## Debugging Tips

1. **Visualize**: Draw the graph on paper
2. **Print state**: Print visited set and queue/stack
3. **Small examples**: Test with 3-4 vertices first
4. **Check directions**: Verify edge directions for directed graphs
5. **Trace algorithm**: Step through BFS/DFS manually
6. **Use debugger**: Set breakpoints in traversal loops
7. **Verify invariants**: Check visited set is updated correctly

## Grading Rubric (for Instructors)

| Component | Points | Criteria |
|-----------|--------|----------|
| Basic Operations | 15 | Add vertex, add edge, remove edge |
| BFS | 15 | Correct implementation |
| DFS | 15 | Correct implementation |
| Shortest Path | 15 | BFS-based shortest path |
| Directed Graph | 15 | Topological sort, cycle detection |
| Weighted Graph | 15 | Dijkstra's algorithm |
| Code Quality | 5 | Documentation, style |
| Testing | 5 | All tests pass |
| **Total** | **100** | |

## Advanced Topics (Extensions)

1. **Minimum Spanning Tree**: Kruskal's, Prim's algorithms
2. **Strongly Connected Components**: Kosaraju's, Tarjan's algorithms
3. **A* Search**: Heuristic-based pathfinding
4. **Bellman-Ford**: Shortest path with negative weights
5. **Floyd-Warshall**: All-pairs shortest paths
6. **Network Flow**: Max flow, min cut
7. **Graph Coloring**: Vertex coloring, chromatic number

## Common Interview Questions

1. Clone a graph
2. Course Schedule (topological sort)
3. Number of Islands (connected components)
4. Word Ladder (BFS shortest path)
5. Network Delay Time (Dijkstra's)
6. Alien Dictionary (topological sort)
7. Minimum Height Trees
8. Graph Valid Tree
9. Reconstruct Itinerary
10. Cheapest Flights Within K Stops

## Tips for Success

1. **Master BFS and DFS**: Foundation for most graph algorithms
2. **Draw pictures**: Visualize before coding
3. **Test incrementally**: Test each method as you implement
4. **Handle edge cases**: Empty graph, single vertex, disconnected
5. **Use visited set**: Prevent infinite loops
6. **Understand complexity**: Know when to use which algorithm
7. **Practice problems**: LeetCode graph problems
8. **Think about representation**: Choose right structure for problem

## Additional Resources

- **Visualization**: [VisuAlgo - Graph](https://visualgo.net/en/graphds)
- **Practice**: LeetCode graph tag problems
- **Reading**: "Introduction to Algorithms" (CLRS) - Graph Algorithms
- **Video**: MIT OpenCourseWare - Graph Algorithms

Good luck with your implementation!
