"""
Unit Tests for Queue Data Structures

This module provides comprehensive unit tests for all queue implementations
and utility functions.

Author: Data Structure Course
Date: 2024
"""

import unittest
from queue import (
    ArrayQueue, LinkedListQueue, CircularQueue, Deque,
    hot_potato, is_palindrome, generate_binary_numbers
)


class TestArrayQueue(unittest.TestCase):
    """Test cases for ArrayQueue implementation."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.queue = ArrayQueue()
    
    def test_initialization(self):
        """Test queue initialization."""
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 0)
    
    def test_enqueue(self):
        """Test enqueue operation."""
        self.queue.enqueue(10)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 1)
        
        self.queue.enqueue(20)
        self.assertEqual(self.queue.size(), 2)
    
    def test_dequeue(self):
        """Test dequeue operation."""
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.queue.enqueue(30)
        
        self.assertEqual(self.queue.dequeue(), 10)
        self.assertEqual(self.queue.size(), 2)
        
        self.assertEqual(self.queue.dequeue(), 20)
        self.assertEqual(self.queue.dequeue(), 30)
        self.assertTrue(self.queue.is_empty())
    
    def test_front(self):
        """Test front operation."""
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        
        self.assertEqual(self.queue.front(), 10)
        self.assertEqual(self.queue.size(), 2)  # Size unchanged
    
    def test_dequeue_empty(self):
        """Test dequeue from empty queue."""
        with self.assertRaises(IndexError):
            self.queue.dequeue()
    
    def test_front_empty(self):
        """Test front from empty queue."""
        with self.assertRaises(IndexError):
            self.queue.front()
    
    def test_fifo_order(self):
        """Test FIFO (First In, First Out) order."""
        items = [1, 2, 3, 4, 5]
        for item in items:
            self.queue.enqueue(item)
        
        for item in items:
            self.assertEqual(self.queue.dequeue(), item)
    
    def test_multiple_operations(self):
        """Test multiple enqueue and dequeue operations."""
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(), 1)
        
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)
        
        self.queue.enqueue(5)
        self.assertEqual(self.queue.size(), 2)


class TestLinkedListQueue(unittest.TestCase):
    """Test cases for LinkedListQueue implementation."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.queue = LinkedListQueue()
    
    def test_initialization(self):
        """Test queue initialization."""
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 0)
    
    def test_enqueue(self):
        """Test enqueue operation."""
        self.queue.enqueue('A')
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 1)
        
        self.queue.enqueue('B')
        self.assertEqual(self.queue.size(), 2)
    
    def test_dequeue(self):
        """Test dequeue operation."""
        self.queue.enqueue('A')
        self.queue.enqueue('B')
        self.queue.enqueue('C')
        
        self.assertEqual(self.queue.dequeue(), 'A')
        self.assertEqual(self.queue.size(), 2)
        
        self.assertEqual(self.queue.dequeue(), 'B')
        self.assertEqual(self.queue.dequeue(), 'C')
        self.assertTrue(self.queue.is_empty())
    
    def test_front(self):
        """Test front operation."""
        self.queue.enqueue('X')
        self.queue.enqueue('Y')
        
        self.assertEqual(self.queue.front(), 'X')
        self.assertEqual(self.queue.size(), 2)
    
    def test_dequeue_empty(self):
        """Test dequeue from empty queue."""
        with self.assertRaises(IndexError):
            self.queue.dequeue()
    
    def test_front_empty(self):
        """Test front from empty queue."""
        with self.assertRaises(IndexError):
            self.queue.front()
    
    def test_fifo_order(self):
        """Test FIFO order."""
        items = ['first', 'second', 'third', 'fourth']
        for item in items:
            self.queue.enqueue(item)
        
        for item in items:
            self.assertEqual(self.queue.dequeue(), item)
    
    def test_single_element(self):
        """Test queue with single element."""
        self.queue.enqueue(42)
        self.assertEqual(self.queue.front(), 42)
        self.assertEqual(self.queue.dequeue(), 42)
        self.assertTrue(self.queue.is_empty())


