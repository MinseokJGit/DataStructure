"""
Tree Data Structure Implementation

This module provides complete implementations of various tree structures:
Binary Search Tree (BST), AVL Tree, and Min/Max Heap.

Author: Data Structure Course
Date: 2024
"""

from collections import deque


class TreeNode:
    """
    Node class for binary tree.
    """
    
    def __init__(self, val):
        """
        Initialize a tree node.
        
        Args:
            val: The value to store in the node
        """
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    Binary Search Tree implementation.
    
    Maintains BST property: left < root < right
    Provides O(log n) average case for search, insert, delete.
    """
    
    def __init__(self):
        """Initialize an empty BST."""
        self.root = None
        self._size = 0
    
    def insert(self, val):
        """
        Insert a value into the BST.
        
        Args:
            val: The value to insert
            
        Time Complexity: O(h) where h is height
        """
        self.root = self._insert_recursive(self.root, val)
        self._size += 1
    
    def _insert_recursive(self, node, val):
        """Helper method for recursive insertion."""
        if not node:
            return TreeNode(val)
        
        if val < node.val:
            node.left = self._insert_recursive(node.left, val)
        else:
            node.right = self._insert_recursive(node.right, val)
        
        return node
    
    def search(self, val):
        """
        Search for a value in the BST.
        
        Args:
            val: The value to search for
            
        Returns:
            TreeNode: The node containing the value, or None if not found
            
        Time Complexity: O(h)
        """
        return self._search_recursive(self.root, val)
    
    def _search_recursive(self, node, val):
        """Helper method for recursive search."""
        if not node or node.val == val:
            return node
        
        if val < node.val:
            return self._search_recursive(node.left, val)
        else:
            return self._search_recursive(node.right, val)
    
    def delete(self, val):
        """
        Delete a value from the BST.
        
        Args:
            val: The value to delete
            
        Returns:
            bool: True if value was found and deleted, False otherwise
            
        Time Complexity: O(h)
        """
        if not self.search(val):
            return False
        
        self.root = self._delete_recursive(self.root, val)
        self._size -= 1
        return True
    
    def _delete_recursive(self, node, val):
        """Helper method for recursive deletion."""
        if not node:
            return None
        
        if val < node.val:
            node.left = self._delete_recursive(node.left, val)
        elif val > node.val:
            node.right = self._delete_recursive(node.right, val)
        else:
            # Node to delete found
            
            # Case 1: No children (leaf)
            if not node.left and not node.right:
                return None
            
            # Case 2: One child
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            
            # Case 3: Two children
            # Find inorder successor (smallest in right subtree)
            successor = self._find_min_node(node.right)
            node.val = successor.val
            node.right = self._delete_recursive(node.right, successor.val)
        
        return node
    
    def find_min(self):
        """
        Find the minimum value in the BST.
        
        Returns:
            The minimum value, or None if tree is empty
            
        Time Complexity: O(h)
        """
        if not self.root:
            return None
        return self._find_min_node(self.root).val
    
    def _find_min_node(self, node):
        """Helper method to find minimum node."""
        while node.left:
            node = node.left
        return node
    
    def find_max(self):
        """
        Find the maximum value in the BST.
        
        Returns:
            The maximum value, or None if tree is empty
            
        Time Complexity: O(h)
        """
        if not self.root:
            return None
        return self._find_max_node(self.root).val
    
    def _find_max_node(self, node):
        """Helper method to find maximum node."""
        while node.right:
            node = node.right
        return node
    
    def inorder_traversal(self):
        """
        Perform inorder traversal (Left-Root-Right).
        Returns sorted order for BST.
        
        Returns:
            list: Values in inorder
            
        Time Complexity: O(n)
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """Helper method for inorder traversal."""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.val)
            self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self):
        """
        Perform preorder traversal (Root-Left-Right).
        
        Returns:
            list: Values in preorder
            
        Time Complexity: O(n)
        """
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        """Helper method for preorder traversal."""
        if node:
            result.append(node.val)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder_traversal(self):
        """
        Perform postorder traversal (Left-Right-Root).
        
        Returns:
            list: Values in postorder
            
        Time Complexity: O(n)
        """
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        """Helper method for postorder traversal."""
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.val)
    
    def level_order_traversal(self):
        """
        Perform level-order traversal (BFS).
        
        Returns:
            list: Values in level order
            
        Time Complexity: O(n)
        """
        if not self.root:
            return []
        
        result = []
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
    
    def height(self):
        """
        Calculate the height of the tree.
        
        Returns:
            int: Height of the tree (-1 for empty tree)
            
        Time Complexity: O(n)
        """
        return self._height_recursive(self.root)
    
    def _height_recursive(self, node):
        """Helper method for height calculation."""
        if not node:
            return -1
        return 1 + max(self._height_recursive(node.left),
                      self._height_recursive(node.right))
    
    def is_balanced(self):
        """
        Check if the tree is balanced.
        A tree is balanced if height difference between left and right
        subtrees is at most 1 for all nodes.
        
        Returns:
            bool: True if balanced, False otherwise
            
        Time Complexity: O(n)
        """
        return self._is_balanced_recursive(self.root)[0]
    
    def _is_balanced_recursive(self, node):
        """Helper method for balance check. Returns (is_balanced, height)."""
        if not node:
            return True, -1
        
        left_balanced, left_height = self._is_balanced_recursive(node.left)
        right_balanced, right_height = self._is_balanced_recursive(node.right)
        
        balanced = (left_balanced and right_balanced and
                   abs(left_height - right_height) <= 1)
        height = 1 + max(left_height, right_height)
        
        return balanced, height
    
    def is_valid_bst(self):
        """
        Validate if the tree is a valid BST.
        
        Returns:
            bool: True if valid BST, False otherwise
        """
        return self._is_valid_bst_recursive(self.root, float('-inf'), float('inf'))
    
    def _is_valid_bst_recursive(self, node, min_val, max_val):
        """Helper method for BST validation."""
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (self._is_valid_bst_recursive(node.left, min_val, node.val) and
                self._is_valid_bst_recursive(node.right, node.val, max_val))
    
    def size(self):
        """Get the number of nodes in the tree."""
        return self._size
    
    def is_empty(self):
        """Check if the tree is empty."""
        return self.root is None
    
    def clear(self):
        """Clear all nodes from the tree."""
        self.root = None
        self._size = 0
    
    def __str__(self):
        """String representation of the tree."""
        return f"BST({self.inorder_traversal()})"
    
    def __repr__(self):
        """Developer representation of the tree."""
        return self.__str__()


