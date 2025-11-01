"""
Queue Data Structure Implementation

This module provides a complete implementation of queue data structures
using array-based, linked list-based, and circular queue approaches.

Author: Data Structure Course
Date: 2024
"""


class ArrayQueue:
    """
    Array-based queue implementation using Python list.
    
    Provides O(1) enqueue and O(n) dequeue operations due to list.pop(0).
    For better performance, consider using CircularQueue.
    """
    
    def __init__(self):
        """Initialize an empty queue."""
        self._data = []
    
    def enqueue(self, item):
        """
        Add an item to the rear of the queue.
        
        Args:
            item: The item to be added to the queue
            
        Time Complexity: O(1)
        """
        self._data.append(item)
    
    def dequeue(self):
        """
        Remove and return the front item from the queue.
        
        Returns:
            The front item from the queue
            
        Raises:
            IndexError: If the queue is empty
            
        Time Complexity: O(n) - due to list shifting
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.pop(0)
    
    def front(self):
        """
        Return the front item without removing it.
        
        Returns:
            The front item from the queue
            
        Raises:
            IndexError: If the queue is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self._data[0]
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            bool: True if queue is empty, False otherwise
            
        Time Complexity: O(1)
        """
        return len(self._data) == 0
    
    def size(self):
        """
        Get the number of items in the queue.
        
        Returns:
            int: Number of items in the queue
            
        Time Complexity: O(1)
        """
        return len(self._data)
    
    def __str__(self):
        """String representation of the queue."""
        return f"ArrayQueue(front -> {self._data} <- rear)"
    
    def __repr__(self):
        """Developer representation of the queue."""
        return f"ArrayQueue({self._data})"


class Node:
    """
    Node class for linked list implementation.
    """
    
    def __init__(self, data, next_node=None):
        """
        Initialize a node.
        
        Args:
            data: The data to store in the node
            next_node: Reference to the next node (default: None)
        """
        self.data = data
        self.next = next_node


class LinkedListQueue:
    """
    Linked list-based queue implementation.
    
    Provides O(1) time complexity for both enqueue and dequeue operations.
    """
    
    def __init__(self):
        """Initialize an empty queue."""
        self._front = None
        self._rear = None
        self._size = 0
    
    def enqueue(self, item):
        """
        Add an item to the rear of the queue.
        
        Args:
            item: The item to be added to the queue
            
        Time Complexity: O(1)
        """
        new_node = Node(item)
        
        if self.is_empty():
            self._front = new_node
            self._rear = new_node
        else:
            self._rear.next = new_node
            self._rear = new_node
        
        self._size += 1
    
    def dequeue(self):
        """
        Remove and return the front item from the queue.
        
        Returns:
            The front item from the queue
            
        Raises:
            IndexError: If the queue is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        
        data = self._front.data
        self._front = self._front.next
        self._size -= 1
        
        # If queue becomes empty, update rear pointer
        if self._front is None:
            self._rear = None
        
        return data
    
    def front(self):
        """
        Return the front item without removing it.
        
        Returns:
            The front item from the queue
            
        Raises:
            IndexError: If the queue is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self._front.data
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            bool: True if queue is empty, False otherwise
            
        Time Complexity: O(1)
        """
        return self._front is None
    
    def size(self):
        """
        Get the number of items in the queue.
        
        Returns:
            int: Number of items in the queue
            
        Time Complexity: O(1)
        """
        return self._size
    
    def __str__(self):
        """String representation of the queue."""
        items = []
        current = self._front
        while current:
            items.append(current.data)
            current = current.next
        return f"LinkedListQueue(front -> {items} <- rear)"
    
    def __repr__(self):
        """Developer representation of the queue."""
        return self.__str__()


