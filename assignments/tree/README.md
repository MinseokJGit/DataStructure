# Tree Assignment

This assignment contains complete implementations of various tree data structures and their applications.

## Files Overview

### 1. `tree.py` - Core Implementation
Contains multiple tree implementations:
- **BinarySearchTree (BST)**: Ordered binary tree with left < root < right property
- **AVLTree**: Self-balancing BST with guaranteed O(log n) operations
- **MinHeap**: Binary heap with parent ≤ children property
- **MaxHeap**: Binary heap with parent ≥ children property
- **Utility functions**: Tree construction, LCA finding

### 2. `application.py` - Practical Applications
Demonstrates real-world use cases of trees:
- **BST Operations**: Insert, delete, search, traversals
- **AVL Tree**: Self-balancing demonstration
- **Heap Operations**: Insert, extract, build heap
- **Priority Queue**: Task scheduling using heap
- **Expression Tree**: Parse and evaluate arithmetic expressions
- **Tree Construction**: Build from level-order list
- **Lowest Common Ancestor**: Find LCA in BST
- **Heap Sort**: Sorting using heap
- **K-th Largest**: Find k-th largest element
- **Merge K Lists**: Merge sorted lists using heap
- **Performance Comparison**: BST vs AVL performance

### 3. `test_tree.py` - Unit Tests
Comprehensive test suite covering:
- BST operations (insert, delete, search, traversals)
- AVL tree balancing and rotations
- Min/Max heap operations
- Heap property verification
- Utility functions
- Edge cases (empty tree, single node, large tree)

## Key Concepts Demonstrated

### Binary Search Tree (BST)

**Structure:**
```
       50
      /  \
    30    70
   / \   / \
  20 40 60 80
```

**BST Property:** For every node:
- All values in left subtree < node value
- All values in right subtree > node value

**Operations:**
| Operation | Average | Worst Case |
|-----------|---------|------------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |
| Traversal | O(n) | O(n) |

### Traversal Methods

1. **Inorder (Left-Root-Right)**: Gives sorted order for BST
2. **Preorder (Root-Left-Right)**: Used for copying tree
3. **Postorder (Left-Right-Root)**: Used for deleting tree
4. **Level-order (BFS)**: Level by level traversal

**Example:**
```
Tree:    4
        / \
       2   6
      / \ / \
     1  3 5  7

Inorder:    [1, 2, 3, 4, 5, 6, 7]
Preorder:   [4, 2, 1, 3, 6, 5, 7]
Postorder:  [1, 3, 2, 5, 7, 6, 4]
Level-order: [4, 2, 6, 1, 3, 5, 7]
```

### AVL Tree (Self-Balancing BST)

**Balance Factor:** height(left) - height(right) ∈ {-1, 0, 1}

**Rotations:**
- **Left Rotation**: Fix right-heavy imbalance
- **Right Rotation**: Fix left-heavy imbalance
- **Left-Right**: Double rotation for left-right case
- **Right-Left**: Double rotation for right-left case

**Advantages:**
- Guaranteed O(log n) for all operations
- Height ≤ 1.44 log n
- No worst-case O(n) like unbalanced BST

### Heap (Binary Heap)

**Min Heap Property:** Parent ≤ Children
**Max Heap Property:** Parent ≥ Children

**Array Representation:**
```
For node at index i:
- Parent: (i - 1) // 2
- Left child: 2 * i + 1
- Right child: 2 * i + 2
```

**Operations:**
| Operation | Time Complexity |
|-----------|----------------|
| Insert | O(log n) |
| Extract Min/Max | O(log n) |
| Peek | O(1) |
| Build Heap | O(n) |

## Running the Code

### Run the comprehensive demo:
```bash
python application.py
```

### Run the unit tests:
```bash
python test_tree.py
```

### Example Usage:

#### Binary Search Tree:
```python
from tree import BinarySearchTree

bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)

print(bst.inorder_traversal())  # [30, 50, 70]
print(bst.search(30))  # TreeNode object
print(bst.find_min())  # 30
print(bst.find_max())  # 70

bst.delete(30)
print(bst.inorder_traversal())  # [50, 70]
```

#### AVL Tree:
```python
from tree import AVLTree

avl = AVLTree()
# Insert sequential values - stays balanced!
for i in range(1, 8):
    avl.insert(i)

print(avl.inorder_traversal())  # [1, 2, 3, 4, 5, 6, 7]
# Height is O(log n) instead of O(n)
```

#### Min Heap:
```python
from tree import MinHeap

heap = MinHeap()
for val in [5, 3, 7, 1, 9]:
    heap.insert(val)

print(heap.peek())  # 1
print(heap.extract_min())  # 1
print(heap.extract_min())  # 3
```