class TestCircularQueue(unittest.TestCase):
    """Test cases for CircularQueue implementation."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.queue = CircularQueue(5)
    
    def test_initialization(self):
        """Test queue initialization."""
        self.assertTrue(self.queue.is_empty())
        self.assertFalse(self.queue.is_full())
        self.assertEqual(self.queue.size(), 0)
        self.assertEqual(self.queue.capacity(), 5)
    
    def test_enqueue(self):
        """Test enqueue operation."""
        self.queue.enqueue(10)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 1)
    
    def test_dequeue(self):
        """Test dequeue operation."""
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        
        self.assertEqual(self.queue.dequeue(), 10)
        self.assertEqual(self.queue.size(), 1)
    
    def test_circular_behavior(self):
        """Test circular wrap-around behavior."""
        # Fill the queue
        for i in range(5):
            self.queue.enqueue(i)
        
        self.assertTrue(self.queue.is_full())
        
        # Remove some elements
        self.queue.dequeue()
        self.queue.dequeue()
        
        # Add new elements (should wrap around)
        self.queue.enqueue(5)
        self.queue.enqueue(6)
        
        # Check order
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertEqual(self.queue.dequeue(), 4)
        self.assertEqual(self.queue.dequeue(), 5)
        self.assertEqual(self.queue.dequeue(), 6)
    
    def test_full_queue(self):
        """Test full queue condition."""
        for i in range(5):
            self.queue.enqueue(i)
        
        self.assertTrue(self.queue.is_full())
        
        with self.assertRaises(OverflowError):
            self.queue.enqueue(5)
    
    def test_empty_queue(self):
        """Test empty queue condition."""
        with self.assertRaises(IndexError):
            self.queue.dequeue()
        
        with self.assertRaises(IndexError):
            self.queue.front()
    
    def test_front(self):
        """Test front operation."""
        self.queue.enqueue(100)
        self.queue.enqueue(200)
        
        self.assertEqual(self.queue.front(), 100)
        self.assertEqual(self.queue.size(), 2)


class TestDeque(unittest.TestCase):
    """Test cases for Deque implementation."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.deque = Deque()
    
    def test_initialization(self):
        """Test deque initialization."""
        self.assertTrue(self.deque.is_empty())
        self.assertEqual(self.deque.size(), 0)
    
    def test_add_front(self):
        """Test add_front operation."""
        self.deque.add_front(1)
        self.assertEqual(self.deque.front(), 1)
        
        self.deque.add_front(2)
        self.assertEqual(self.deque.front(), 2)
    
    def test_add_rear(self):
        """Test add_rear operation."""
        self.deque.add_rear(1)
        self.assertEqual(self.deque.rear(), 1)
        
        self.deque.add_rear(2)
        self.assertEqual(self.deque.rear(), 2)
    
    def test_remove_front(self):
        """Test remove_front operation."""
        self.deque.add_rear(1)
        self.deque.add_rear(2)
        self.deque.add_rear(3)
        
        self.assertEqual(self.deque.remove_front(), 1)
        self.assertEqual(self.deque.size(), 2)
    
    def test_remove_rear(self):
        """Test remove_rear operation."""
        self.deque.add_rear(1)
        self.deque.add_rear(2)
        self.deque.add_rear(3)
        
        self.assertEqual(self.deque.remove_rear(), 3)
        self.assertEqual(self.deque.size(), 2)
    
    def test_front_and_rear(self):
        """Test front and rear access."""
        self.deque.add_rear(1)
        self.deque.add_rear(2)
        self.deque.add_front(0)
        
        self.assertEqual(self.deque.front(), 0)
        self.assertEqual(self.deque.rear(), 2)
    
    def test_empty_operations(self):
        """Test operations on empty deque."""
        with self.assertRaises(IndexError):
            self.deque.remove_front()
        
        with self.assertRaises(IndexError):
            self.deque.remove_rear()
        
        with self.assertRaises(IndexError):
            self.deque.front()
        
        with self.assertRaises(IndexError):
            self.deque.rear()
    
    def test_mixed_operations(self):
        """Test mixed front and rear operations."""
        self.deque.add_front(2)
        self.deque.add_front(1)
        self.deque.add_rear(3)
        self.deque.add_rear(4)
        
        # Deque should be: [1, 2, 3, 4]
        self.assertEqual(self.deque.remove_front(), 1)
        self.assertEqual(self.deque.remove_rear(), 4)
        self.assertEqual(self.deque.remove_front(), 2)
        self.assertEqual(self.deque.remove_rear(), 3)
        self.assertTrue(self.deque.is_empty())