class CircularQueue:
    """
    Circular queue implementation using a fixed-size array.
    
    Provides O(1) time complexity for all operations with efficient space usage.
    Uses modulo arithmetic to wrap around the array.
    """
    
    def __init__(self, capacity=10):
        """
        Initialize a circular queue with fixed capacity.
        
        Args:
            capacity (int): Maximum number of items the queue can hold
        """
        self._capacity = capacity
        self._data = [None] * capacity
        self._front = 0
        self._rear = 0
        self._size = 0
    
    def enqueue(self, item):
        """
        Add an item to the rear of the queue.
        
        Args:
            item: The item to be added to the queue
            
        Raises:
            OverflowError: If the queue is full
            
        Time Complexity: O(1)
        """
        if self.is_full():
            raise OverflowError("enqueue to full queue")
        
        self._data[self._rear] = item
        self._rear = (self._rear + 1) % self._capacity
        self._size += 1
    
    def dequeue(self):
        """
        Remove and return the front item from the queue.
        
        Returns:
            The front item from the queue
            
        Raises:
            IndexError: If the queue is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        
        data = self._data[self._front]
        self._data[self._front] = None  # Help garbage collection
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        
        return data
    
    def front(self):
        """
        Return the front item without removing it.
        
        Returns:
            The front item from the queue
            
        Raises:
            IndexError: If the queue is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self._data[self._front]
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            bool: True if queue is empty, False otherwise
            
        Time Complexity: O(1)
        """
        return self._size == 0
    
    def is_full(self):
        """
        Check if the queue is full.
        
        Returns:
            bool: True if queue is full, False otherwise
            
        Time Complexity: O(1)
        """
        return self._size == self._capacity
    
    def size(self):
        """
        Get the number of items in the queue.
        
        Returns:
            int: Number of items in the queue
            
        Time Complexity: O(1)
        """
        return self._size
    
    def capacity(self):
        """
        Get the maximum capacity of the queue.
        
        Returns:
            int: Maximum capacity of the queue
        """
        return self._capacity
    
    def __str__(self):
        """String representation of the queue."""
        if self.is_empty():
            return f"CircularQueue([], capacity={self._capacity})"
        
        items = []
        index = self._front
        for _ in range(self._size):
            items.append(self._data[index])
            index = (index + 1) % self._capacity
        
        return f"CircularQueue(front -> {items} <- rear, capacity={self._capacity})"
    
    def __repr__(self):
        """Developer representation of the queue."""
        return self.__str__()


class Deque:
    """
    Double-ended queue (deque) implementation.
    
    Allows insertion and deletion at both ends in O(1) time.
    """
    
    def __init__(self):
        """Initialize an empty deque."""
        self._data = []
    
    def add_front(self, item):
        """
        Add an item to the front of the deque.
        
        Args:
            item: The item to be added
            
        Time Complexity: O(n) - due to list insertion at index 0
        """
        self._data.insert(0, item)
    
    def add_rear(self, item):
        """
        Add an item to the rear of the deque.
        
        Args:
            item: The item to be added
            
        Time Complexity: O(1)
        """
        self._data.append(item)
    
    def remove_front(self):
        """
        Remove and return the front item.
        
        Returns:
            The front item from the deque
            
        Raises:
            IndexError: If the deque is empty
            
        Time Complexity: O(n) - due to list shifting
        """
        if self.is_empty():
            raise IndexError("remove_front from empty deque")
        return self._data.pop(0)
    
    def remove_rear(self):
        """
        Remove and return the rear item.
        
        Returns:
            The rear item from the deque
            
        Raises:
            IndexError: If the deque is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("remove_rear from empty deque")
        return self._data.pop()
    
    def front(self):
        """
        Return the front item without removing it.
        
        Returns:
            The front item from the deque
            
        Raises:
            IndexError: If the deque is empty
        """
        if self.is_empty():
            raise IndexError("front from empty deque")
        return self._data[0]
    
    def rear(self):
        """
        Return the rear item without removing it.
        
        Returns:
            The rear item from the deque
            
        Raises:
            IndexError: If the deque is empty
        """
        if self.is_empty():
            raise IndexError("rear from empty deque")
        return self._data[-1]
    
    def is_empty(self):
        """
        Check if the deque is empty.
        
        Returns:
            bool: True if deque is empty, False otherwise
        """
        return len(self._data) == 0
    
    def size(self):
        """
        Get the number of items in the deque.
        
        Returns:
            int: Number of items in the deque
        """
        return len(self._data)
    
    def __str__(self):
        """String representation of the deque."""
        return f"Deque({self._data})"
    
    def __repr__(self):
        """Developer representation of the deque."""
        return f"Deque({self._data})"


# Utility functions for queue operations
def hot_potato(names, num):
    """
    Simulate the Hot Potato game using a queue.
    
    Args:
        names (list): List of player names
        num (int): Number of passes before elimination
        
    Returns:
        str: Name of the winner
        
    Example:
        >>> hot_potato(['Alice', 'Bob', 'Charlie', 'David'], 7)
        'Charlie'
    """
    queue = LinkedListQueue()
    
    # Add all players to the queue
    for name in names:
        queue.enqueue(name)
    
    # Continue until only one player remains
    while queue.size() > 1:
        # Pass the potato num times
        for _ in range(num):
            queue.enqueue(queue.dequeue())
        
        # Eliminate the player holding the potato
        eliminated = queue.dequeue()
        print(f"{eliminated} is eliminated")
    
    # Return the winner
    return queue.dequeue()


def is_palindrome(text):
    """
    Check if a string is a palindrome using a deque.
    
    Args:
        text (str): The text to check
        
    Returns:
        bool: True if palindrome, False otherwise
        
    Example:
        >>> is_palindrome("radar")
        True
        >>> is_palindrome("hello")
        False
    """
    # Remove spaces and convert to lowercase
    text = text.replace(" ", "").lower()
    
    deque = Deque()
    
    # Add all characters to the deque
    for char in text:
        deque.add_rear(char)
    
    # Compare characters from both ends
    while deque.size() > 1:
        if deque.remove_front() != deque.remove_rear():
            return False
    
    return True


def generate_binary_numbers(n):
    """
    Generate binary numbers from 1 to n using a queue.
    
    Args:
        n (int): Upper limit for binary number generation
        
    Returns:
        list: List of binary number strings
        
    Example:
        >>> generate_binary_numbers(5)
        ['1', '10', '11', '100', '101']
    """
    if n <= 0:
        return []
    
    result = []
    queue = LinkedListQueue()
    
    # Start with "1"
    queue.enqueue("1")
    
    for _ in range(n):
        # Get the front binary number
        binary = queue.dequeue()
        result.append(binary)
        
        # Generate next binary numbers by appending 0 and 1
        queue.enqueue(binary + "0")
        queue.enqueue(binary + "1")
    
    return result


# Default queue implementation (using LinkedListQueue for best performance)
Queue = LinkedListQueue
