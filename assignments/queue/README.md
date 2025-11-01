# Queue Assignment

This assignment contains a complete implementation of queue data structures and their applications.

## Files Overview

### 1. `queue.py` - Core Implementation
Contains multiple queue implementations:
- **ArrayQueue**: Simple array-based implementation using Python lists
- **LinkedListQueue**: Linked list-based implementation with O(1) operations
- **CircularQueue**: Fixed-size circular buffer with efficient space usage
- **Deque**: Double-ended queue allowing operations at both ends
- **Utility functions**: Hot potato game, palindrome checker, binary number generation

### 2. `application.py` - Practical Applications
Demonstrates real-world use cases of queues:
- **Basic Operations Demo**: Shows enqueue, dequeue, front operations
- **Task Scheduler**: FIFO task scheduling system
- **Printer Queue**: Simulates printer job management
- **Breadth-First Traversal**: Tree traversal using queues
- **Hot Potato Game**: Classic elimination game simulation
- **Palindrome Checker**: Uses deque to check palindromes
- **Binary Number Generation**: Generates binary numbers using queue
- **Customer Service Queue**: Multi-window service simulation
- **Performance Comparison**: Compares different queue implementations

### 3. `test_queue.py` - Unit Tests
Comprehensive test suite covering:
- Basic queue operations for all implementations
- Exception handling for empty/full queues
- FIFO order verification
- Circular queue wrap-around behavior
- Deque bidirectional operations
- Utility function correctness
- Edge cases and error conditions

## Key Concepts Demonstrated

### Queue Operations (FIFO - First In, First Out)
- `enqueue(item)`: Add item to rear
- `dequeue()`: Remove and return front item
- `front()`: View front item without removing
- `is_empty()`: Check if queue is empty
- `size()`: Get number of elements

### Implementation Comparison
| Feature | ArrayQueue | LinkedListQueue | CircularQueue |
|---------|------------|-----------------|---------------|
| Enqueue | O(1) | O(1) | O(1) |
| Dequeue | O(n) | O(1) | O(1) |
| Space | Dynamic | Dynamic + pointers | Fixed |
| Best For | Simple use | General purpose | Bounded buffer |

### Deque Operations (Double-Ended Queue)
- `add_front(item)`: Add item to front
- `add_rear(item)`: Add item to rear
- `remove_front()`: Remove from front
- `remove_rear()`: Remove from rear

### Applications Covered
1. **Task Scheduling**: FIFO job scheduling
2. **Breadth-First Search**: Level-order tree traversal
3. **Buffering**: Printer queue, customer service
4. **Game Simulation**: Hot potato elimination game
5. **String Processing**: Palindrome checking with deque
6. **Number Generation**: Binary numbers using queue pattern

## Running the Code

### Run the comprehensive demo:
```bash
python application.py
```

### Run the unit tests:
```bash
python test_queue.py
```

### Example Usage:
```python
from queue import LinkedListQueue, CircularQueue, Deque

# Basic queue operations
queue = LinkedListQueue()
queue.enqueue(10)
queue.enqueue(20)
print(queue.dequeue())  # Output: 10

# Circular queue with fixed capacity
circular = CircularQueue(5)
for i in range(5):
    circular.enqueue(i)
print(circular.is_full())  # Output: True

# Deque operations
deque = Deque()
deque.add_front(1)
deque.add_rear(2)
print(deque.remove_front())  # Output: 1
```

## Assignment Instructions for Students

When adapting this for student assignments:

1. **Hide Core Functions**: Remove implementations of enqueue, dequeue, front, is_empty, size from all queue classes
2. **Provide Template**: Give students the class structure with empty method bodies
3. **Include Tests**: Provide the test file so students can verify their implementations
4. **Progressive Difficulty**: 
   - Start with ArrayQueue (simpler but less efficient)
   - Then implement LinkedListQueue (more efficient)
   - Implement CircularQueue (fixed capacity with wrap-around)
   - Finally implement Deque (bidirectional operations)

### Student Implementation Template:
```python
class ArrayQueue:
    def __init__(self):
        self._data = []
    
    def enqueue(self, item):
        # TODO: Implement enqueue operation
        # Add item to the rear of the queue
        pass
    
    def dequeue(self):
        # TODO: Implement dequeue operation
        # Remove and return the front item
        # Remember to check for empty queue and raise IndexError
        pass
    
    def front(self):
        # TODO: Implement front operation
        # Return front item without removing it
        pass
    
    def is_empty(self):
        # TODO: Check if queue is empty
        pass
    
    def size(self):
        # TODO: Return number of items in queue
        pass
```

### Circular Queue Template:
```python
class CircularQueue:
    def __init__(self, capacity=10):
        self._capacity = capacity
        self._data = [None] * capacity
        self._front = 0
        self._rear = 0
        self._size = 0
    
    def enqueue(self, item):
        # TODO: Implement enqueue with wrap-around
        # Use modulo arithmetic: (index + 1) % capacity
        # Check for full queue and raise OverflowError
        pass
    
    def dequeue(self):
        # TODO: Implement dequeue with wrap-around
        # Update front pointer using modulo
        pass
    
    # ... other methods
```

