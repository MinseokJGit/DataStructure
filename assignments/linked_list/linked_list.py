"""
Linked List Data Structure Implementation

This module provides complete implementations of various linked list types:
singly linked list, doubly linked list, and circular linked list.

Author: Data Structure Course
Date: 2024
"""


class Node:
    """
    Node class for singly linked list.
    """
    
    def __init__(self, data):
        """
        Initialize a node.
        
        Args:
            data: The data to store in the node
        """
        self.data = data
        self.next = None


class SinglyLinkedList:
    """
    Singly linked list implementation.
    
    Each node has a reference to the next node only.
    Provides O(1) insertion at head, O(1) insertion at tail (with tail pointer).
    """
    
    def __init__(self):
        """Initialize an empty singly linked list."""
        self.head = None
        self.tail = None
        self._size = 0
    
    def append(self, data):
        """
        Add an element to the end of the list.
        
        Args:
            data: The data to be added
            
        Time Complexity: O(1) with tail pointer
        """
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
    
    def prepend(self, data):
        """
        Add an element to the beginning of the list.
        
        Args:
            data: The data to be added
            
        Time Complexity: O(1)
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
        if not self.tail:
            self.tail = new_node
        
        self._size += 1
    
    def insert_at(self, index, data):
        """
        Insert an element at a specific position.
        
        Args:
            index (int): Position to insert at (0-indexed)
            data: The data to be inserted
            
        Raises:
            IndexError: If index is out of bounds
            
        Time Complexity: O(index)
        """
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            self.prepend(data)
            return
        
        if index == self._size:
            self.append(data)
            return
        
        new_node = Node(data)
        current = self.head
        
        for _ in range(index - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self._size += 1
    
    def delete_first(self):
        """
        Delete the first element.
        
        Returns:
            The data of the deleted node
            
        Raises:
            IndexError: If list is empty
            
        Time Complexity: O(1)
        """
        if not self.head:
            raise IndexError("delete from empty list")
        
        data = self.head.data
        self.head = self.head.next
        self._size -= 1
        
        if not self.head:
            self.tail = None
        
        return data
    
    def delete_last(self):
        """
        Delete the last element.
        
        Returns:
            The data of the deleted node
            
        Raises:
            IndexError: If list is empty
            
        Time Complexity: O(n) - need to find second-to-last node
        """
        if not self.head:
            raise IndexError("delete from empty list")
        
        if not self.head.next:
            data = self.head.data
            self.head = None
            self.tail = None
            self._size -= 1
            return data
        
        current = self.head
        while current.next.next:
            current = current.next
        
        data = current.next.data
        current.next = None
        self.tail = current
        self._size -= 1
        
        return data
    
    def delete_value(self, value):
        """
        Delete the first occurrence of a value.
        
        Args:
            value: The value to delete
            
        Returns:
            bool: True if value was found and deleted, False otherwise
            
        Time Complexity: O(n)
        """
        if not self.head:
            return False
        
        if self.head.data == value:
            self.delete_first()
            return True
        
        current = self.head
        while current.next and current.next.data != value:
            current = current.next
        
        if current.next:
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next
            self._size -= 1
            return True
        
        return False
    
    def find(self, value):
        """
        Find a value in the list.
        
        Args:
            value: The value to find
            
        Returns:
            Node: The node containing the value, or None if not found
            
        Time Complexity: O(n)
        """
        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next
        return None
    
    def get(self, index):
        """
        Get element at a specific index.
        
        Args:
            index (int): Index of the element (0-indexed)
            
        Returns:
            The data at the specified index
            
        Raises:
            IndexError: If index is out of bounds
            
        Time Complexity: O(index)
        """
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        
        current = self.head
        for _ in range(index):
            current = current.next
        
        return current.data
    
    def reverse(self):
        """
        Reverse the linked list in place.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        prev = None
        current = self.head
        self.tail = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    def find_middle(self):
        """
        Find the middle node using slow-fast pointer technique.
        
        Returns:
            The data of the middle node, or None if list is empty
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not self.head:
            return None
        
        slow = fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data
    
    def has_cycle(self):
        """
        Detect if the list has a cycle using Floyd's algorithm.
        
        Returns:
            bool: True if cycle exists, False otherwise
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not self.head:
            return False
        
        slow = fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False
    
    def is_empty(self):
        """
        Check if the list is empty.
        
        Returns:
            bool: True if empty, False otherwise
        """
        return self.head is None
    
    def size(self):
        """
        Get the number of elements in the list.
        
        Returns:
            int: Number of elements
        """
        return self._size
    
    def clear(self):
        """Clear all elements from the list."""
        self.head = None
        self.tail = None
        self._size = 0
    
    def to_list(self):
        """
        Convert linked list to Python list.
        
        Returns:
            list: List of all elements
        """
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def __str__(self):
        """String representation of the list."""
        return f"SinglyLinkedList({self.to_list()})"
    
    def __repr__(self):
        """Developer representation of the list."""
        return self.__str__()
    
    def __len__(self):
        """Return the length of the list."""
        return self._size
    
    def __iter__(self):
        """Make the list iterable."""
        current = self.head
        while current:
            yield current.data
            current = current.next