class AVLNode:
    """
    Node class for AVL tree with height information.
    """
    
    def __init__(self, val):
        """Initialize an AVL node."""
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    """
    AVL Tree implementation (self-balancing BST).
    
    Maintains balance factor of -1, 0, or 1 for all nodes.
    Guarantees O(log n) for all operations.
    """
    
    def __init__(self):
        """Initialize an empty AVL tree."""
        self.root = None
        self._size = 0
    
    def _get_height(self, node):
        """Get height of a node."""
        return node.height if node else 0
    
    def _get_balance(self, node):
        """Get balance factor of a node."""
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    def _update_height(self, node):
        """Update height of a node."""
        if node:
            node.height = 1 + max(self._get_height(node.left),
                                 self._get_height(node.right))
    
    def _rotate_right(self, y):
        """
        Perform right rotation.
        
            y                x
           / \              / \
          x   C    -->     A   y
         / \                  / \
        A   B                B   C
        """
        x = y.left
        B = x.right
        
        x.right = y
        y.left = B
        
        self._update_height(y)
        self._update_height(x)
        
        return x
    
    def _rotate_left(self, x):
        """
        Perform left rotation.
        
          x                  y
         / \                / \
        A   y      -->     x   C
           / \            / \
          B   C          A   B
        """
        y = x.right
        B = y.left
        
        y.left = x
        x.right = B
        
        self._update_height(x)
        self._update_height(y)
        
        return y
    
    def insert(self, val):
        """
        Insert a value into the AVL tree with rebalancing.
        
        Args:
            val: The value to insert
            
        Time Complexity: O(log n)
        """
        self.root = self._insert_recursive(self.root, val)
        self._size += 1
    
    def _insert_recursive(self, node, val):
        """Helper method for AVL insertion with rebalancing."""
        # Standard BST insert
        if not node:
            return AVLNode(val)
        
        if val < node.val:
            node.left = self._insert_recursive(node.left, val)
        else:
            node.right = self._insert_recursive(node.right, val)
        
        # Update height
        self._update_height(node)
        
        # Get balance factor
        balance = self._get_balance(node)
        
        # Left-Left case
        if balance > 1 and val < node.left.val:
            return self._rotate_right(node)
        
        # Right-Right case
        if balance < -1 and val > node.right.val:
            return self._rotate_left(node)
        
        # Left-Right case
        if balance > 1 and val > node.left.val:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        # Right-Left case
        if balance < -1 and val < node.right.val:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    
    def inorder_traversal(self):
        """Perform inorder traversal."""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """Helper method for inorder traversal."""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.val)
            self._inorder_recursive(node.right, result)
    
    def size(self):
        """Get the number of nodes in the tree."""
        return self._size
    
    def __str__(self):
        """String representation of the tree."""
        return f"AVLTree({self.inorder_traversal()})"


