"""
Unit Tests for Graph Data Structures

This module provides comprehensive unit tests for graph implementations
and algorithms.

Author: Data Structure Course
Date: 2024
"""

import unittest
from graph import Graph, DirectedGraph, WeightedGraph, UnionFind


class TestGraph(unittest.TestCase):
    """Test cases for undirected Graph implementation."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.graph = Graph()
    
    def test_initialization(self):
        """Test graph initialization."""
        self.assertEqual(self.graph.num_vertices(), 0)
        self.assertEqual(self.graph.num_edges(), 0)
    
    def test_add_vertex(self):
        """Test adding vertices."""
        self.graph.add_vertex(0)
        self.assertEqual(self.graph.num_vertices(), 1)
        
        self.graph.add_vertex(1)
        self.assertEqual(self.graph.num_vertices(), 2)
    
    def test_add_edge(self):
        """Test adding edges."""
        self.graph.add_edge(0, 1)
        self.assertEqual(self.graph.num_edges(), 1)
        self.assertTrue(self.graph.has_edge(0, 1))
        self.assertTrue(self.graph.has_edge(1, 0))  # Undirected
    
    def test_add_duplicate_edge(self):
        """Test adding duplicate edges."""
        self.graph.add_edge(0, 1)
        self.graph.add_edge(0, 1)
        self.assertEqual(self.graph.num_edges(), 1)
    
    def test_remove_edge(self):
        """Test removing edges."""
        self.graph.add_edge(0, 1)
        self.graph.add_edge(1, 2)
        
        self.assertTrue(self.graph.remove_edge(0, 1))
        self.assertFalse(self.graph.has_edge(0, 1))
        self.assertEqual(self.graph.num_edges(), 1)
    
    def test_remove_nonexistent_edge(self):
        """Test removing non-existent edge."""
        self.assertFalse(self.graph.remove_edge(0, 1))
    
    def test_has_edge(self):
        """Test checking edge existence."""
        self.graph.add_edge(0, 1)
        self.assertTrue(self.graph.has_edge(0, 1))
        self.assertFalse(self.graph.has_edge(0, 2))
    
    def test_get_neighbors(self):
        """Test getting neighbors."""
        self.graph.add_edge(0, 1)
        self.graph.add_edge(0, 2)
        
        neighbors = self.graph.get_neighbors(0)
        self.assertEqual(set(neighbors), {1, 2})
    
    def test_degree(self):
        """Test vertex degree."""
        self.graph.add_edge(0, 1)
        self.graph.add_edge(0, 2)
        self.graph.add_edge(0, 3)
        
        self.assertEqual(self.graph.degree(0), 3)
        self.assertEqual(self.graph.degree(1), 1)
    
    def test_bfs(self):
        """Test breadth-first search."""
        # Create graph: 0-1-3
        #               |   |
        #               2-4
        edges = [(0, 1), (0, 2), (1, 3), (2, 4), (3, 4)]
        for u, v in edges:
            self.graph.add_edge(u, v)
        
        result = self.graph.bfs(0)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0], 0)
    
    def test_dfs(self):
        """Test depth-first search."""
        edges = [(0, 1), (0, 2), (1, 3), (2, 4)]
        for u, v in edges:
            self.graph.add_edge(u, v)
        
        result = self.graph.dfs(0)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0], 0)
    
    def test_shortest_path(self):
        """Test shortest path finding."""
        edges = [(0, 1), (1, 2), (2, 3), (0, 3)]
        for u, v in edges:
            self.graph.add_edge(u, v)
        
        path = self.graph.shortest_path(0, 3)
        self.assertIsNotNone(path)
        self.assertEqual(path[0], 0)
        self.assertEqual(path[-1], 3)
        self.assertEqual(len(path), 2)  # Direct path
    
    def test_shortest_path_no_path(self):
        """Test shortest path when no path exists."""
        self.graph.add_edge(0, 1)
        self.graph.add_edge(2, 3)
        
        path = self.graph.shortest_path(0, 3)
        self.assertIsNone(path)
    
    def test_is_connected(self):
        """Test connectivity check."""
        # Connected graph
        self.graph.add_edge(0, 1)
        self.graph.add_edge(1, 2)
        self.assertTrue(self.graph.is_connected())
        
        # Disconnected graph
        self.graph.add_vertex(3)
        self.assertFalse(self.graph.is_connected())
    
    def test_find_components(self):
        """Test finding connected components."""
        # Component 1: 0-1
        self.graph.add_edge(0, 1)
        
        # Component 2: 2-3-4
        self.graph.add_edge(2, 3)
        self.graph.add_edge(3, 4)
        
        # Component 3: 5 (isolated)
        self.graph.add_vertex(5)
        
        components = self.graph.find_components()
        self.assertEqual(len(components), 3)
    
    def test_has_cycle_true(self):
        """Test cycle detection when cycle exists."""
        self.graph.add_edge(0, 1)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(2, 0)
        
        self.assertTrue(self.graph.has_cycle())
    
    def test_has_cycle_false(self):
        """Test cycle detection when no cycle exists."""
        self.graph.add_edge(0, 1)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(2, 3)
        
        self.assertFalse(self.graph.has_cycle())


class TestDirectedGraph(unittest.TestCase):
    """Test cases for DirectedGraph implementation."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.graph = DirectedGraph()
    
    def test_initialization(self):
        """Test directed graph initialization."""
        self.assertEqual(self.graph.num_vertices(), 0)
        self.assertEqual(self.graph.num_edges(), 0)
    
    def test_add_directed_edge(self):
        """Test adding directed edges."""
        self.graph.add_edge(0, 1)
        
        self.assertTrue(self.graph.has_edge(0, 1))
        self.assertFalse(self.graph.has_edge(1, 0))  # Directed
    
    def test_out_degree(self):
        """Test out-degree calculation."""
        self.graph.add_edge(0, 1)
        self.graph.add_edge(0, 2)
        self.graph.add_edge(1, 2)
        
        self.assertEqual(self.graph.out_degree(0), 2)
        self.assertEqual(self.graph.out_degree(1), 1)
        self.assertEqual(self.graph.out_degree(2), 0)
    
    def test_in_degree(self):
        """Test in-degree calculation."""
        self.graph.add_edge(0, 1)
        self.graph.add_edge(0, 2)
        self.graph.add_edge(1, 2)
        
        self.assertEqual(self.graph.in_degree(0), 0)
        self.assertEqual(self.graph.in_degree(1), 1)
        self.assertEqual(self.graph.in_degree(2), 2)
    
    def test_has_cycle_dag(self):
        """Test cycle detection in DAG."""
        # Create DAG
        self.graph.add_edge(0, 1)
        self.graph.add_edge(0, 2)
        self.graph.add_edge(1, 3)
        self.graph.add_edge(2, 3)
        
        self.assertFalse(self.graph.has_cycle())
    
    def test_has_cycle_with_cycle(self):
        """Test cycle detection when cycle exists."""
        self.graph.add_edge(0, 1)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(2, 0)
        
        self.assertTrue(self.graph.has_cycle())
    
    def test_topological_sort_dag(self):
        """Test topological sort on DAG."""
        # Create DAG
        self.graph.add_edge(0, 1)
        self.graph.add_edge(0, 2)
        self.graph.add_edge(1, 3)
        self.graph.add_edge(2, 3)
        
        topo = self.graph.topological_sort()
        self.assertIsNotNone(topo)
        self.assertEqual(len(topo), 4)
        
        # Verify order (0 before 1 and 2, 1 and 2 before 3)
        self.assertLess(topo.index(0), topo.index(1))
        self.assertLess(topo.index(0), topo.index(2))
        self.assertLess(topo.index(1), topo.index(3))
        self.assertLess(topo.index(2), topo.index(3))
    
    def test_topological_sort_with_cycle(self):
        """Test topological sort with cycle."""
        self.graph.add_edge(0, 1)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(2, 0)
        
        topo = self.graph.topological_sort()
        self.assertIsNone(topo)


