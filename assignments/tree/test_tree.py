"""
Unit Tests for Tree Data Structures

This module provides comprehensive unit tests for BST, AVL Tree, and Heap
implementations.

Author: Data Structure Course
Date: 2024
"""

import unittest
from tree import (
    BinarySearchTree, AVLTree, MinHeap, MaxHeap, TreeNode,
    build_tree_from_list, tree_to_list, lowest_common_ancestor
)


class TestBinarySearchTree(unittest.TestCase):
    """Test cases for BinarySearchTree implementation."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.bst = BinarySearchTree()
    
    def test_initialization(self):
        """Test tree initialization."""
        self.assertTrue(self.bst.is_empty())
        self.assertEqual(self.bst.size(), 0)
        self.assertIsNone(self.bst.root)
    
    def test_insert(self):
        """Test insertion."""
        self.bst.insert(50)
        self.assertFalse(self.bst.is_empty())
        self.assertEqual(self.bst.size(), 1)
        self.assertEqual(self.bst.root.val, 50)
        
        self.bst.insert(30)
        self.bst.insert(70)
        self.assertEqual(self.bst.size(), 3)
    
    def test_search(self):
        """Test search operation."""
        values = [50, 30, 70, 20, 40, 60, 80]
        for val in values:
            self.bst.insert(val)
        
        self.assertIsNotNone(self.bst.search(50))
        self.assertIsNotNone(self.bst.search(30))
        self.assertIsNotNone(self.bst.search(80))
        self.assertIsNone(self.bst.search(100))
    
    def test_delete_leaf(self):
        """Test deleting leaf node."""
        values = [50, 30, 70, 20, 40]
        for val in values:
            self.bst.insert(val)
        
        self.assertTrue(self.bst.delete(20))
        self.assertIsNone(self.bst.search(20))
        self.assertEqual(self.bst.size(), 4)
    
    def test_delete_one_child(self):
        """Test deleting node with one child."""
        values = [50, 30, 70, 20]
        for val in values:
            self.bst.insert(val)
        
        self.assertTrue(self.bst.delete(30))
        self.assertIsNone(self.bst.search(30))
        self.assertIsNotNone(self.bst.search(20))
    
    def test_delete_two_children(self):
        """Test deleting node with two children."""
        values = [50, 30, 70, 20, 40, 60, 80]
        for val in values:
            self.bst.insert(val)
        
        self.assertTrue(self.bst.delete(50))
        self.assertIsNone(self.bst.search(50))
        # Tree should still be valid BST
        self.assertTrue(self.bst.is_valid_bst())
    
    def test_delete_nonexistent(self):
        """Test deleting non-existent value."""
        self.bst.insert(50)
        self.assertFalse(self.bst.delete(100))
        self.assertEqual(self.bst.size(), 1)
    
    def test_find_min_max(self):
        """Test finding minimum and maximum."""
        values = [50, 30, 70, 20, 40, 60, 80]
        for val in values:
            self.bst.insert(val)
        
        self.assertEqual(self.bst.find_min(), 20)
        self.assertEqual(self.bst.find_max(), 80)
    
    def test_find_min_max_empty(self):
        """Test min/max on empty tree."""
        self.assertIsNone(self.bst.find_min())
        self.assertIsNone(self.bst.find_max())
    
    def test_inorder_traversal(self):
        """Test inorder traversal (should be sorted)."""
        values = [50, 30, 70, 20, 40, 60, 80]
        for val in values:
            self.bst.insert(val)
        
        result = self.bst.inorder_traversal()
        self.assertEqual(result, [20, 30, 40, 50, 60, 70, 80])
    
    def test_preorder_traversal(self):
        """Test preorder traversal."""
        values = [50, 30, 70, 20, 40, 60, 80]
        for val in values:
            self.bst.insert(val)
        
        result = self.bst.preorder_traversal()
        self.assertEqual(result, [50, 30, 20, 40, 70, 60, 80])
    
    def test_postorder_traversal(self):
        """Test postorder traversal."""
        values = [50, 30, 70, 20, 40, 60, 80]
        for val in values:
            self.bst.insert(val)
        
        result = self.bst.postorder_traversal()
        self.assertEqual(result, [20, 40, 30, 60, 80, 70, 50])
    
    def test_level_order_traversal(self):
        """Test level-order traversal."""
        values = [50, 30, 70, 20, 40, 60, 80]
        for val in values:
            self.bst.insert(val)
        
        result = self.bst.level_order_traversal()
        self.assertEqual(result, [50, 30, 70, 20, 40, 60, 80])
    
    def test_height(self):
        """Test height calculation."""
        self.assertEqual(self.bst.height(), -1)  # Empty tree
        
        self.bst.insert(50)
        self.assertEqual(self.bst.height(), 0)
        
        self.bst.insert(30)
        self.bst.insert(70)
        self.assertEqual(self.bst.height(), 1)
        
        self.bst.insert(20)
        self.assertEqual(self.bst.height(), 2)
    
    def test_is_balanced(self):
        """Test balance checking."""
        # Balanced tree
        for val in [50, 30, 70, 20, 40]:
            self.bst.insert(val)
        self.assertTrue(self.bst.is_balanced())
        
        # Unbalanced tree
        bst2 = BinarySearchTree()
        for i in range(1, 6):
            bst2.insert(i)
        self.assertFalse(bst2.is_balanced())
    
    def test_is_valid_bst(self):
        """Test BST validation."""
        values = [50, 30, 70, 20, 40, 60, 80]
        for val in values:
            self.bst.insert(val)
        
        self.assertTrue(self.bst.is_valid_bst())
    
    def test_clear(self):
        """Test clearing the tree."""
        for i in range(5):
            self.bst.insert(i)
        
        self.bst.clear()
        self.assertTrue(self.bst.is_empty())
        self.assertEqual(self.bst.size(), 0)


class TestAVLTree(unittest.TestCase):
    """Test cases for AVLTree implementation."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.avl = AVLTree()
    
    def test_initialization(self):
        """Test tree initialization."""
        self.assertIsNone(self.avl.root)
        self.assertEqual(self.avl.size(), 0)
    
    def test_insert_and_balance(self):
        """Test insertion with automatic balancing."""
        # Insert sequential values (would be skewed in regular BST)
        for i in range(1, 8):
            self.avl.insert(i)
        
        # Check that tree is balanced
        height = self.avl._get_height(self.avl.root)
        self.assertLessEqual(height, 3)  # Should be log2(7) ≈ 2.8
        
        # Check inorder is still sorted
        result = self.avl.inorder_traversal()
        self.assertEqual(result, list(range(1, 8)))
    
    def test_left_rotation(self):
        """Test left rotation case."""
        # Insert in ascending order triggers left rotations
        for i in [1, 2, 3]:
            self.avl.insert(i)
        
        # Root should be 2 after rotation
        self.assertEqual(self.avl.root.val, 2)
        self.assertEqual(self.avl.root.left.val, 1)
        self.assertEqual(self.avl.root.right.val, 3)
    
    def test_right_rotation(self):
        """Test right rotation case."""
        # Insert in descending order triggers right rotations
        for i in [3, 2, 1]:
            self.avl.insert(i)
        
        # Root should be 2 after rotation
        self.assertEqual(self.avl.root.val, 2)
    
    def test_balance_factor(self):
        """Test balance factor calculation."""
        self.avl.insert(10)
        self.avl.insert(5)
        self.avl.insert(15)
        
        # Balance factor should be between -1 and 1
        balance = self.avl._get_balance(self.avl.root)
        self.assertIn(balance, [-1, 0, 1])


