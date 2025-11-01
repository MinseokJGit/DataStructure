"""
Tree Applications Demo

This module demonstrates practical applications of tree data structures
including BST operations, heap-based priority queue, expression trees,
and various tree algorithms.

Author: Data Structure Course
Date: 2024
"""

from tree import (
    BinarySearchTree, AVLTree, MinHeap, MaxHeap, TreeNode,
    build_tree_from_list, tree_to_list, lowest_common_ancestor
)
import time
import random


class PriorityQueue:
    """
    Priority queue implementation using min heap.
    Lower priority number = higher priority.
    """
    
    def __init__(self):
        """Initialize empty priority queue."""
        self.heap = MinHeap()
        self.counter = 0
    
    def enqueue(self, item, priority):
        """
        Add item with priority.
        
        Args:
            item: Item to add
            priority (int): Priority value (lower = higher priority)
        """
        # Use counter to break ties (FIFO for same priority)
        self.heap.insert((priority, self.counter, item))
        self.counter += 1
        print(f"Enqueued: {item} (priority={priority})")
    
    def dequeue(self):
        """
        Remove and return highest priority item.
        
        Returns:
            Item with highest priority
        """
        if self.heap.is_empty():
            return None
        
        priority, _, item = self.heap.extract_min()
        print(f"Dequeued: {item} (priority={priority})")
        return item
    
    def is_empty(self):
        """Check if queue is empty."""
        return self.heap.is_empty()


class ExpressionTree:
    """
    Expression tree for arithmetic expressions.
    """
    
    def __init__(self, expression=None):
        """
        Initialize expression tree.
        
        Args:
            expression (str): Postfix expression (optional)
        """
        self.root = None
        if expression:
            self.build_from_postfix(expression)
    
    def build_from_postfix(self, expression):
        """
        Build tree from postfix expression.
        
        Args:
            expression (str): Space-separated postfix expression
        """
        stack = []
        operators = {'+', '-', '*', '/'}
        
        for token in expression.split():
            node = TreeNode(token)
            
            if token in operators:
                # Pop two operands
                node.right = stack.pop()
                node.left = stack.pop()
            
            stack.append(node)
        
        self.root = stack[0] if stack else None
    
    def evaluate(self):
        """
        Evaluate the expression tree.
        
        Returns:
            float: Result of evaluation
        """
        return self._evaluate_recursive(self.root)
    
    def _evaluate_recursive(self, node):
        """Helper method for evaluation."""
        if not node:
            return 0
        
        # Leaf node (operand)
        if not node.left and not node.right:
            return float(node.val)
        
        # Evaluate subtrees
        left_val = self._evaluate_recursive(node.left)
        right_val = self._evaluate_recursive(node.right)
        
        # Apply operator
        if node.val == '+':
            return left_val + right_val
        elif node.val == '-':
            return left_val - right_val
        elif node.val == '*':
            return left_val * right_val
        elif node.val == '/':
            return left_val / right_val if right_val != 0 else 0
    
    def to_infix(self):
        """
        Convert to infix notation.
        
        Returns:
            str: Infix expression
        """
        return self._to_infix_recursive(self.root)
    
    def _to_infix_recursive(self, node):
        """Helper method for infix conversion."""
        if not node:
            return ""
        
        # Leaf node
        if not node.left and not node.right:
            return str(node.val)
        
        # Build infix with parentheses
        left_expr = self._to_infix_recursive(node.left)
        right_expr = self._to_infix_recursive(node.right)
        
        return f"({left_expr} {node.val} {right_expr})"


