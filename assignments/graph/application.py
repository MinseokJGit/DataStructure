"""
Graph Applications Demo

This module demonstrates practical applications of graph data structures
including social networks, route finding, dependency resolution, and more.

Author: Data Structure Course
Date: 2024
"""

from graph import Graph, DirectedGraph, WeightedGraph, UnionFind
import time


class SocialNetwork:
    """
    Social network implementation using undirected graph.
    """
    
    def __init__(self):
        """Initialize empty social network."""
        self.graph = Graph()
        self.users = {}  # username -> user info
    
    def add_user(self, username, name):
        """Add a user to the network."""
        self.graph.add_vertex(username)
        self.users[username] = {'name': name, 'friends': set()}
        print(f"Added user: {name} (@{username})")
    
    def add_friendship(self, user1, user2):
        """Create friendship between two users."""
        self.graph.add_edge(user1, user2)
        self.users[user1]['friends'].add(user2)
        self.users[user2]['friends'].add(user1)
        print(f"  {user1} and {user2} are now friends")
    
    def recommend_friends(self, username):
        """
        Recommend friends (friends of friends).
        
        Args:
            username: User to recommend friends for
            
        Returns:
            list: Recommended usernames
        """
        if username not in self.graph.adj_list:
            return []
        
        friends = set(self.graph.get_neighbors(username))
        recommendations = set()
        
        for friend in friends:
            for friend_of_friend in self.graph.get_neighbors(friend):
                if friend_of_friend != username and friend_of_friend not in friends:
                    recommendations.add(friend_of_friend)
        
        return list(recommendations)
    
    def degrees_of_separation(self, user1, user2):
        """
        Find degrees of separation between two users.
        
        Returns:
            int: Number of connections, or -1 if not connected
        """
        path = self.graph.shortest_path(user1, user2)
        return len(path) - 1 if path else -1
    
    def find_influencers(self, top_k=3):
        """
        Find most connected users.
        
        Returns:
            list: Top k users by number of friends
        """
        degrees = [(user, self.graph.degree(user)) for user in self.graph.adj_list]
        degrees.sort(key=lambda x: x[1], reverse=True)
        return degrees[:top_k]


class RouteMap:
    """
    Route/map system using weighted graph.
    """
    
    def __init__(self):
        """Initialize empty map."""
        self.graph = WeightedGraph()
        self.locations = {}
    
    def add_location(self, name):
        """Add a location to the map."""
        self.graph.add_vertex(name)
        self.locations[name] = True
        print(f"Added location: {name}")
    
    def add_route(self, loc1, loc2, distance):
        """
        Add a route between two locations.
        
        Args:
            loc1: First location
            loc2: Second location
            distance: Distance in km
        """
        self.graph.add_edge(loc1, loc2, distance)
        print(f"  Route: {loc1} <-> {loc2} ({distance} km)")
    
    def find_shortest_route(self, start, end):
        """
        Find shortest route between two locations.
        
        Returns:
            tuple: (path, distance)
        """
        return self.graph.shortest_path(start, end)
    
    def find_all_distances(self, start):
        """
        Find distances from start to all other locations.
        
        Returns:
            dict: location -> distance
        """
        return self.graph.dijkstra(start)


class DependencyResolver:
    """
    Dependency resolution system using directed graph.
    """
    
    def __init__(self):
        """Initialize empty dependency graph."""
        self.graph = DirectedGraph()
        self.packages = set()
    
    def add_package(self, package):
        """Add a package."""
        self.graph.add_vertex(package)
        self.packages.add(package)
        print(f"Added package: {package}")
    
    def add_dependency(self, package, depends_on):
        """
        Add dependency: package depends on depends_on.
        
        Args:
            package: Package name
            depends_on: Dependency name
        """
        self.graph.add_edge(package, depends_on)
        print(f"  {package} depends on {depends_on}")
    
    def get_install_order(self):
        """
        Get installation order using topological sort.
        
        Returns:
            list: Packages in installation order, or None if circular dependency
        """
        order = self.graph.topological_sort()
        if order is None:
            print("ERROR: Circular dependency detected!")
            return None
        
        # Reverse to get install order (dependencies first)
        return order[::-1]
    
    def has_circular_dependency(self):
        """Check if there are circular dependencies."""
        return self.graph.has_cycle()