## Assignment Instructions for Students

When adapting this for student assignments:

1. **Hide Core Functions**: Remove implementations of key methods
2. **Provide Template**: Give students the class structure with empty method bodies
3. **Include Tests**: Provide the test file for verification
4. **Progressive Difficulty**: 
   - Start with BST (basic tree operations)
   - Then implement traversals (recursive and iterative)
   - Implement heap (array-based structure)
   - Advanced: AVL tree with rotations

### Student Implementation Template:

#### BST Template:
```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self._size = 0
    
    def insert(self, val):
        # TODO: Insert value into BST
        # Use recursive helper method
        # Remember to update size
        pass
    
    def search(self, val):
        # TODO: Search for value
        # Return node if found, None otherwise
        # Compare with current node and recurse
        pass
    
    def delete(self, val):
        # TODO: Delete value from BST
        # Handle three cases:
        #   1. Leaf node (no children)
        #   2. One child
        #   3. Two children (use inorder successor)
        pass
    
    def inorder_traversal(self):
        # TODO: Implement inorder traversal
        # Order: Left -> Root -> Right
        # Should return sorted list for BST
        pass
```

#### Heap Template:
```python
class MinHeap:
    def __init__(self):
        self.heap = []
    
    def _parent(self, i):
        return (i - 1) // 2
    
    def _left_child(self, i):
        return 2 * i + 1
    
    def _right_child(self, i):
        return 2 * i + 2
    
    def insert(self, val):
        # TODO: Insert value into heap
        # 1. Append to end of array
        # 2. Heapify up to maintain heap property
        pass
    
    def extract_min(self):
        # TODO: Remove and return minimum
        # 1. Save root value
        # 2. Move last element to root
        # 3. Heapify down to maintain heap property
        pass
    
    def _heapify_up(self, i):
        # TODO: Bubble up element at index i
        # Compare with parent and swap if needed
        pass
    
    def _heapify_down(self, i):
        # TODO: Bubble down element at index i
        # Compare with children and swap with smallest
        pass
```

## Learning Objectives

By completing this assignment, students will:
1. Understand hierarchical data structures
2. Implement binary search tree with insert, delete, search
3. Master tree traversal algorithms (inorder, preorder, postorder, level-order)
4. Understand heap structure and operations
5. Implement self-balancing trees (AVL)
6. Apply trees to solve real-world problems
7. Analyze time and space complexity of tree operations
8. Understand the importance of balanced trees

## Common Pitfalls for Students

1. **Null pointer errors**: Not checking for null nodes before accessing
2. **BST property violation**: Incorrect insertion/deletion breaking BST property
3. **Recursion confusion**: Forgetting base cases or return values
4. **Heap indexing**: Off-by-one errors in parent/child calculations
5. **Delete complexity**: Not handling all three cases correctly
6. **Traversal order**: Mixing up the order of operations
7. **Memory leaks**: In languages with manual memory management
8. **Balance factor**: Incorrect calculation in AVL trees

## Key Algorithms

### 1. BST Insertion (Recursive)
```python
def insert(root, val):
    if not root:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    
    return root
```

### 2. BST Deletion (Three Cases)
```python
def delete(root, val):
    if not root:
        return None
    
    if val < root.val:
        root.left = delete(root.left, val)
    elif val > root.val:
        root.right = delete(root.right, val)
    else:
        # Case 1: No children
        if not root.left and not root.right:
            return None
        
        # Case 2: One child
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        
        # Case 3: Two children
        successor = find_min(root.right)
        root.val = successor.val
        root.right = delete(root.right, successor.val)
    
    return root
```

### 3. Inorder Traversal (Iterative)
```python
def inorder_iterative(root):
    result = []
    stack = []
    current = root
    
    while current or stack:
        # Go to leftmost node
        while current:
            stack.append(current)
            current = current.left
        
        # Process node
        current = stack.pop()
        result.append(current.val)
        
        # Go to right subtree
        current = current.right
    
    return result
```

### 4. Heap Insert
```python
def insert(self, val):
    self.heap.append(val)
    self._heapify_up(len(self.heap) - 1)

def _heapify_up(self, i):
    while i > 0:
        parent = (i - 1) // 2
        if self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = \
                self.heap[parent], self.heap[i]
            i = parent
        else:
            break
```

## Real-World Applications

### 1. Database Indexing
- **B-Trees**: Used in MySQL, PostgreSQL for indexing
- **Why**: Optimized for disk I/O, high fanout
- **Operations**: O(log n) search, range queries