def demo_bst_operations():
    """Demonstrate BST operations."""
    print("=== BINARY SEARCH TREE OPERATIONS ===\n")
    
    bst = BinarySearchTree()
    
    # Insert values
    values = [50, 30, 70, 20, 40, 60, 80]
    print("Inserting values:", values)
    for val in values:
        bst.insert(val)
    
    print(f"BST: {bst}")
    print(f"Size: {bst.size()}")
    print(f"Height: {bst.height()}")
    print(f"Is balanced: {bst.is_balanced()}")
    print(f"Is valid BST: {bst.is_valid_bst()}")
    
    # Traversals
    print(f"\nInorder (sorted): {bst.inorder_traversal()}")
    print(f"Preorder: {bst.preorder_traversal()}")
    print(f"Postorder: {bst.postorder_traversal()}")
    print(f"Level-order: {bst.level_order_traversal()}")
    
    # Search
    print(f"\nSearch for 40: {bst.search(40) is not None}")
    print(f"Search for 25: {bst.search(25) is not None}")
    
    # Min/Max
    print(f"\nMinimum: {bst.find_min()}")
    print(f"Maximum: {bst.find_max()}")
    
    # Delete
    print(f"\nDeleting 20 (leaf): {bst.delete(20)}")
    print(f"Inorder: {bst.inorder_traversal()}")
    
    print(f"\nDeleting 30 (one child): {bst.delete(30)}")
    print(f"Inorder: {bst.inorder_traversal()}")
    
    print(f"\nDeleting 50 (two children): {bst.delete(50)}")
    print(f"Inorder: {bst.inorder_traversal()}")
    
    print("\n" + "="*50 + "\n")


def demo_avl_tree():
    """Demonstrate AVL tree self-balancing."""
    print("=== AVL TREE (SELF-BALANCING) ===\n")
    
    # Compare BST vs AVL with sequential insertions
    print("Inserting sequential values 1-7:\n")
    
    # Regular BST (becomes skewed)
    bst = BinarySearchTree()
    for i in range(1, 8):
        bst.insert(i)
    
    print(f"BST height: {bst.height()} (skewed)")
    print(f"BST balanced: {bst.is_balanced()}")
    
    # AVL Tree (stays balanced)
    avl = AVLTree()
    for i in range(1, 8):
        avl.insert(i)
    
    print(f"\nAVL height: {avl._get_height(avl.root)} (balanced)")
    print(f"AVL inorder: {avl.inorder_traversal()}")
    
    print("\nAVL tree automatically rebalances during insertion!")
    
    print("\n" + "="*50 + "\n")


def demo_heap_operations():
    """Demonstrate heap operations."""
    print("=== HEAP OPERATIONS ===\n")
    
    # Min Heap
    print("Min Heap:")
    min_heap = MinHeap()
    
    values = [5, 3, 7, 1, 9, 4, 6]
    print(f"Inserting: {values}")
    for val in values:
        min_heap.insert(val)
        print(f"  After inserting {val}: {min_heap.heap}")
    
    print(f"\nMin heap: {min_heap}")
    print(f"Peek (min): {min_heap.peek()}")
    
    print("\nExtracting all elements:")
    while not min_heap.is_empty():
        print(f"  Extracted: {min_heap.extract_min()}")
    
    print()
    
    # Max Heap
    print("Max Heap:")
    max_heap = MaxHeap()
    
    print(f"Inserting: {values}")
    for val in values:
        max_heap.insert(val)
    
    print(f"\nMax heap: {max_heap}")
    print(f"Peek (max): {max_heap.peek()}")
    
    print("\nExtracting all elements:")
    while not max_heap.is_empty():
        print(f"  Extracted: {max_heap.extract_max()}")
    
    print()
    
    # Build heap from array
    print("Build heap from array:")
    arr = [9, 5, 6, 2, 3, 7, 1, 4, 8]
    print(f"Array: {arr}")
    
    heap = MinHeap()
    heap.build_heap(arr)
    print(f"Min heap: {heap.heap}")
    
    print("\n" + "="*50 + "\n")


