"""
Unit Tests for Linked List Data Structures

This module provides comprehensive unit tests for all linked list implementations
and utility functions.

Author: Data Structure Course
Date: 2024
"""

import unittest
from linked_list import (
    SinglyLinkedList, DoublyLinkedList, CircularLinkedList,
    Node, DNode, merge_sorted_lists, remove_duplicates, find_kth_from_end
)


class TestSinglyLinkedList(unittest.TestCase):
    """Test cases for SinglyLinkedList implementation."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.sll = SinglyLinkedList()
    
    def test_initialization(self):
        """Test list initialization."""
        self.assertTrue(self.sll.is_empty())
        self.assertEqual(self.sll.size(), 0)
        self.assertIsNone(self.sll.head)
        self.assertIsNone(self.sll.tail)
    
    def test_append(self):
        """Test append operation."""
        self.sll.append(10)
        self.assertFalse(self.sll.is_empty())
        self.assertEqual(self.sll.size(), 1)
        self.assertEqual(self.sll.head.data, 10)
        self.assertEqual(self.sll.tail.data, 10)
        
        self.sll.append(20)
        self.assertEqual(self.sll.size(), 2)
        self.assertEqual(self.sll.tail.data, 20)
    
    def test_prepend(self):
        """Test prepend operation."""
        self.sll.prepend(10)
        self.assertEqual(self.sll.head.data, 10)
        
        self.sll.prepend(5)
        self.assertEqual(self.sll.head.data, 5)
        self.assertEqual(self.sll.size(), 2)
    
    def test_insert_at(self):
        """Test insert at specific position."""
        self.sll.append(10)
        self.sll.append(30)
        self.sll.insert_at(1, 20)
        
        self.assertEqual(self.sll.to_list(), [10, 20, 30])
        
        self.sll.insert_at(0, 5)
        self.assertEqual(self.sll.to_list(), [5, 10, 20, 30])
        
        self.sll.insert_at(4, 40)
        self.assertEqual(self.sll.to_list(), [5, 10, 20, 30, 40])
    
    def test_insert_at_invalid(self):
        """Test insert at invalid position."""
        with self.assertRaises(IndexError):
            self.sll.insert_at(5, 10)
        
        with self.assertRaises(IndexError):
            self.sll.insert_at(-1, 10)
    
    def test_delete_first(self):
        """Test delete first element."""
        self.sll.append(10)
        self.sll.append(20)
        self.sll.append(30)
        
        data = self.sll.delete_first()
        self.assertEqual(data, 10)
        self.assertEqual(self.sll.to_list(), [20, 30])
    
    def test_delete_first_empty(self):
        """Test delete first from empty list."""
        with self.assertRaises(IndexError):
            self.sll.delete_first()
    
    def test_delete_last(self):
        """Test delete last element."""
        self.sll.append(10)
        self.sll.append(20)
        self.sll.append(30)
        
        data = self.sll.delete_last()
        self.assertEqual(data, 30)
        self.assertEqual(self.sll.to_list(), [10, 20])
    
    def test_delete_last_single_element(self):
        """Test delete last when only one element."""
        self.sll.append(10)
        data = self.sll.delete_last()
        
        self.assertEqual(data, 10)
        self.assertTrue(self.sll.is_empty())
    
    def test_delete_value(self):
        """Test delete by value."""
        self.sll.append(10)
        self.sll.append(20)
        self.sll.append(30)
        
        result = self.sll.delete_value(20)
        self.assertTrue(result)
        self.assertEqual(self.sll.to_list(), [10, 30])
        
        result = self.sll.delete_value(40)
        self.assertFalse(result)
    
    def test_find(self):
        """Test find operation."""
        self.sll.append(10)
        self.sll.append(20)
        self.sll.append(30)
        
        node = self.sll.find(20)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 20)
        
        node = self.sll.find(40)
        self.assertIsNone(node)
    
    def test_get(self):
        """Test get by index."""
        for i in range(5):
            self.sll.append(i * 10)
        
        self.assertEqual(self.sll.get(0), 0)
        self.assertEqual(self.sll.get(2), 20)
        self.assertEqual(self.sll.get(4), 40)
    
    def test_get_invalid(self):
        """Test get with invalid index."""
        self.sll.append(10)
        
        with self.assertRaises(IndexError):
            self.sll.get(5)
        
        with self.assertRaises(IndexError):
            self.sll.get(-1)
    
    def test_reverse(self):
        """Test list reversal."""
        for i in range(1, 6):
            self.sll.append(i)
        
        self.sll.reverse()
        self.assertEqual(self.sll.to_list(), [5, 4, 3, 2, 1])
    
    def test_find_middle(self):
        """Test find middle element."""
        for i in range(1, 6):
            self.sll.append(i)
        
        middle = self.sll.find_middle()
        self.assertEqual(middle, 3)
        
        self.sll.append(6)
        middle = self.sll.find_middle()
        self.assertEqual(middle, 4)
    
    def test_has_cycle(self):
        """Test cycle detection."""
        for i in range(5):
            self.sll.append(i)
        
        self.assertFalse(self.sll.has_cycle())
    
    def test_clear(self):
        """Test clear operation."""
        for i in range(5):
            self.sll.append(i)
        
        self.sll.clear()
        self.assertTrue(self.sll.is_empty())
        self.assertEqual(self.sll.size(), 0)
    
    def test_iteration(self):
        """Test iteration over list."""
        data = [1, 2, 3, 4, 5]
        for item in data:
            self.sll.append(item)
        
        result = [x for x in self.sll]
        self.assertEqual(result, data)
    
    def test_len(self):
        """Test __len__ method."""
        for i in range(5):
            self.sll.append(i)
        
        self.assertEqual(len(self.sll), 5)


class TestDoublyLinkedList(unittest.TestCase):
    """Test cases for DoublyLinkedList implementation."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.dll = DoublyLinkedList()
    
    def test_initialization(self):
        """Test list initialization."""
        self.assertTrue(self.dll.is_empty())
        self.assertEqual(self.dll.size(), 0)
    
    def test_append(self):
        """Test append operation."""
        self.dll.append(10)
        self.assertEqual(self.dll.head.data, 10)
        self.assertEqual(self.dll.tail.data, 10)
        
        self.dll.append(20)
        self.assertEqual(self.dll.tail.data, 20)
        self.assertEqual(self.dll.tail.prev.data, 10)
    
    def test_prepend(self):
        """Test prepend operation."""
        self.dll.prepend(10)
        self.dll.prepend(5)
        
        self.assertEqual(self.dll.head.data, 5)
        self.assertEqual(self.dll.head.next.data, 10)
    
    def test_insert_at(self):
        """Test insert at specific position."""
        self.dll.append(10)
        self.dll.append(30)
        self.dll.insert_at(1, 20)
        
        self.assertEqual(self.dll.to_list(), [10, 20, 30])
    
    def test_delete_first(self):
        """Test delete first element."""
        self.dll.append(10)
        self.dll.append(20)
        
        data = self.dll.delete_first()
        self.assertEqual(data, 10)
        self.assertEqual(self.dll.head.data, 20)
        self.assertIsNone(self.dll.head.prev)
    
    def test_delete_last(self):
        """Test delete last element."""
        self.dll.append(10)
        self.dll.append(20)
        
        data = self.dll.delete_last()
        self.assertEqual(data, 20)
        self.assertEqual(self.dll.tail.data, 10)
        self.assertIsNone(self.dll.tail.next)
    
    def test_delete_value(self):
        """Test delete by value."""
        self.dll.append(10)
        self.dll.append(20)
        self.dll.append(30)
        
        result = self.dll.delete_value(20)
        self.assertTrue(result)
        self.assertEqual(self.dll.to_list(), [10, 30])
    
    def test_reverse(self):
        """Test list reversal."""
        for i in range(1, 6):
            self.dll.append(i)
        
        self.dll.reverse()
        self.assertEqual(self.dll.to_list(), [5, 4, 3, 2, 1])
        
        # Check backward links
        self.assertEqual(self.dll.to_list_reverse(), [1, 2, 3, 4, 5])
    
    def test_to_list_reverse(self):
        """Test reverse list conversion."""
        for i in range(1, 6):
            self.dll.append(i)
        
        self.assertEqual(self.dll.to_list_reverse(), [5, 4, 3, 2, 1])
    
    def test_bidirectional_links(self):
        """Test that prev and next links are correct."""
        self.dll.append(10)
        self.dll.append(20)
        self.dll.append(30)
        
        # Check forward links
        self.assertEqual(self.dll.head.data, 10)
        self.assertEqual(self.dll.head.next.data, 20)
        self.assertEqual(self.dll.head.next.next.data, 30)
        
        # Check backward links
        self.assertEqual(self.dll.tail.data, 30)
        self.assertEqual(self.dll.tail.prev.data, 20)
        self.assertEqual(self.dll.tail.prev.prev.data, 10)