class DNode:
    """
    Node class for doubly linked list.
    """
    
    def __init__(self, data):
        """
        Initialize a doubly linked node.
        
        Args:
            data: The data to store in the node
        """
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """
    Doubly linked list implementation.
    
    Each node has references to both next and previous nodes.
    Provides O(1) insertion/deletion at both ends.
    """
    
    def __init__(self):
        """Initialize an empty doubly linked list."""
        self.head = None
        self.tail = None
        self._size = 0
    
    def append(self, data):
        """
        Add an element to the end of the list.
        
        Args:
            data: The data to be added
            
        Time Complexity: O(1)
        """
        new_node = DNode(data)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
    
    def prepend(self, data):
        """
        Add an element to the beginning of the list.
        
        Args:
            data: The data to be added
            
        Time Complexity: O(1)
        """
        new_node = DNode(data)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self._size += 1
    
    def insert_at(self, index, data):
        """
        Insert an element at a specific position.
        
        Args:
            index (int): Position to insert at (0-indexed)
            data: The data to be inserted
            
        Raises:
            IndexError: If index is out of bounds
            
        Time Complexity: O(min(index, n-index))
        """
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            self.prepend(data)
            return
        
        if index == self._size:
            self.append(data)
            return
        
        new_node = DNode(data)
        
        # Optimize: traverse from head or tail depending on index
        if index < self._size // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self._size - index - 1):
                current = current.prev
        
        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node
        self._size += 1
    
    def delete_first(self):
        """
        Delete the first element.
        
        Returns:
            The data of the deleted node
            
        Raises:
            IndexError: If list is empty
            
        Time Complexity: O(1)
        """
        if not self.head:
            raise IndexError("delete from empty list")
        
        data = self.head.data
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        
        self._size -= 1
        return data
    
    def delete_last(self):
        """
        Delete the last element.
        
        Returns:
            The data of the deleted node
            
        Raises:
            IndexError: If list is empty
            
        Time Complexity: O(1)
        """
        if not self.tail:
            raise IndexError("delete from empty list")
        
        data = self.tail.data
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        self._size -= 1
        return data
    
    def delete_value(self, value):
        """
        Delete the first occurrence of a value.
        
        Args:
            value: The value to delete
            
        Returns:
            bool: True if value was found and deleted, False otherwise
            
        Time Complexity: O(n)
        """
        current = self.head
        
        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                
                self._size -= 1
                return True
            
            current = current.next
        
        return False
    
    def find(self, value):
        """
        Find a value in the list.
        
        Args:
            value: The value to find
            
        Returns:
            DNode: The node containing the value, or None if not found
            
        Time Complexity: O(n)
        """
        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next
        return None
    
    def get(self, index):
        """
        Get element at a specific index.
        
        Args:
            index (int): Index of the element (0-indexed)
            
        Returns:
            The data at the specified index
            
        Raises:
            IndexError: If index is out of bounds
            
        Time Complexity: O(min(index, n-index))
        """
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        
        # Optimize: traverse from head or tail
        if index < self._size // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self._size - index - 1):
                current = current.prev
        
        return current.data
    
    def reverse(self):
        """
        Reverse the doubly linked list in place.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        current = self.head
        self.head, self.tail = self.tail, self.head
        
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev
    
    def is_empty(self):
        """Check if the list is empty."""
        return self.head is None
    
    def size(self):
        """Get the number of elements in the list."""
        return self._size
    
    def clear(self):
        """Clear all elements from the list."""
        self.head = None
        self.tail = None
        self._size = 0
    
    def to_list(self):
        """Convert linked list to Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def to_list_reverse(self):
        """Convert linked list to Python list in reverse order."""
        result = []
        current = self.tail
        while current:
            result.append(current.data)
            current = current.prev
        return result
    
    def __str__(self):
        """String representation of the list."""
        return f"DoublyLinkedList({self.to_list()})"
    
    def __repr__(self):
        """Developer representation of the list."""
        return self.__str__()
    
    def __len__(self):
        """Return the length of the list."""
        return self._size
    
    def __iter__(self):
        """Make the list iterable."""
        current = self.head
        while current:
            yield current.data
            current = current.next