def demo_priority_queue():
    """Demonstrate priority queue using heap."""
    print("=== PRIORITY QUEUE (TASK SCHEDULER) ===\n")
    
    pq = PriorityQueue()
    
    # Add tasks with priorities
    tasks = [
        ("Fix critical bug", 1),
        ("Write documentation", 3),
        ("Code review", 2),
        ("Deploy to production", 1),
        ("Update dependencies", 3),
        ("Refactor code", 2)
    ]
    
    print("Adding tasks:")
    for task, priority in tasks:
        pq.enqueue(task, priority)
    
    print("\nProcessing tasks by priority:")
    while not pq.is_empty():
        task = pq.dequeue()
    
    print("\n" + "="*50 + "\n")


def demo_expression_tree():
    """Demonstrate expression tree."""
    print("=== EXPRESSION TREE ===\n")
    
    # Postfix expression: 3 4 + 2 *
    # Infix: (3 + 4) * 2 = 14
    postfix = "3 4 + 2 *"
    print(f"Postfix expression: {postfix}")
    
    expr_tree = ExpressionTree(postfix)
    
    print(f"Infix expression: {expr_tree.to_infix()}")
    print(f"Evaluation result: {expr_tree.evaluate()}")
    
    print()
    
    # More complex expression
    postfix2 = "15 7 1 1 + - / 3 * 2 1 1 + + -"
    print(f"Postfix expression: {postfix2}")
    
    expr_tree2 = ExpressionTree(postfix2)
    
    print(f"Infix expression: {expr_tree2.to_infix()}")
    print(f"Evaluation result: {expr_tree2.evaluate()}")
    
    print("\n" + "="*50 + "\n")


def demo_tree_construction():
    """Demonstrate tree construction from list."""
    print("=== TREE CONSTRUCTION FROM LIST ===\n")
    
    # Build tree from level-order list
    values = [1, 2, 3, 4, 5, 6, 7]
    print(f"Level-order values: {values}")
    
    root = build_tree_from_list(values)
    
    print("\nTree structure:")
    print("       1")
    print("      / \\")
    print("     2   3")
    print("    / \\ / \\")
    print("   4  5 6  7")
    
    # Convert back to list
    result = tree_to_list(root)
    print(f"\nConverted back: {result}")
    
    print("\n" + "="*50 + "\n")


def demo_lowest_common_ancestor():
    """Demonstrate LCA in BST."""
    print("=== LOWEST COMMON ANCESTOR (BST) ===\n")
    
    bst = BinarySearchTree()
    values = [20, 10, 30, 5, 15, 25, 35]
    
    print(f"Building BST with values: {values}")
    for val in values:
        bst.insert(val)
    
    print("\nTree structure:")
    print("       20")
    print("      /  \\")
    print("    10    30")
    print("   /  \\  /  \\")
    print("  5   15 25  35")
    
    # Find LCA
    test_pairs = [(5, 15), (5, 35), (25, 35), (10, 30)]
    
    print("\nFinding Lowest Common Ancestor:")
    for p, q in test_pairs:
        lca = lowest_common_ancestor(bst.root, p, q)
        print(f"  LCA({p}, {q}) = {lca.val if lca else None}")
    
    print("\n" + "="*50 + "\n")


def demo_heap_sort():
    """Demonstrate heap sort."""
    print("=== HEAP SORT ===\n")
    
    arr = [12, 11, 13, 5, 6, 7, 3, 9, 1]
    print(f"Original array: {arr}")
    
    # Build max heap
    heap = MaxHeap()
    heap.build_heap(arr)
    print(f"Max heap: {heap.heap}")
    
    # Extract all elements (will be in descending order)
    sorted_desc = []
    while not heap.is_empty():
        sorted_desc.append(heap.extract_max())
    
    print(f"Sorted (descending): {sorted_desc}")
    print(f"Sorted (ascending): {sorted_desc[::-1]}")
    
    print("\nTime Complexity: O(n log n)")
    print("Space Complexity: O(1) in-place")
    
    print("\n" + "="*50 + "\n")