def demo_basic_operations():
    """Demonstrate basic graph operations."""
    print("=== BASIC GRAPH OPERATIONS ===\n")
    
    # Undirected graph
    print("Undirected Graph:")
    g = Graph()
    
    # Add vertices and edges
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4)]
    for u, v in edges:
        g.add_edge(u, v)
    
    print(f"Vertices: {g.get_vertices()}")
    print(f"Edges: {g.num_edges()}")
    print(f"Neighbors of 1: {g.get_neighbors(1)}")
    print(f"Degree of 1: {g.degree(1)}")
    print(f"Has edge (1, 3): {g.has_edge(1, 3)}")
    print(f"Has edge (0, 3): {g.has_edge(0, 3)}")
    
    # Traversals
    print(f"\nBFS from 0: {g.bfs(0)}")
    print(f"DFS from 0: {g.dfs(0)}")
    
    # Shortest path
    path = g.shortest_path(0, 4)
    print(f"Shortest path 0 -> 4: {path}")
    
    # Connected components
    print(f"Is connected: {g.is_connected()}")
    print(f"Has cycle: {g.has_cycle()}")
    
    print("\n" + "="*50 + "\n")


def demo_directed_graph():
    """Demonstrate directed graph."""
    print("=== DIRECTED GRAPH ===\n")
    
    dg = DirectedGraph()
    
    # Add edges (directed)
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
    for u, v in edges:
        dg.add_edge(u, v)
    
    print(f"Vertices: {dg.get_vertices()}")
    print(f"Edges: {dg.num_edges()}")
    
    print(f"\nOut-degree of 0: {dg.out_degree(0)}")
    print(f"In-degree of 3: {dg.in_degree(3)}")
    
    print(f"\nBFS from 0: {dg.bfs(0)}")
    print(f"DFS from 0: {dg.dfs(0)}")
    
    print(f"\nHas cycle: {dg.has_cycle()}")
    
    # Topological sort
    topo = dg.topological_sort()
    print(f"Topological sort: {topo}")
    
    print("\n" + "="*50 + "\n")


def demo_weighted_graph():
    """Demonstrate weighted graph."""
    print("=== WEIGHTED GRAPH ===\n")
    
    wg = WeightedGraph()
    
    # Add weighted edges
    edges = [
        (0, 1, 4), (0, 2, 1),
        (1, 3, 5), (2, 3, 2),
        (2, 4, 4), (3, 4, 1)
    ]
    
    for u, v, w in edges:
        wg.add_edge(u, v, w)
    
    print("Graph with weighted edges:")
    for u, v, w in edges:
        print(f"  {u} -- {v} (weight: {w})")
    
    # Dijkstra's algorithm
    print(f"\nShortest distances from 0:")
    distances = wg.dijkstra(0)
    for vertex, dist in sorted(distances.items()):
        print(f"  To {vertex}: {dist}")
    
    # Shortest path
    path, dist = wg.shortest_path(0, 4)
    print(f"\nShortest path 0 -> 4: {path} (distance: {dist})")
    
    print("\n" + "="*50 + "\n")