class TestCircularLinkedList(unittest.TestCase):
    """Test cases for CircularLinkedList implementation."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.cll = CircularLinkedList()
    
    def test_initialization(self):
        """Test list initialization."""
        self.assertTrue(self.cll.is_empty())
        self.assertEqual(self.cll.size(), 0)
    
    def test_append(self):
        """Test append operation."""
        self.cll.append(10)
        self.assertEqual(self.cll.head.data, 10)
        self.assertEqual(self.cll.head.next, self.cll.head)
        
        self.cll.append(20)
        self.assertEqual(self.cll.size(), 2)
    
    def test_prepend(self):
        """Test prepend operation."""
        self.cll.append(20)
        self.cll.prepend(10)
        
        self.assertEqual(self.cll.head.data, 10)
        self.assertEqual(self.cll.to_list(), [10, 20])
    
    def test_circular_property(self):
        """Test that list is circular."""
        self.cll.append(10)
        self.cll.append(20)
        self.cll.append(30)
        
        # Traverse and check we come back to head
        current = self.cll.head
        for _ in range(3):
            current = current.next
        
        self.assertEqual(current, self.cll.head)
    
    def test_delete_first(self):
        """Test delete first element."""
        self.cll.append(10)
        self.cll.append(20)
        self.cll.append(30)
        
        data = self.cll.delete_first()
        self.assertEqual(data, 10)
        self.assertEqual(self.cll.to_list(), [20, 30])
    
    def test_delete_value(self):
        """Test delete by value."""
        self.cll.append(10)
        self.cll.append(20)
        self.cll.append(30)
        
        result = self.cll.delete_value(20)
        self.assertTrue(result)
        self.assertEqual(self.cll.to_list(), [10, 30])
    
    def test_find(self):
        """Test find operation."""
        self.cll.append(10)
        self.cll.append(20)
        self.cll.append(30)
        
        node = self.cll.find(20)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 20)
    
    def test_iteration(self):
        """Test iteration (one complete cycle)."""
        data = [1, 2, 3, 4, 5]
        for item in data:
            self.cll.append(item)
        
        result = [x for x in self.cll]
        self.assertEqual(result, data)


class TestUtilityFunctions(unittest.TestCase):
    """Test cases for utility functions."""
    
    def test_merge_sorted_lists(self):
        """Test merging two sorted lists."""
        list1 = SinglyLinkedList()
        for item in [1, 3, 5]:
            list1.append(item)
        
        list2 = SinglyLinkedList()
        for item in [2, 4, 6]:
            list2.append(item)
        
        merged = merge_sorted_lists(list1, list2)
        self.assertEqual(merged.to_list(), [1, 2, 3, 4, 5, 6])
    
    def test_merge_sorted_lists_empty(self):
        """Test merging with empty list."""
        list1 = SinglyLinkedList()
        for item in [1, 2, 3]:
            list1.append(item)
        
        list2 = SinglyLinkedList()
        
        merged = merge_sorted_lists(list1, list2)
        self.assertEqual(merged.to_list(), [1, 2, 3])
    
    def test_remove_duplicates(self):
        """Test removing duplicates."""
        sll = SinglyLinkedList()
        for item in [1, 2, 3, 2, 4, 1, 5]:
            sll.append(item)
        
        remove_duplicates(sll)
        self.assertEqual(sll.to_list(), [1, 2, 3, 4, 5])
    
    def test_remove_duplicates_no_duplicates(self):
        """Test removing duplicates when none exist."""
        sll = SinglyLinkedList()
        for item in [1, 2, 3, 4, 5]:
            sll.append(item)
        
        original = sll.to_list()
        remove_duplicates(sll)
        self.assertEqual(sll.to_list(), original)
    
    def test_find_kth_from_end(self):
        """Test finding k-th element from end."""
        sll = SinglyLinkedList()
        for i in range(1, 11):
            sll.append(i)
        
        self.assertEqual(find_kth_from_end(sll, 1), 10)
        self.assertEqual(find_kth_from_end(sll, 5), 6)
        self.assertEqual(find_kth_from_end(sll, 10), 1)
    
    def test_find_kth_from_end_invalid(self):
        """Test finding k-th from end with invalid k."""
        sll = SinglyLinkedList()
        for i in range(1, 6):
            sll.append(i)
        
        self.assertIsNone(find_kth_from_end(sll, 0))
        self.assertIsNone(find_kth_from_end(sll, 10))
        self.assertIsNone(find_kth_from_end(sll, -1))


class TestEdgeCases(unittest.TestCase):
    """Test edge cases for linked lists."""
    
    def test_single_element_operations(self):
        """Test operations on single element list."""
        sll = SinglyLinkedList()
        sll.append(10)
        
        self.assertEqual(sll.find_middle(), 10)
        self.assertEqual(sll.get(0), 10)
        
        sll.reverse()
        self.assertEqual(sll.to_list(), [10])
    
    def test_empty_list_operations(self):
        """Test operations on empty list."""
        sll = SinglyLinkedList()
        
        self.assertIsNone(sll.find_middle())
        self.assertFalse(sll.has_cycle())
        self.assertIsNone(sll.find(10))
        self.assertEqual(sll.to_list(), [])
    
    def test_large_list(self):
        """Test with large list."""
        sll = SinglyLinkedList()
        
        for i in range(1000):
            sll.append(i)
        
        self.assertEqual(sll.size(), 1000)
        self.assertEqual(sll.get(500), 500)
        self.assertEqual(sll.find_middle(), 500)
    
    def test_different_data_types(self):
        """Test with different data types."""
        sll = SinglyLinkedList()
        
        sll.append(42)
        sll.append("hello")
        sll.append([1, 2, 3])
        sll.append({'key': 'value'})
        
        self.assertEqual(sll.size(), 4)
        self.assertEqual(sll.get(1), "hello")
        self.assertEqual(sll.get(2), [1, 2, 3])
    
    def test_alternating_operations(self):
        """Test alternating append and delete."""
        sll = SinglyLinkedList()
        
        for i in range(10):
            sll.append(i)
            if i % 2 == 0:
                sll.delete_first()
        
        self.assertEqual(sll.size(), 5)


def run_tests():
    """Run all tests."""
    unittest.main(verbosity=2)


if __name__ == '__main__':
    run_tests()