### 2. File Systems
- **Directory Structure**: Tree hierarchy
- **Operations**: Navigate, search files
- **Example**: Unix file system

### 3. Expression Parsing
- **Parse Trees**: Represent arithmetic expressions
- **Operations**: Evaluate, convert notations
- **Use**: Compilers, calculators

### 4. Priority Queues
- **Heap-based**: Task scheduling, event simulation
- **Operations**: O(log n) insert/extract
- **Use**: OS schedulers, Dijkstra's algorithm

### 5. Auto-complete
- **Trie Trees**: Prefix-based search
- **Operations**: O(k) where k = key length
- **Use**: Search engines, IDEs

### 6. Decision Trees
- **Machine Learning**: Classification/regression
- **Structure**: Internal nodes = tests, leaves = decisions
- **Use**: Random forests, gradient boosting

## Performance Characteristics

### BST vs AVL vs Heap

| Operation | BST (avg) | BST (worst) | AVL | Heap |
|-----------|-----------|-------------|-----|------|
| Search | O(log n) | O(n) | O(log n) | O(n) |
| Insert | O(log n) | O(n) | O(log n) | O(log n) |
| Delete | O(log n) | O(n) | O(log n) | O(log n) |
| Find Min | O(log n) | O(n) | O(log n) | O(1) |
| Find Max | O(log n) | O(n) | O(log n) | O(n) |

### Space Complexity
- **Tree Storage**: O(n) for n nodes
- **Recursive Traversal**: O(h) stack space (h = height)
- **Iterative Traversal**: O(h) for explicit stack/queue

### Height Analysis
```
Best case (balanced): h = log₂ n
Worst case (skewed): h = n

Example: n = 1000 nodes
- Balanced: h ≈ 10 (very fast)
- Skewed: h = 1000 (slow as linked list)
```

## Testing Your Implementation

Run the tests to verify your implementation:
```bash
python test_tree.py
```

Expected output:
```
test_insert (__main__.TestBinarySearchTree) ... ok
test_delete_leaf (__main__.TestBinarySearchTree) ... ok
test_inorder_traversal (__main__.TestBinarySearchTree) ... ok
...
----------------------------------------------------------------------
Ran 45 tests in 0.XXXs

OK
```

## Debugging Tips

1. **Visualize**: Draw the tree on paper before coding
2. **Print statements**: Print tree structure during operations
3. **Small examples**: Test with 3-5 nodes first
4. **Check invariants**: Verify BST property, heap property
5. **Traversal verification**: Use inorder to check BST property
6. **Base cases**: Always handle null/empty cases
7. **Recursive thinking**: Trust the recursion for subtrees

## Grading Rubric (for Instructors)

| Component | Points | Criteria |
|-----------|--------|----------|
| BST Insert/Search | 15 | Correct implementation |
| BST Delete | 15 | All three cases handled |
| Traversals | 15 | All four methods correct |
| Heap Operations | 20 | Insert, extract, heapify |
| AVL Tree (bonus) | 10 | Rotations and balancing |
| Code Quality | 10 | Documentation, style |
| Testing | 15 | All tests pass |
| **Total** | **100** | |

## Advanced Topics (Extensions)

1. **Red-Black Trees**: Alternative self-balancing BST
2. **B-Trees**: Multi-way trees for databases
3. **Tries**: Prefix trees for string operations
4. **Segment Trees**: Range query optimization
5. **Fenwick Trees**: Efficient prefix sums
6. **Splay Trees**: Self-adjusting BST
7. **Treaps**: Randomized BST

## Common Interview Questions

1. Validate if a tree is a valid BST
2. Find lowest common ancestor
3. Serialize and deserialize binary tree
4. Maximum path sum in binary tree
5. Level-order traversal (zigzag)
6. Convert sorted array to balanced BST
7. Find k-th smallest element in BST
8. Implement iterator for BST
9. Check if tree is balanced
10. Mirror/invert binary tree

## Tips for Success

1. **Master recursion**: Most tree operations are recursive
2. **Draw pictures**: Visualize before coding
3. **Test incrementally**: Test each method as you implement
4. **Understand invariants**: BST property, heap property
5. **Practice traversals**: Know all four by heart
6. **Handle edge cases**: Empty tree, single node, null pointers
7. **Use helper methods**: Separate recursive logic
8. **Think about base cases**: What's the simplest case?

## Additional Resources

- **Visualization**: [VisuAlgo - BST](https://visualgo.net/en/bst)
- **Practice**: LeetCode tree problems
- **Reading**: "Introduction to Algorithms" (CLRS) - Tree chapters
- **Video**: MIT OpenCourseWare - Binary Search Trees

Good luck with your implementation!
