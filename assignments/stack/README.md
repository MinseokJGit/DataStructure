# Stack Assignment

This assignment contains a complete implementation of stack data structures and their applications.

## Files Overview

### 1. `stack.py` - Core Implementation
Contains two stack implementations:
- **ArrayStack**: Array-based implementation using Python lists
- **LinkedListStack**: Linked list-based implementation using Node objects
- **Utility functions**: Parentheses balancing, postfix evaluation, infix to postfix conversion

### 2. `application.py` - Practical Applications
Demonstrates real-world use cases of stacks:
- **Basic Operations Demo**: Shows push, pop, peek operations
- **Parentheses Balancing**: Validates bracket matching in expressions
- **Expression Evaluation**: Postfix evaluation and infix to postfix conversion
- **Text Editor**: Undo/redo functionality using two stacks
- **Function Call Simulation**: Demonstrates how recursion uses the call stack
- **Performance Comparison**: Compares array vs linked list implementations

### 3. `test_stack.py` - Unit Tests
Comprehensive test suite covering:
- Basic stack operations for both implementations
- Exception handling for empty stacks
- Utility function correctness
- Edge cases and error conditions

## Key Concepts Demonstrated

### Stack Operations (LIFO - Last In, First Out)
- `push(item)`: Add item to top
- `pop()`: Remove and return top item
- `peek()`: View top item without removing
- `is_empty()`: Check if stack is empty
- `size()`: Get number of elements

### Implementation Comparison
| Feature | ArrayStack | LinkedListStack |
|---------|------------|-----------------|
| Time Complexity | O(1) amortized | O(1) guaranteed |
| Space Efficiency | Better (contiguous memory) | More overhead (pointers) |
| Cache Performance | Excellent | Fair |
| Resize Cost | Occasional O(n) | Never |

### Applications Covered
1. **Expression Evaluation**: Converting and evaluating mathematical expressions
2. **Syntax Checking**: Validating balanced parentheses, brackets, braces
3. **Undo/Redo Systems**: Managing reversible operations
4. **Function Calls**: Understanding how recursion works with call stacks

## Running the Code

### Run the comprehensive demo:
```bash
python application.py
```

### Run the unit tests:
```bash
python test_stack.py
```

### Example Usage:
```python
from stack import ArrayStack, is_balanced_parentheses, evaluate_postfix

# Basic stack operations
stack = ArrayStack()
stack.push(10)
stack.push(20)
print(stack.pop())  # Output: 20

# Check balanced parentheses
print(is_balanced_parentheses("([{}])"))  # Output: True

# Evaluate postfix expression
print(evaluate_postfix("3 4 + 2 *"))  # Output: 14.0
```

## Assignment Instructions for Students

When adapting this for student assignments:

1. **Hide Core Functions**: Remove implementations of push, pop, peek, is_empty, size from both stack classes
2. **Provide Template**: Give students the class structure with empty method bodies
3. **Include Tests**: Provide the test file so students can verify their implementations
4. **Progressive Difficulty**: 
   - Start with ArrayStack (simpler)
   - Then implement LinkedListStack
   - Finally implement utility functions

### Student Implementation Template:
```python
class ArrayStack:
    def __init__(self):
        self._data = []
    
    def push(self, item):
        # TODO: Implement push operation
        pass
    
    def pop(self):
        # TODO: Implement pop operation
        # Remember to check for empty stack and raise IndexError
        pass
    
    # ... other methods
```

## Learning Objectives

By completing this assignment, students will:
1. Understand LIFO (Last In, First Out) principle
2. Implement stack using different underlying data structures
3. Analyze time and space complexity trade-offs
4. Apply stacks to solve real-world problems
5. Practice exception handling and edge cases
6. Gain experience with both iterative and recursive thinking

## Common Pitfalls for Students

1. **Forgetting edge cases**: Not handling empty stack conditions
2. **Index errors**: Incorrect array indexing in ArrayStack
3. **Memory leaks**: Not properly updating links in LinkedListStack
4. **Off-by-one errors**: Incorrect size tracking
5. **Exception handling**: Not raising appropriate exceptions

## Extension Ideas

1. Implement a `MinStack` that tracks minimum element
2. Add iterator support to traverse stack elements
3. Implement stack using two queues
4. Create a stack that supports undo operations on stack operations themselves
5. Implement expression parsing with operator precedence