def demo_social_network():
    """Demonstrate social network."""
    print("=== SOCIAL NETWORK ===\n")
    
    network = SocialNetwork()
    
    # Add users
    users = [
        ("alice", "Alice Smith"),
        ("bob", "Bob Johnson"),
        ("charlie", "Charlie Brown"),
        ("david", "David Wilson"),
        ("eve", "Eve Davis")
    ]
    
    for username, name in users:
        network.add_user(username, name)
    
    print("\nCreating friendships:")
    friendships = [
        ("alice", "bob"),
        ("alice", "charlie"),
        ("bob", "david"),
        ("charlie", "david"),
        ("david", "eve")
    ]
    
    for user1, user2 in friendships:
        network.add_friendship(user1, user2)
    
    # Friend recommendations
    print(f"\nFriend recommendations for Bob:")
    recommendations = network.recommend_friends("bob")
    for rec in recommendations:
        print(f"  - {rec}")
    
    # Degrees of separation
    print(f"\nDegrees of separation:")
    print(f"  Alice to Eve: {network.degrees_of_separation('alice', 'eve')}")
    print(f"  Bob to Charlie: {network.degrees_of_separation('bob', 'charlie')}")
    
    # Find influencers
    print(f"\nTop influencers:")
    influencers = network.find_influencers(3)
    for user, friends_count in influencers:
        print(f"  {user}: {friends_count} friends")
    
    print("\n" + "="*50 + "\n")


def demo_route_map():
    """Demonstrate route finding."""
    print("=== ROUTE MAP (GPS NAVIGATION) ===\n")
    
    map_system = RouteMap()
    
    # Add locations
    cities = ["NYC", "Boston", "Philadelphia", "Washington", "Baltimore"]
    for city in cities:
        map_system.add_location(city)
    
    print("\nAdding routes:")
    routes = [
        ("NYC", "Boston", 215),
        ("NYC", "Philadelphia", 95),
        ("Philadelphia", "Washington", 140),
        ("Philadelphia", "Baltimore", 100),
        ("Baltimore", "Washington", 40)
    ]
    
    for loc1, loc2, dist in routes:
        map_system.add_route(loc1, loc2, dist)
    
    # Find shortest route
    print(f"\nShortest route from NYC to Washington:")
    path, distance = map_system.find_shortest_route("NYC", "Washington")
    if path:
        print(f"  Path: {' -> '.join(path)}")
        print(f"  Distance: {distance} km")
    
    # All distances from NYC
    print(f"\nAll distances from NYC:")
    distances = map_system.find_all_distances("NYC")
    for city, dist in sorted(distances.items()):
        if dist != float('inf'):
            print(f"  To {city}: {dist} km")
    
    print("\n" + "="*50 + "\n")


def demo_dependency_resolver():
    """Demonstrate dependency resolution."""
    print("=== DEPENDENCY RESOLVER ===\n")
    
    resolver = DependencyResolver()
    
    # Add packages
    packages = ["app", "web", "database", "auth", "utils"]
    for pkg in packages:
        resolver.add_package(pkg)
    
    print("\nAdding dependencies:")
    dependencies = [
        ("app", "web"),
        ("app", "database"),
        ("web", "auth"),
        ("web", "utils"),
        ("database", "utils"),
        ("auth", "utils")
    ]
    
    for pkg, dep in dependencies:
        resolver.add_dependency(pkg, dep)
    
    # Get install order
    print(f"\nInstallation order:")
    order = resolver.get_install_order()
    if order:
        for i, pkg in enumerate(order, 1):
            print(f"  {i}. {pkg}")
    
    # Check for circular dependencies
    print(f"\nHas circular dependency: {resolver.has_circular_dependency()}")
    
    # Add circular dependency
    print("\nAdding circular dependency (app -> utils -> app):")
    resolver.add_dependency("utils", "app")
    print(f"Has circular dependency: {resolver.has_circular_dependency()}")
    
    print("\n" + "="*50 + "\n")


def demo_connected_components():
    """Demonstrate connected components."""
    print("=== CONNECTED COMPONENTS ===\n")
    
    g = Graph()
    
    # Create disconnected graph
    # Component 1: 0-1-2
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    
    # Component 2: 3-4
    g.add_edge(3, 4)
    
    # Component 3: 5 (isolated)
    g.add_vertex(5)
    
    print("Graph with 3 components:")
    print("  Component 1: 0-1-2")
    print("  Component 2: 3-4")
    print("  Component 3: 5 (isolated)")
    
    components = g.find_components()
    print(f"\nFound {len(components)} components:")
    for i, comp in enumerate(components, 1):
        print(f"  Component {i}: {comp}")
    
    print(f"\nIs graph connected: {g.is_connected()}")
    
    print("\n" + "="*50 + "\n")


