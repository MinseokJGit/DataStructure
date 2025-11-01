# Linked List Assignment

This assignment contains complete implementations of various linked list data structures and their applications.

## Files Overview

### 1. `linked_list.py` - Core Implementation
Contains three linked list implementations:
- **SinglyLinkedList**: Each node has pointer to next node only
- **DoublyLinkedList**: Each node has pointers to both next and previous nodes
- **CircularLinkedList**: Last node points back to first node (circular)
- **Utility functions**: Merge sorted lists, remove duplicates, find k-th from end

### 2. `application.py` - Practical Applications
Demonstrates real-world use cases of linked lists:
- **Basic Operations Demo**: Shows append, prepend, insert, delete operations
- **Browser History**: Back/forward navigation using doubly linked list
- **Music Playlist**: Circular playlist with continuous playback
- **LRU Cache**: Least Recently Used cache with O(1) operations
- **Undo/Redo Manager**: Text editor undo/redo functionality
- **List Reversal**: In-place reversal algorithms
- **Merge Sorted Lists**: Merging two sorted lists
- **Remove Duplicates**: Efficient duplicate removal
- **Find K-th from End**: Two-pointer technique
- **Cycle Detection**: Floyd's cycle detection algorithm
- **Performance Comparison**: Compare with Python lists

### 3. `test_linked_list.py` - Unit Tests
Comprehensive test suite covering:
- Basic operations for all three implementations
- Edge cases (empty list, single element)
- Insertion and deletion at various positions
- List reversal and manipulation
- Utility functions
- Bidirectional links in doubly linked list
- Circular property in circular linked list
- Different data types

## Key Concepts Demonstrated

### Linked List Types

#### Singly Linked List
```
head → [1|→] → [2|→] → [3|→] → [4|None]
```
- **Advantages**: Simple, less memory per node
- **Disadvantages**: Can't traverse backward, O(n) to delete last

#### Doubly Linked List
```
head → [None|1|→] ⇄ [←|2|→] ⇄ [←|3|→] ⇄ [←|4|None] ← tail
```
- **Advantages**: Bidirectional traversal, O(1) delete last
- **Disadvantages**: More memory (two pointers per node)

#### Circular Linked List
```
     ┌─────────────────────┐
     ↓                     |
head → [1|→] → [2|→] → [3|→] → [4|─]
```
- **Advantages**: Can traverse from any node, no null checks
- **Disadvantages**: Risk of infinite loops, complex termination

### Common Operations

| Operation | Singly (no tail) | Singly (with tail) | Doubly (with tail) |
|-----------|------------------|--------------------|--------------------|
| Append | O(n) | O(1) | O(1) |
| Prepend | O(1) | O(1) | O(1) |
| Insert at i | O(i) | O(i) | O(min(i, n-i)) |
| Delete first | O(1) | O(1) | O(1) |
| Delete last | O(n) | O(n) | O(1) |
| Search | O(n) | O(n) | O(n) |
| Access by index | O(i) | O(i) | O(min(i, n-i)) |

### Important Algorithms

1. **Reversal**: In-place reversal in O(n) time, O(1) space
2. **Find Middle**: Slow-fast pointer technique
3. **Cycle Detection**: Floyd's algorithm (tortoise and hare)
4. **Merge Sorted Lists**: Two-pointer merge in O(n+m) time
5. **Remove Duplicates**: Hash set approach in O(n) time
6. **K-th from End**: Two-pointer with k-step gap

## Running the Code

### Run the comprehensive demo:
```bash
python application.py
```

### Run the unit tests:
```bash
python test_linked_list.py
```

### Example Usage:
```python
from linked_list import SinglyLinkedList, DoublyLinkedList

# Singly linked list
sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.prepend(5)
print(sll.to_list())  # Output: [5, 10, 20]

# Doubly linked list
dll = DoublyLinkedList()
dll.append('A')
dll.append('B')
dll.append('C')
print(dll.to_list())  # Output: ['A', 'B', 'C']
print(dll.to_list_reverse())  # Output: ['C', 'B', 'A']

# Find middle
sll.find_middle()  # Returns 10

# Reverse
sll.reverse()
print(sll.to_list())  # Output: [20, 10, 5]
```

## Assignment Instructions for Students

When adapting this for student assignments:

1. **Hide Core Functions**: Remove implementations of key methods from all list classes
2. **Provide Template**: Give students the class structure with empty method bodies
3. **Include Tests**: Provide the test file so students can verify their implementations
4. **Progressive Difficulty**: 
   - Start with SinglyLinkedList (simpler)
   - Then implement DoublyLinkedList (more complex pointer management)
   - Finally implement CircularLinkedList (tricky termination conditions)
   - Advanced: Implement utility functions

### Student Implementation Template:

#### Singly Linked List Template:
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    
    def append(self, data):
        # TODO: Add element to end
        # Remember to update both head and tail
        # Update size
        pass
    
    def prepend(self, data):
        # TODO: Add element to beginning
        # Remember to handle empty list case
        pass
    
    def delete_first(self):
        # TODO: Delete first element
        # Remember to check for empty list
        # Update tail if list becomes empty
        pass
    
    def reverse(self):
        # TODO: Reverse the list in place
        # Use three pointers: prev, current, next
        pass
    
    def find_middle(self):
        # TODO: Find middle using slow-fast pointers
        # Slow moves 1 step, fast moves 2 steps
        pass
```

#### Doubly Linked List Template:
```python
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    
    def append(self, data):
        # TODO: Add element to end
        # Update both next and prev pointers
        pass
    
    def delete_last(self):
        # TODO: Delete last element in O(1)
        # Use tail pointer for direct access
        pass
    
    def reverse(self):
        # TODO: Reverse by swapping next and prev pointers
        # Also swap head and tail
        pass
```

## Learning Objectives

By completing this assignment, students will:
1. Understand pointer-based data structures
2. Master pointer manipulation and memory management concepts
3. Implement three different linked list variants
4. Analyze time and space complexity trade-offs
5. Apply linked lists to solve real-world problems
6. Practice important algorithms (reversal, cycle detection, two-pointer)
7. Understand when to use linked lists vs arrays

## Common Pitfalls for Students

1. **Null pointer errors**: Not checking for null before dereferencing
2. **Lost references**: Forgetting to save next pointer before changing it
3. **Tail pointer**: Forgetting to update tail in singly linked list
4. **Doubly linked list**: Not updating both prev and next pointers
5. **Circular list**: Infinite loops due to incorrect termination
6. **Edge cases**: Not handling empty list or single element
7. **Memory leaks**: In languages with manual memory management
8. **Off-by-one errors**: In insertion/deletion at specific positions

## Key Pointer Manipulation Patterns

### Pattern 1: Traversal
```python
current = head
while current:
    # Process current.data
    current = current.next
```

### Pattern 2: Insertion After Node
```python
new_node.next = prev_node.next
prev_node.next = new_node
```

### Pattern 3: Deletion After Node
```python
prev_node.next = prev_node.next.next
```

### Pattern 4: Reversal (Three Pointers)
```python
prev = None
current = head
while current:
    next_node = current.next  # Save next
    current.next = prev       # Reverse pointer
    prev = current            # Move prev forward
    current = next_node       # Move current forward
head = prev
```

### Pattern 5: Slow-Fast Pointers
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
# slow is now at middle
```

## Real-World Applications

### 1. Browser History
- **Structure**: Doubly linked list
- **Operations**: Back (prev), Forward (next)
- **Why**: Need bidirectional navigation

### 2. Music Playlist
- **Structure**: Circular linked list
- **Operations**: Next song (continuous loop)
- **Why**: Automatic repeat functionality

### 3. LRU Cache
- **Structure**: Doubly linked list + Hash map
- **Operations**: O(1) get and put
- **Why**: Need to move nodes to front efficiently

### 4. Undo/Redo
- **Structure**: Doubly linked list
- **Operations**: Undo (prev), Redo (next)
- **Why**: Navigate through action history

### 5. Operating System
- **Process scheduling**: Ready queue
- **Memory management**: Free list
- **File systems**: Directory entries

### 6. Hash Table Chaining
- **Structure**: Array of linked lists
- **Operations**: Insert, search, delete
- **Why**: Handle collisions efficiently

## Comparison with Arrays

### When to Use Linked Lists:
- ✓ Frequent insertions/deletions at beginning
- ✓ Unknown or highly variable size
- ✓ Don't need random access
- ✓ Implementing other data structures (stack, queue)
- ✓ Need to frequently split/merge lists

### When to Use Arrays:
- ✓ Need random access by index
- ✓ Size is known or stable
- ✓ Memory locality is important
- ✓ Need to sort or binary search
- ✓ Iteration is primary operation