class TestMinHeap(unittest.TestCase):
    """Test cases for MinHeap implementation."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.heap = MinHeap()
    
    def test_initialization(self):
        """Test heap initialization."""
        self.assertTrue(self.heap.is_empty())
        self.assertEqual(self.heap.size(), 0)
    
    def test_insert(self):
        """Test insertion."""
        self.heap.insert(5)
        self.assertEqual(self.heap.peek(), 5)
        
        self.heap.insert(3)
        self.assertEqual(self.heap.peek(), 3)
        
        self.heap.insert(7)
        self.assertEqual(self.heap.peek(), 3)
    
    def test_extract_min(self):
        """Test extracting minimum."""
        values = [5, 3, 7, 1, 9, 4, 6]
        for val in values:
            self.heap.insert(val)
        
        # Extract in sorted order
        result = []
        while not self.heap.is_empty():
            result.append(self.heap.extract_min())
        
        self.assertEqual(result, sorted(values))
    
    def test_extract_min_empty(self):
        """Test extracting from empty heap."""
        with self.assertRaises(IndexError):
            self.heap.extract_min()
    
    def test_peek(self):
        """Test peek operation."""
        self.assertIsNone(self.heap.peek())
        
        self.heap.insert(5)
        self.assertEqual(self.heap.peek(), 5)
        self.assertEqual(self.heap.size(), 1)  # Size unchanged
    
    def test_build_heap(self):
        """Test building heap from array."""
        arr = [9, 5, 6, 2, 3, 7, 1, 4, 8]
        self.heap.build_heap(arr)
        
        # Extract all and verify sorted
        result = []
        while not self.heap.is_empty():
            result.append(self.heap.extract_min())
        
        self.assertEqual(result, sorted(arr))
    
    def test_heap_property(self):
        """Test that heap property is maintained."""
        values = [5, 3, 7, 1, 9, 4, 6]
        for val in values:
            self.heap.insert(val)
        
        # Check heap property: parent <= children
        for i in range(len(self.heap.heap)):
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < len(self.heap.heap):
                self.assertLessEqual(self.heap.heap[i], self.heap.heap[left])
            
            if right < len(self.heap.heap):
                self.assertLessEqual(self.heap.heap[i], self.heap.heap[right])


class TestMaxHeap(unittest.TestCase):
    """Test cases for MaxHeap implementation."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.heap = MaxHeap()
    
    def test_initialization(self):
        """Test heap initialization."""
        self.assertTrue(self.heap.is_empty())
        self.assertEqual(self.heap.size(), 0)
    
    def test_insert(self):
        """Test insertion."""
        self.heap.insert(5)
        self.assertEqual(self.heap.peek(), 5)
        
        self.heap.insert(3)
        self.assertEqual(self.heap.peek(), 5)
        
        self.heap.insert(7)
        self.assertEqual(self.heap.peek(), 7)
    
    def test_extract_max(self):
        """Test extracting maximum."""
        values = [5, 3, 7, 1, 9, 4, 6]
        for val in values:
            self.heap.insert(val)
        
        # Extract in reverse sorted order
        result = []
        while not self.heap.is_empty():
            result.append(self.heap.extract_max())
        
        self.assertEqual(result, sorted(values, reverse=True))
    
    def test_heap_property(self):
        """Test that max heap property is maintained."""
        values = [5, 3, 7, 1, 9, 4, 6]
        for val in values:
            self.heap.insert(val)
        
        # Check heap property: parent >= children
        for i in range(len(self.heap.heap)):
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < len(self.heap.heap):
                self.assertGreaterEqual(self.heap.heap[i], self.heap.heap[left])
            
            if right < len(self.heap.heap):
                self.assertGreaterEqual(self.heap.heap[i], self.heap.heap[right])