class CircularLinkedList:
    """
    Circular linked list implementation.
    
    The last node points back to the first node, forming a cycle.
    Useful for round-robin scheduling and circular buffers.
    """
    
    def __init__(self):
        """Initialize an empty circular linked list."""
        self.head = None
        self._size = 0
    
    def append(self, data):
        """
        Add an element to the end of the list.
        
        Args:
            data: The data to be added
            
        Time Complexity: O(n) without tail pointer
        """
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            
            current.next = new_node
            new_node.next = self.head
        
        self._size += 1
    
    def prepend(self, data):
        """
        Add an element to the beginning of the list.
        
        Args:
            data: The data to be added
            
        Time Complexity: O(n) - need to update last node's pointer
        """
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            
            new_node.next = self.head
            current.next = new_node
            self.head = new_node
        
        self._size += 1
    
    def delete_first(self):
        """
        Delete the first element.
        
        Returns:
            The data of the deleted node
            
        Raises:
            IndexError: If list is empty
            
        Time Complexity: O(n) - need to update last node's pointer
        """
        if not self.head:
            raise IndexError("delete from empty list")
        
        data = self.head.data
        
        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            
            current.next = self.head.next
            self.head = self.head.next
        
        self._size -= 1
        return data
    
    def delete_value(self, value):
        """
        Delete the first occurrence of a value.
        
        Args:
            value: The value to delete
            
        Returns:
            bool: True if value was found and deleted, False otherwise
            
        Time Complexity: O(n)
        """
        if not self.head:
            return False
        
        if self.head.data == value:
            self.delete_first()
            return True
        
        current = self.head
        while current.next != self.head:
            if current.next.data == value:
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next
        
        return False
    
    def find(self, value):
        """
        Find a value in the list.
        
        Args:
            value: The value to find
            
        Returns:
            Node: The node containing the value, or None if not found
            
        Time Complexity: O(n)
        """
        if not self.head:
            return None
        
        current = self.head
        while True:
            if current.data == value:
                return current
            current = current.next
            if current == self.head:
                break
        
        return None
    
    def is_empty(self):
        """Check if the list is empty."""
        return self.head is None
    
    def size(self):
        """Get the number of elements in the list."""
        return self._size
    
    def clear(self):
        """Clear all elements from the list."""
        self.head = None
        self._size = 0
    
    def to_list(self):
        """Convert circular linked list to Python list."""
        if not self.head:
            return []
        
        result = []
        current = self.head
        while True:
            result.append(current.data)
            current = current.next
            if current == self.head:
                break
        
        return result
    
    def __str__(self):
        """String representation of the list."""
        return f"CircularLinkedList({self.to_list()})"
    
    def __repr__(self):
        """Developer representation of the list."""
        return self.__str__()
    
    def __len__(self):
        """Return the length of the list."""
        return self._size
    
    def __iter__(self):
        """Make the list iterable (one complete cycle)."""
        if not self.head:
            return
        
        current = self.head
        while True:
            yield current.data
            current = current.next
            if current == self.head:
                break


# Utility functions for linked list operations
def merge_sorted_lists(list1, list2):
    """
    Merge two sorted linked lists into one sorted list.
    
    Args:
        list1 (SinglyLinkedList): First sorted list
        list2 (SinglyLinkedList): Second sorted list
        
    Returns:
        SinglyLinkedList: Merged sorted list
        
    Time Complexity: O(n + m)
    """
    result = SinglyLinkedList()
    
    current1 = list1.head
    current2 = list2.head
    
    while current1 and current2:
        if current1.data <= current2.data:
            result.append(current1.data)
            current1 = current1.next
        else:
            result.append(current2.data)
            current2 = current2.next
    
    while current1:
        result.append(current1.data)
        current1 = current1.next
    
    while current2:
        result.append(current2.data)
        current2 = current2.next
    
    return result


def remove_duplicates(linked_list):
    """
    Remove duplicate values from a linked list.
    
    Args:
        linked_list (SinglyLinkedList): The list to remove duplicates from
        
    Time Complexity: O(n) with hash set
    """
    if not linked_list.head:
        return
    
    seen = set()
    current = linked_list.head
    seen.add(current.data)
    
    while current.next:
        if current.next.data in seen:
            current.next = current.next.next
            linked_list._size -= 1
        else:
            seen.add(current.next.data)
            current = current.next
    
    # Update tail pointer
    current = linked_list.head
    while current.next:
        current = current.next
    linked_list.tail = current


def find_kth_from_end(linked_list, k):
    """
    Find the k-th element from the end of the list.
    
    Args:
        linked_list (SinglyLinkedList): The linked list
        k (int): Position from end (1-indexed)
        
    Returns:
        The data of the k-th node from end, or None if not found
        
    Time Complexity: O(n)
    """
    if not linked_list.head or k <= 0:
        return None
    
    fast = slow = linked_list.head
    
    # Move fast k steps ahead
    for _ in range(k):
        if not fast:
            return None
        fast = fast.next
    
    # Move both until fast reaches end
    while fast:
        slow = slow.next
        fast = fast.next
    
    return slow.data if slow else None


# Default linked list (using SinglyLinkedList)
LinkedList = SinglyLinkedList