def demo_union_find():
    """Demonstrate Union-Find."""
    print("=== UNION-FIND (DISJOINT SET) ===\n")
    
    vertices = [0, 1, 2, 3, 4, 5]
    uf = UnionFind(vertices)
    
    print(f"Initial components: {uf.count_components()}")
    
    # Union operations
    print("\nPerforming unions:")
    unions = [(0, 1), (1, 2), (3, 4)]
    
    for x, y in unions:
        uf.union(x, y)
        print(f"  Union({x}, {y}) -> {uf.count_components()} components")
    
    # Check connections
    print(f"\nConnectivity checks:")
    checks = [(0, 2), (0, 3), (3, 4)]
    for x, y in checks:
        connected = uf.connected(x, y)
        print(f"  {x} and {y}: {'Connected' if connected else 'Not connected'}")
    
    print("\n" + "="*50 + "\n")


def demo_cycle_detection():
    """Demonstrate cycle detection."""
    print("=== CYCLE DETECTION ===\n")
    
    # Undirected graph without cycle
    print("Undirected graph (tree):")
    g1 = Graph()
    g1.add_edge(0, 1)
    g1.add_edge(0, 2)
    g1.add_edge(1, 3)
    print(f"  Has cycle: {g1.has_cycle()}")
    
    # Undirected graph with cycle
    print("\nUndirected graph (with cycle):")
    g2 = Graph()
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 0)
    print(f"  Has cycle: {g2.has_cycle()}")
    
    # Directed graph without cycle (DAG)
    print("\nDirected graph (DAG):")
    dg1 = DirectedGraph()
    dg1.add_edge(0, 1)
    dg1.add_edge(0, 2)
    dg1.add_edge(1, 3)
    dg1.add_edge(2, 3)
    print(f"  Has cycle: {dg1.has_cycle()}")
    
    # Directed graph with cycle
    print("\nDirected graph (with cycle):")
    dg2 = DirectedGraph()
    dg2.add_edge(0, 1)
    dg2.add_edge(1, 2)
    dg2.add_edge(2, 0)
    print(f"  Has cycle: {dg2.has_cycle()}")
    
    print("\n" + "="*50 + "\n")


def demo_performance():
    """Demonstrate performance characteristics."""
    print("=== PERFORMANCE COMPARISON ===\n")
    
    # Create graphs of different sizes
    sizes = [100, 500, 1000]
    
    print("BFS Performance:")
    print(f"{'Size':<10} {'Time (s)':<15}")
    print("-" * 25)
    
    for size in sizes:
        g = Graph()
        
        # Create a connected graph
        for i in range(size - 1):
            g.add_edge(i, i + 1)
        
        start = time.time()
        g.bfs(0)
        elapsed = time.time() - start
        
        print(f"{size:<10} {elapsed:<15.6f}")
    
    print("\nKey observations:")
    print("- BFS/DFS: O(V + E) time complexity")
    print("- Adjacency list: O(V + E) space")
    print("- Efficient for sparse graphs")
    
    print("\n" + "="*50 + "\n")


def main():
    """Run all demonstrations."""
    print("GRAPH DATA STRUCTURE - COMPREHENSIVE DEMO")
    print("="*50)
    print()
    
    demo_basic_operations()
    demo_directed_graph()
    demo_weighted_graph()
    demo_social_network()
    demo_route_map()
    demo_dependency_resolver()
    demo_connected_components()
    demo_union_find()
    demo_cycle_detection()
    demo_performance()
    
    print("All demonstrations completed!")


if __name__ == "__main__":
    main()