class TestUtilityFunctions(unittest.TestCase):
    """Test cases for utility functions."""
    
    def test_build_tree_from_list(self):
        """Test building tree from level-order list."""
        values = [1, 2, 3, 4, 5, 6, 7]
        root = build_tree_from_list(values)
        
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)
        self.assertEqual(root.left.left.val, 4)
    
    def test_build_tree_from_list_with_none(self):
        """Test building tree with None values."""
        values = [1, 2, 3, None, 5]
        root = build_tree_from_list(values)
        
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)
        self.assertIsNone(root.left.left)
        self.assertEqual(root.left.right.val, 5)
    
    def test_tree_to_list(self):
        """Test converting tree to list."""
        values = [1, 2, 3, 4, 5, 6, 7]
        root = build_tree_from_list(values)
        
        result = tree_to_list(root)
        self.assertEqual(result, values)
    
    def test_lowest_common_ancestor(self):
        """Test LCA finding."""
        bst = BinarySearchTree()
        values = [20, 10, 30, 5, 15, 25, 35]
        for val in values:
            bst.insert(val)
        
        # LCA of 5 and 15 is 10
        lca = lowest_common_ancestor(bst.root, 5, 15)
        self.assertEqual(lca.val, 10)
        
        # LCA of 5 and 35 is 20 (root)
        lca = lowest_common_ancestor(bst.root, 5, 35)
        self.assertEqual(lca.val, 20)
        
        # LCA of 25 and 35 is 30
        lca = lowest_common_ancestor(bst.root, 25, 35)
        self.assertEqual(lca.val, 30)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases for tree structures."""
    
    def test_single_node_tree(self):
        """Test operations on single node tree."""
        bst = BinarySearchTree()
        bst.insert(50)
        
        self.assertEqual(bst.height(), 0)
        self.assertTrue(bst.is_balanced())
        self.assertEqual(bst.find_min(), 50)
        self.assertEqual(bst.find_max(), 50)
        self.assertEqual(bst.inorder_traversal(), [50])
    
    def test_empty_tree_operations(self):
        """Test operations on empty tree."""
        bst = BinarySearchTree()
        
        self.assertEqual(bst.height(), -1)
        self.assertTrue(bst.is_balanced())
        self.assertIsNone(bst.find_min())
        self.assertIsNone(bst.find_max())
        self.assertEqual(bst.inorder_traversal(), [])
    
    def test_duplicate_values(self):
        """Test inserting duplicate values."""
        bst = BinarySearchTree()
        bst.insert(50)
        bst.insert(50)
        
        # Both should be inserted (BST allows duplicates on right)
        self.assertEqual(bst.size(), 2)
    
    def test_large_tree(self):
        """Test with large number of nodes."""
        bst = BinarySearchTree()
        
        for i in range(100):
            bst.insert(i)
        
        self.assertEqual(bst.size(), 100)
        self.assertEqual(bst.find_min(), 0)
        self.assertEqual(bst.find_max(), 99)
    
    def test_heap_single_element(self):
        """Test heap with single element."""
        heap = MinHeap()
        heap.insert(5)
        
        self.assertEqual(heap.peek(), 5)
        self.assertEqual(heap.extract_min(), 5)
        self.assertTrue(heap.is_empty())


def run_tests():
    """Run all tests."""
    unittest.main(verbosity=2)


if __name__ == '__main__':
    run_tests()