class TestUtilityFunctions(unittest.TestCase):
    """Test cases for utility functions."""
    
    def test_hot_potato_basic(self):
        """Test hot potato game."""
        names = ['Alice', 'Bob', 'Charlie']
        winner = hot_potato(names, 1)
        self.assertIn(winner, names)
    
    def test_hot_potato_single_player(self):
        """Test hot potato with single player."""
        names = ['Alice']
        winner = hot_potato(names, 5)
        self.assertEqual(winner, 'Alice')
    
    def test_is_palindrome_true(self):
        """Test palindrome detection - positive cases."""
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))
    
    def test_is_palindrome_false(self):
        """Test palindrome detection - negative cases."""
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("hello world"))
    
    def test_generate_binary_numbers(self):
        """Test binary number generation."""
        result = generate_binary_numbers(5)
        expected = ['1', '10', '11', '100', '101']
        self.assertEqual(result, expected)
    
    def test_generate_binary_numbers_zero(self):
        """Test binary number generation with zero."""
        result = generate_binary_numbers(0)
        self.assertEqual(result, [])
    
    def test_generate_binary_numbers_one(self):
        """Test binary number generation with one."""
        result = generate_binary_numbers(1)
        self.assertEqual(result, ['1'])
    
    def test_generate_binary_numbers_large(self):
        """Test binary number generation with larger number."""
        result = generate_binary_numbers(10)
        expected = ['1', '10', '11', '100', '101', '110', '111', '1000', '1001', '1010']
        self.assertEqual(result, expected)


class TestQueueEdgeCases(unittest.TestCase):
    """Test edge cases for queue implementations."""
    
    def test_large_number_of_operations(self):
        """Test queue with large number of operations."""
        queue = LinkedListQueue()
        
        # Enqueue 1000 items
        for i in range(1000):
            queue.enqueue(i)
        
        self.assertEqual(queue.size(), 1000)
        
        # Dequeue 1000 items
        for i in range(1000):
            self.assertEqual(queue.dequeue(), i)
        
        self.assertTrue(queue.is_empty())
    
    def test_alternating_operations(self):
        """Test alternating enqueue and dequeue."""
        queue = LinkedListQueue()
        
        for i in range(100):
            queue.enqueue(i)
            if i % 2 == 0:
                queue.dequeue()
        
        self.assertEqual(queue.size(), 50)
    
    def test_different_data_types(self):
        """Test queue with different data types."""
        queue = LinkedListQueue()
        
        queue.enqueue(42)
        queue.enqueue("hello")
        queue.enqueue([1, 2, 3])
        queue.enqueue({'key': 'value'})
        
        self.assertEqual(queue.dequeue(), 42)
        self.assertEqual(queue.dequeue(), "hello")
        self.assertEqual(queue.dequeue(), [1, 2, 3])
        self.assertEqual(queue.dequeue(), {'key': 'value'})
    
    def test_circular_queue_edge_cases(self):
        """Test circular queue edge cases."""
        queue = CircularQueue(3)
        
        # Fill and empty multiple times
        for _ in range(3):
            queue.enqueue(1)
            queue.enqueue(2)
            queue.enqueue(3)
            
            queue.dequeue()
            queue.dequeue()
            queue.dequeue()
        
        self.assertTrue(queue.is_empty())


def run_tests():
    """Run all tests."""
    unittest.main(verbosity=2)


if __name__ == '__main__':
    run_tests()