## Learning Objectives

By completing this assignment, students will:
1. Understand FIFO (First In, First Out) principle
2. Implement queue using different underlying data structures
3. Analyze time and space complexity trade-offs
4. Master circular buffer concept with modulo arithmetic
5. Apply queues to solve real-world problems (BFS, scheduling, buffering)
6. Practice exception handling and edge cases
7. Understand the difference between queue and deque

## Common Pitfalls for Students

1. **Array Queue Inefficiency**: Not realizing that `list.pop(0)` is O(n)
2. **Circular Queue Logic**: Confusion with wrap-around using modulo arithmetic
3. **Full vs Empty**: In circular queue, distinguishing between full and empty states
4. **Linked List Pointers**: Forgetting to update both front and rear pointers
5. **Edge Cases**: Not handling empty queue or full circular queue properly
6. **Deque Confusion**: Mixing up front and rear operations

## Circular Queue Key Concepts

The circular queue uses modulo arithmetic to wrap around:
```
Indices: [0] [1] [2] [3] [4]
         
After wrapping:
front = 3, rear = 1
         [5] [6] [_] [3] [4]
              ^       ^
            rear    front
```

Formula: `next_index = (current_index + 1) % capacity`

## Extension Ideas

1. Implement a **Priority Queue** using a heap
2. Create a **Deque using circular array** for O(1) operations at both ends
3. Implement **queue using two stacks**
4. Create a **thread-safe queue** with locks
5. Implement **level-order tree traversal** variations (zigzag, reverse)
6. Build a **task scheduler with priorities**
7. Simulate **CPU scheduling algorithms** (Round Robin, FCFS)

## Real-World Applications

### Operating Systems
- **Process Scheduling**: Ready queue for CPU scheduling
- **I/O Buffering**: Keyboard buffer, printer spooler
- **Disk Scheduling**: Request queue for disk operations

### Networking
- **Packet Queues**: Router buffers for packet forwarding
- **Message Queues**: Asynchronous communication between services
- **Rate Limiting**: Token bucket algorithm

### Algorithms
- **Breadth-First Search**: Graph and tree traversal
- **Level-Order Traversal**: Binary tree operations
- **Shortest Path**: BFS for unweighted graphs

### Software Systems
- **Task Queues**: Background job processing (Celery, RabbitMQ)
- **Event Loops**: JavaScript event queue, GUI event handling
- **Cache Replacement**: FIFO cache eviction policy

## Performance Characteristics

### Time Complexity Summary
| Operation | ArrayQueue | LinkedListQueue | CircularQueue | Deque |
|-----------|------------|-----------------|---------------|-------|
| enqueue | O(1) | O(1) | O(1) | O(1) rear, O(n) front |
| dequeue | O(n) | O(1) | O(1) | O(n) front, O(1) rear |
| front | O(1) | O(1) | O(1) | O(1) |
| is_empty | O(1) | O(1) | O(1) | O(1) |
| size | O(1) | O(1) | O(1) | O(1) |

### Space Complexity
- **ArrayQueue**: O(n) - dynamic resizing
- **LinkedListQueue**: O(n) - extra space for node pointers
- **CircularQueue**: O(capacity) - fixed size
- **Deque**: O(n) - similar to ArrayQueue

### Recommendations
- **Use LinkedListQueue** for general-purpose queuing (best O(1) performance)
- **Use CircularQueue** for bounded buffers with known capacity
- **Use ArrayQueue** only for simple cases or when dequeue is infrequent
- **Use Deque** when you need operations at both ends

## Testing Your Implementation

Run the tests to verify your implementation:
```bash
python test_queue.py
```

Expected output:
```
test_dequeue (__main__.TestArrayQueue) ... ok
test_enqueue (__main__.TestArrayQueue) ... ok
test_fifo_order (__main__.TestArrayQueue) ... ok
...
----------------------------------------------------------------------
Ran 40 tests in 0.XXXs

OK
```

## Additional Resources

- **Visualization**: [VisuAlgo - Queue](https://visualgo.net/en/list)
- **Practice Problems**: LeetCode queue problems
- **Further Reading**: "Introduction to Algorithms" (CLRS) Chapter on Elementary Data Structures

## Grading Rubric (for Instructors)

| Component | Points | Criteria |
|-----------|--------|----------|
| ArrayQueue | 20 | All methods implemented correctly |
| LinkedListQueue | 25 | Proper pointer management, O(1) operations |
| CircularQueue | 25 | Correct modulo arithmetic, full/empty handling |
| Deque | 15 | Bidirectional operations working |
| Code Quality | 10 | Documentation, style, readability |
| Testing | 5 | All tests pass |
| **Total** | **100** | |

## Tips for Success

1. **Start Simple**: Begin with ArrayQueue, then move to more complex implementations
2. **Draw Diagrams**: Visualize pointer movements and array indices
3. **Test Incrementally**: Test each method as you implement it
4. **Handle Edge Cases**: Empty queue, full queue, single element
5. **Use the Tests**: Run tests frequently to catch bugs early
6. **Understand Modulo**: Master `(index + 1) % capacity` for circular queue
7. **Check Pointers**: In linked list, ensure front and rear are updated correctly