class MinHeap:
    """
    Min Heap implementation using array.
    
    Parent is smaller than children.
    Provides O(log n) insert and extract_min.
    """
    
    def __init__(self):
        """Initialize an empty min heap."""
        self.heap = []
    
    def _parent(self, i):
        """Get parent index."""
        return (i - 1) // 2
    
    def _left_child(self, i):
        """Get left child index."""
        return 2 * i + 1
    
    def _right_child(self, i):
        """Get right child index."""
        return 2 * i + 2
    
    def _heapify_up(self, i):
        """
        Bubble up element at index i.
        
        Time Complexity: O(log n)
        """
        while i > 0:
            parent_idx = self._parent(i)
            if self.heap[i] < self.heap[parent_idx]:
                self.heap[i], self.heap[parent_idx] = \
                    self.heap[parent_idx], self.heap[i]
                i = parent_idx
            else:
                break
    
    def _heapify_down(self, i):
        """
        Bubble down element at index i.
        
        Time Complexity: O(log n)
        """
        n = len(self.heap)
        
        while True:
            smallest = i
            left = self._left_child(i)
            right = self._right_child(i)
            
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            
            if smallest != i:
                self.heap[i], self.heap[smallest] = \
                    self.heap[smallest], self.heap[i]
                i = smallest
            else:
                break
    
    def insert(self, val):
        """
        Insert a value into the heap.
        
        Args:
            val: The value to insert
            
        Time Complexity: O(log n)
        """
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)
    
    def extract_min(self):
        """
        Remove and return the minimum value.
        
        Returns:
            The minimum value
            
        Raises:
            IndexError: If heap is empty
            
        Time Complexity: O(log n)
        """
        if not self.heap:
            raise IndexError("extract_min from empty heap")
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        
        return min_val
    
    def peek(self):
        """
        Get the minimum value without removing it.
        
        Returns:
            The minimum value, or None if heap is empty
            
        Time Complexity: O(1)
        """
        return self.heap[0] if self.heap else None
    
    def build_heap(self, arr):
        """
        Build heap from an array.
        
        Args:
            arr (list): Array to build heap from
            
        Time Complexity: O(n)
        """
        self.heap = arr[:]
        # Start from last non-leaf node
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)
    
    def size(self):
        """Get the number of elements in the heap."""
        return len(self.heap)
    
    def is_empty(self):
        """Check if the heap is empty."""
        return len(self.heap) == 0
    
    def __str__(self):
        """String representation of the heap."""
        return f"MinHeap({self.heap})"
    
    def __repr__(self):
        """Developer representation of the heap."""
        return self.__str__()


class MaxHeap:
    """
    Max Heap implementation using array.
    
    Parent is larger than children.
    Provides O(log n) insert and extract_max.
    """
    
    def __init__(self):
        """Initialize an empty max heap."""
        self.heap = []
    
    def _parent(self, i):
        """Get parent index."""
        return (i - 1) // 2
    
    def _left_child(self, i):
        """Get left child index."""
        return 2 * i + 1
    
    def _right_child(self, i):
        """Get right child index."""
        return 2 * i + 2
    
    def _heapify_up(self, i):
        """Bubble up element at index i."""
        while i > 0:
            parent_idx = self._parent(i)
            if self.heap[i] > self.heap[parent_idx]:
                self.heap[i], self.heap[parent_idx] = \
                    self.heap[parent_idx], self.heap[i]
                i = parent_idx
            else:
                break
    
    def _heapify_down(self, i):
        """Bubble down element at index i."""
        n = len(self.heap)
        
        while True:
            largest = i
            left = self._left_child(i)
            right = self._right_child(i)
            
            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right
            
            if largest != i:
                self.heap[i], self.heap[largest] = \
                    self.heap[largest], self.heap[i]
                i = largest
            else:
                break
    
    def insert(self, val):
        """Insert a value into the heap."""
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)
    
    def extract_max(self):
        """Remove and return the maximum value."""
        if not self.heap:
            raise IndexError("extract_max from empty heap")
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        
        return max_val
    
    def peek(self):
        """Get the maximum value without removing it."""
        return self.heap[0] if self.heap else None
    
    def build_heap(self, arr):
        """Build heap from an array."""
        self.heap = arr[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)
    
    def size(self):
        """Get the number of elements in the heap."""
        return len(self.heap)
    
    def is_empty(self):
        """Check if the heap is empty."""
        return len(self.heap) == 0
    
    def __str__(self):
        """String representation of the heap."""
        return f"MaxHeap({self.heap})"
    
    def __repr__(self):
        """Developer representation of the heap."""
        return self.__str__()


# Utility functions
def build_tree_from_list(values):
    """
    Build a binary tree from level-order list.
    None values represent missing nodes.
    
    Args:
        values (list): Level-order values
        
    Returns:
        TreeNode: Root of the constructed tree
    """
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


def tree_to_list(root):
    """
    Convert tree to level-order list representation.
    
    Args:
        root (TreeNode): Root of the tree
        
    Returns:
        list: Level-order values
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    
    return result


def lowest_common_ancestor(root, p, q):
    """
    Find the lowest common ancestor of two nodes in a BST.
    
    Args:
        root (TreeNode): Root of the BST
        p: First value
        q: Second value
        
    Returns:
        TreeNode: LCA node, or None if not found
    """
    if not root:
        return None
    
    # If both p and q are smaller, LCA is in left subtree
    if p < root.val and q < root.val:
        return lowest_common_ancestor(root.left, p, q)
    
    # If both p and q are larger, LCA is in right subtree
    if p > root.val and q > root.val:
        return lowest_common_ancestor(root.right, p, q)
    
    # Otherwise, root is the LCA
    return root