def demo_kth_largest():
    """Demonstrate finding k-th largest element using heap."""
    print("=== FIND K-TH LARGEST ELEMENT ===\n")
    
    arr = [3, 2, 1, 5, 6, 4]
    k = 2
    
    print(f"Array: {arr}")
    print(f"Find {k}-th largest element")
    
    # Use min heap of size k
    heap = MinHeap()
    
    for num in arr:
        heap.insert(num)
        if heap.size() > k:
            heap.extract_min()
    
    result = heap.peek()
    print(f"\n{k}-th largest: {result}")
    print(f"Heap (top {k} largest): {heap.heap}")
    
    print("\nTime Complexity: O(n log k)")
    print("Space Complexity: O(k)")
    
    print("\n" + "="*50 + "\n")


def demo_merge_k_sorted_lists():
    """Demonstrate merging k sorted lists using heap."""
    print("=== MERGE K SORTED LISTS ===\n")
    
    lists = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
    ]
    
    print("Sorted lists:")
    for i, lst in enumerate(lists):
        print(f"  List {i+1}: {lst}")
    
    # Use min heap to merge
    heap = MinHeap()
    
    # Initialize heap with first element from each list
    for i, lst in enumerate(lists):
        if lst:
            heap.insert((lst[0], i, 0))  # (value, list_index, element_index)
    
    result = []
    
    while not heap.is_empty():
        val, list_idx, elem_idx = heap.extract_min()
        result.append(val)
        
        # Add next element from the same list
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heap.insert((next_val, list_idx, elem_idx + 1))
    
    print(f"\nMerged result: {result}")
    
    print("\nTime Complexity: O(n log k) where n = total elements, k = number of lists")
    
    print("\n" + "="*50 + "\n")


def demo_performance_comparison():
    """Compare performance of different tree structures."""
    print("=== PERFORMANCE COMPARISON ===\n")
    
    test_size = 1000
    
    # BST with random insertions
    bst_random = BinarySearchTree()
    random_values = random.sample(range(test_size * 10), test_size)
    
    start = time.time()
    for val in random_values:
        bst_random.insert(val)
    bst_random_time = time.time() - start
    
    # BST with sequential insertions (worst case)
    bst_sequential = BinarySearchTree()
    
    start = time.time()
    for i in range(test_size):
        bst_sequential.insert(i)
    bst_sequential_time = time.time() - start
    
    # AVL with sequential insertions
    avl = AVLTree()
    
    start = time.time()
    for i in range(test_size):
        avl.insert(i)
    avl_time = time.time() - start
    
    print(f"Inserting {test_size} elements:\n")
    print(f"{'Structure':<25} {'Time (s)':<15} {'Height':<10}")
    print("-" * 50)
    print(f"{'BST (random order)':<25} {bst_random_time:<15.6f} {bst_random.height():<10}")
    print(f"{'BST (sequential order)':<25} {bst_sequential_time:<15.6f} {bst_sequential.height():<10}")
    print(f"{'AVL (sequential order)':<25} {avl_time:<15.6f} {avl._get_height(avl.root):<10}")
    
    print("\nKey observations:")
    print("- BST with random order: O(log n) height, good performance")
    print("- BST with sequential order: O(n) height (skewed), poor performance")
    print("- AVL with sequential order: O(log n) height (balanced), consistent performance")
    
    print("\n" + "="*50 + "\n")


def main():
    """Run all demonstrations."""
    print("TREE DATA STRUCTURE - COMPREHENSIVE DEMO")
    print("="*50)
    print()
    
    demo_bst_operations()
    demo_avl_tree()
    demo_heap_operations()
    demo_priority_queue()
    demo_expression_tree()
    demo_tree_construction()
    demo_lowest_common_ancestor()
    demo_heap_sort()
    demo_kth_largest()
    demo_merge_k_sorted_lists()
    demo_performance_comparison()
    
    print("All demonstrations completed!")


if __name__ == "__main__":
    main()