class TestWeightedGraph(unittest.TestCase):
    """Test cases for WeightedGraph implementation."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.graph = WeightedGraph()
    
    def test_initialization(self):
        """Test weighted graph initialization."""
        self.assertEqual(self.graph.num_vertices(), 0)
        self.assertEqual(self.graph.num_edges(), 0)
    
    def test_add_weighted_edge(self):
        """Test adding weighted edges."""
        self.graph.add_edge(0, 1, 5)
        self.assertEqual(self.graph.num_edges(), 1)
        
        neighbors = self.graph.get_neighbors(0)
        self.assertEqual(len(neighbors), 1)
        self.assertEqual(neighbors[0], (1, 5))
    
    def test_dijkstra_single_source(self):
        """Test Dijkstra's algorithm."""
        # Create weighted graph
        self.graph.add_edge(0, 1, 4)
        self.graph.add_edge(0, 2, 1)
        self.graph.add_edge(1, 3, 5)
        self.graph.add_edge(2, 3, 2)
        
        distances = self.graph.dijkstra(0)
        
        self.assertEqual(distances[0], 0)
        self.assertEqual(distances[1], 4)
        self.assertEqual(distances[2], 1)
        self.assertEqual(distances[3], 3)  # Via 2
    
    def test_dijkstra_to_target(self):
        """Test Dijkstra's algorithm to specific target."""
        self.graph.add_edge(0, 1, 4)
        self.graph.add_edge(0, 2, 1)
        self.graph.add_edge(2, 3, 2)
        
        distance = self.graph.dijkstra(0, 3)
        self.assertEqual(distance, 3)
    
    def test_shortest_path_weighted(self):
        """Test shortest path in weighted graph."""
        self.graph.add_edge(0, 1, 4)
        self.graph.add_edge(0, 2, 1)
        self.graph.add_edge(1, 3, 5)
        self.graph.add_edge(2, 3, 2)
        
        path, distance = self.graph.shortest_path(0, 3)
        
        self.assertIsNotNone(path)
        self.assertEqual(path[0], 0)
        self.assertEqual(path[-1], 3)
        self.assertEqual(distance, 3)
    
    def test_shortest_path_no_path(self):
        """Test shortest path when no path exists."""
        self.graph.add_edge(0, 1, 5)
        self.graph.add_edge(2, 3, 5)
        
        path, distance = self.graph.shortest_path(0, 3)
        
        self.assertIsNone(path)
        self.assertEqual(distance, float('inf'))