### Memory Overhead:
```python
# Array: 5 integers
arr = [1, 2, 3, 4, 5]
# Memory: 5 * 4 bytes = 20 bytes (just data)

# Singly Linked List: 5 nodes
# Memory per node: 4 bytes (int) + 8 bytes (pointer) = 12 bytes
# Total: 5 * 12 = 60 bytes (200% overhead!)

# Doubly Linked List: 5 nodes
# Memory per node: 4 bytes (int) + 16 bytes (2 pointers) = 20 bytes
# Total: 5 * 20 = 100 bytes (400% overhead!)
```

## Advanced Topics (Extensions)

1. **Skip List**: Add express lanes for O(log n) search
2. **XOR Linked List**: Store both pointers in one using XOR
3. **Unrolled Linked List**: Store multiple elements per node
4. **Self-organizing List**: Move frequently accessed items to front
5. **Memory Pool**: Allocate nodes from contiguous pool for better cache
6. **Sentinel Nodes**: Dummy head/tail to eliminate edge cases

## Testing Your Implementation

Run the tests to verify your implementation:
```bash
python test_linked_list.py
```

Expected output:
```
test_append (__main__.TestSinglyLinkedList) ... ok
test_delete_first (__main__.TestSinglyLinkedList) ... ok
test_reverse (__main__.TestSinglyLinkedList) ... ok
...
----------------------------------------------------------------------
Ran 50 tests in 0.XXXs

OK
```

## Debugging Tips

1. **Draw diagrams**: Visualize pointer changes on paper
2. **Print statements**: Print node values and addresses
3. **Check invariants**: Verify head, tail, size are consistent
4. **Test edge cases**: Empty list, single element, two elements
5. **Use debugger**: Step through pointer changes
6. **Verify links**: Check both forward and backward links (doubly)

## Grading Rubric (for Instructors)

| Component | Points | Criteria |
|-----------|--------|----------|
| SinglyLinkedList | 30 | All methods implemented correctly |
| DoublyLinkedList | 30 | Proper bidirectional pointer management |
| CircularLinkedList | 20 | Correct circular property and termination |
| Utility Functions | 10 | Merge, remove duplicates, k-th from end |
| Code Quality | 5 | Documentation, style, readability |
| Testing | 5 | All tests pass |
| **Total** | **100** | |

## Performance Characteristics

### Time Complexity Summary:
| Operation | Best Case | Average Case | Worst Case |
|-----------|-----------|--------------|------------|
| Access | O(1) at head | O(n/2) | O(n) |
| Search | O(1) if first | O(n/2) | O(n) |
| Insert (head) | O(1) | O(1) | O(1) |
| Insert (tail) | O(1) with tail | O(1) with tail | O(n) without tail |
| Insert (middle) | O(1) with ref | O(n/2) | O(n) |
| Delete (head) | O(1) | O(1) | O(1) |
| Delete (tail) | O(1) doubly | O(n) singly | O(n) singly |
| Delete (middle) | O(1) with ref | O(n/2) | O(n) |

### Space Complexity:
- **Singly Linked List**: O(n) - one pointer per node
- **Doubly Linked List**: O(n) - two pointers per node
- **Circular Linked List**: O(n) - one pointer per node

## Tips for Success

1. **Start Simple**: Implement and test one method at a time
2. **Draw Pictures**: Visualize pointer changes before coding
3. **Handle Edge Cases**: Always consider empty list and single element
4. **Test Frequently**: Run tests after each method implementation
5. **Use Sentinel Nodes**: Consider dummy head/tail to simplify code
6. **Master Patterns**: Learn the common pointer manipulation patterns
7. **Think Recursively**: Some operations are elegant with recursion
8. **Optimize Later**: Get it working first, then optimize

## Additional Resources

- **Visualization**: [VisuAlgo - Linked List](https://visualgo.net/en/list)
- **Practice**: LeetCode linked list problems
- **Reading**: "Cracking the Coding Interview" - Linked Lists chapter
- **Video**: MIT OpenCourseWare - Linked Lists lecture

## Common Interview Questions

1. Reverse a linked list (iterative and recursive)
2. Detect cycle in a linked list
3. Find the middle of a linked list
4. Merge two sorted linked lists
5. Remove n-th node from end
6. Check if linked list is palindrome
7. Add two numbers represented as linked lists
8. Clone a linked list with random pointers
9. Flatten a multilevel linked list
10. LRU Cache implementation

Good luck with your implementation!