class TestUnionFind(unittest.TestCase):
    """Test cases for UnionFind implementation."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.uf = UnionFind([0, 1, 2, 3, 4])
    
    def test_initialization(self):
        """Test Union-Find initialization."""
        self.assertEqual(self.uf.count_components(), 5)
    
    def test_find(self):
        """Test find operation."""
        # Initially, each element is its own parent
        self.assertEqual(self.uf.find(0), 0)
        self.assertEqual(self.uf.find(1), 1)
    
    def test_union(self):
        """Test union operation."""
        self.assertTrue(self.uf.union(0, 1))
        self.assertEqual(self.uf.count_components(), 4)
        
        self.assertTrue(self.uf.union(2, 3))
        self.assertEqual(self.uf.count_components(), 3)
    
    def test_union_same_set(self):
        """Test union of elements in same set."""
        self.uf.union(0, 1)
        self.assertFalse(self.uf.union(0, 1))
        self.assertEqual(self.uf.count_components(), 4)
    
    def test_connected(self):
        """Test connectivity check."""
        self.assertFalse(self.uf.connected(0, 1))
        
        self.uf.union(0, 1)
        self.assertTrue(self.uf.connected(0, 1))
        
        self.uf.union(1, 2)
        self.assertTrue(self.uf.connected(0, 2))
    
    def test_path_compression(self):
        """Test that path compression works."""
        # Create chain: 0 -> 1 -> 2 -> 3
        self.uf.union(0, 1)
        self.uf.union(1, 2)
        self.uf.union(2, 3)
        
        # All should have same root
        root = self.uf.find(0)
        self.assertEqual(self.uf.find(1), root)
        self.assertEqual(self.uf.find(2), root)
        self.assertEqual(self.uf.find(3), root)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases for graph structures."""
    
    def test_empty_graph(self):
        """Test operations on empty graph."""
        g = Graph()
        
        self.assertEqual(g.num_vertices(), 0)
        self.assertEqual(g.num_edges(), 0)
        self.assertTrue(g.is_connected())
        self.assertEqual(g.find_components(), [])
    
    def test_single_vertex(self):
        """Test graph with single vertex."""
        g = Graph()
        g.add_vertex(0)
        
        self.assertEqual(g.num_vertices(), 1)
        self.assertEqual(g.degree(0), 0)
        self.assertTrue(g.is_connected())
        self.assertFalse(g.has_cycle())
    
    def test_self_loop(self):
        """Test self-loop edge."""
        g = Graph()
        g.add_edge(0, 0)
        
        self.assertTrue(g.has_edge(0, 0))
        self.assertTrue(g.has_cycle())
    
    def test_large_graph(self):
        """Test with large graph."""
        g = Graph()
        
        # Create chain of 1000 vertices
        for i in range(999):
            g.add_edge(i, i + 1)
        
        self.assertEqual(g.num_vertices(), 1000)
        self.assertEqual(g.num_edges(), 999)
        self.assertTrue(g.is_connected())
    
    def test_complete_graph(self):
        """Test complete graph (all pairs connected)."""
        g = Graph()
        n = 5
        
        for i in range(n):
            for j in range(i + 1, n):
                g.add_edge(i, j)
        
        self.assertEqual(g.num_edges(), n * (n - 1) // 2)
        self.assertTrue(g.is_connected())
        self.assertTrue(g.has_cycle())
    
    def test_weighted_zero_weight(self):
        """Test weighted graph with zero weights."""
        wg = WeightedGraph()
        wg.add_edge(0, 1, 0)
        wg.add_edge(1, 2, 0)
        
        distance = wg.dijkstra(0, 2)
        self.assertEqual(distance, 0)
    
    def test_directed_graph_reverse_edges(self):
        """Test directed graph with reverse edges."""
        dg = DirectedGraph()
        dg.add_edge(0, 1)
        dg.add_edge(1, 0)
        
        self.assertTrue(dg.has_edge(0, 1))
        self.assertTrue(dg.has_edge(1, 0))
        self.assertTrue(dg.has_cycle())


def run_tests():
    """Run all tests."""
    unittest.main(verbosity=2)


if __name__ == '__main__':
    run_tests()
