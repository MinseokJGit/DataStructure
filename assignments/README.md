# Data Structure Assignments

This directory contains comprehensive programming assignments for the Data Structure course. Each assignment includes complete implementations, practical applications, unit tests, and detailed documentation.

## 📚 Assignment Overview

### 1. Stack Assignment
**Location:** `stack/`

**Topics Covered:**
- Array-based stack implementation
- Linked list-based stack implementation
- Stack operations: push, pop, peek, is_empty
- Applications: Expression evaluation, parentheses matching, undo/redo, browser history

**Key Concepts:**
- LIFO (Last In, First Out) principle
- O(1) push and pop operations
- Practical use cases in text editors and compilers

**Files:**
- `stack.py` - Core implementations
- `application.py` - Real-world applications
- `test_stack.py` - Unit tests
- `README.md` - Documentation

---

### 2. Queue Assignment
**Location:** `queue/`

**Topics Covered:**
- Array-based queue implementation
- Linked list-based queue implementation
- Circular queue with wrap-around
- Deque (double-ended queue)
- Priority queue concepts

**Key Concepts:**
- FIFO (First In, First Out) principle
- Circular buffer optimization
- Applications in task scheduling and BFS

**Files:**
- `queue.py` - Core implementations
- `application.py` - Task scheduling, printer queue, BFS
- `test_queue.py` - Unit tests
- `README.md` - Documentation

---

### 3. Linked List Assignment
**Location:** `linked_list/`

**Topics Covered:**
- Singly linked list
- Doubly linked list
- Circular linked list
- Common algorithms: reversal, cycle detection, finding middle

**Key Concepts:**
- Pointer manipulation
- O(1) insertion/deletion at known positions
- Trade-offs vs arrays (memory overhead, cache locality)

**Files:**
- `linked_list.py` - Three list implementations
- `application.py` - Browser history, music playlist, LRU cache
- `test_linked_list.py` - Unit tests
- `README.md` - Documentation

---

### 4. Tree Assignment
**Location:** `tree/`

**Topics Covered:**
- Binary Search Tree (BST)
- AVL Tree (self-balancing)
- Min Heap and Max Heap
- Tree traversals: inorder, preorder, postorder, level-order

**Key Concepts:**
- Hierarchical data organization
- O(log n) operations with balanced trees
- Heap property and heapify operations
- Applications in databases and priority queues

**Files:**
- `tree.py` - BST, AVL, Min/Max Heap
- `application.py` - Priority queue, expression trees, heap sort
- `test_tree.py` - Unit tests
- `README.md` - Documentation

---

### 5. Trie Assignment
**Location:** `trie/`

**Topics Covered:**
- Standard trie (prefix tree)
- Frequency trie for ranking
- Wildcard pattern matching
- Prefix-based queries and autocomplete

**Key Concepts:**
- O(m) operations where m = word length
- Space-efficient for shared prefixes
- Applications in autocomplete and spell checking

**Files:**
- `trie.py` - Trie implementations
- `application.py` - Autocomplete, spell checker, contact search
- `test_trie.py` - Unit tests
- `README.md` - Documentation

---

### 6. Graph Assignment
**Location:** `graph/`

**Topics Covered:**
- Undirected and directed graphs
- Weighted graphs
- BFS and DFS traversals
- Shortest path algorithms (Dijkstra's)
- Topological sort
- Cycle detection
- Union-Find (Disjoint Set)

**Key Concepts:**
- Adjacency list representation
- O(V + E) traversal algorithms
- Real-world modeling (social networks, maps, dependencies)

**Files:**
- `graph.py` - Multiple graph implementations
- `application.py` - Social network, GPS navigation, dependency resolution
- `test_graph.py` - Unit tests
- `README.md` - Documentation

---

## 🎯 Learning Progression

The assignments are designed to build upon each other:

1. **Stack & Queue** → Basic linear data structures, foundation for algorithms
2. **Linked List** → Pointer manipulation, dynamic memory management
3. **Tree** → Hierarchical structures, recursion, balanced structures
4. **Trie** → Specialized tree for string operations
5. **Graph** → Complex relationships, advanced algorithms

## 📋 Assignment Structure

Each assignment follows a consistent structure:

```
assignment_name/
├── data_structure.py    # Core implementation
├── application.py       # Practical demonstrations
├── test_*.py           # Comprehensive unit tests
└── README.md           # Documentation and instructions
```

### Core Implementation (`*.py`)
- Complete, working implementations
- Well-documented with docstrings
- Complexity analysis in comments
- Multiple variants where applicable

### Applications (`application.py`)
- 8-12 real-world demonstrations
- Practical use cases
- Performance comparisons
- Interactive examples

### Unit Tests (`test_*.py`)
- 40-50+ test cases per assignment
- Edge case coverage
- Property verification
- Performance tests

### Documentation (`README.md`)
- Concept explanations with visuals
- Complexity tables
- Usage examples
- **Student templates** for assignments
- Common pitfalls and debugging tips
- Grading rubrics

## 🎓 For Students

### How to Use These Assignments

1. **Read the README** in each assignment folder
2. **Study the implementations** to understand the concepts
3. **Run the applications** to see practical uses
4. **Run the tests** to verify correctness
5. **Complete the templates** provided in the README

### Converting to Student Assignments

Each README includes a section on hiding implementations for student work. Instructors can:

1. Remove method bodies from core classes
2. Provide TODO comments for guidance
3. Keep the test files for verification
4. Use the grading rubrics provided

### Running the Code

```bash
# Navigate to any assignment folder
cd stack/  # or queue/, linked_list/, tree/, trie/, graph/

# Run the demonstration
python application.py

# Run the tests
python test_*.py
```

## 📊 Complexity Summary

| Data Structure | Access | Search | Insert | Delete | Space |
|----------------|--------|--------|--------|--------|-------|
| **Stack** | O(n) | O(n) | O(1) | O(1) | O(n) |
| **Queue** | O(n) | O(n) | O(1) | O(1) | O(n) |
| **Linked List** | O(n) | O(n) | O(1)* | O(1)* | O(n) |
| **BST (avg)** | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| **AVL Tree** | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| **Heap** | O(1)† | O(n) | O(log n) | O(log n) | O(n) |
| **Trie** | O(m) | O(m) | O(m) | O(m) | O(ALPHABET × N × M) |
| **Graph** | O(1)‡ | O(V+E) | O(1) | O(E) | O(V+E) |

*With reference to node  
†For min/max element  
‡For adjacency check with adjacency matrix  
m = key length, V = vertices, E = edges

## 🔧 Common Operations Across Data Structures

### Basic Operations
- **Insert**: Add element to structure
- **Delete**: Remove element from structure
- **Search**: Find element in structure
- **Traverse**: Visit all elements

### Advanced Operations
- **Sort**: Order elements (heap sort, BST inorder)
- **Find Path**: Shortest path (BFS, Dijkstra's)
- **Detect Cycle**: Check for cycles (DFS)
- **Balance**: Maintain structure (AVL rotations)

## 🌟 Real-World Applications

### Stack
- Function call stack
- Undo/redo functionality
- Expression evaluation
- Browser back button

### Queue
- Task scheduling
- Printer queue
- BFS algorithm
- Message queues

### Linked List
- Music playlist
- Browser history
- LRU cache
- Undo/redo with navigation

### Tree
- File system hierarchy
- Database indexing
- Expression parsing
- Priority queues

### Trie
- Autocomplete
- Spell checker
- IP routing
- Dictionary implementation

### Graph
- Social networks
- GPS navigation
- Web page ranking
- Dependency resolution

## 📝 Grading Guidelines

Each assignment can be graded on:

1. **Correctness** (40%): Implementation works as specified
2. **Testing** (20%): All tests pass
3. **Code Quality** (20%): Clean, documented, follows style
4. **Complexity** (10%): Meets time/space requirements
5. **Understanding** (10%): Can explain design decisions

Detailed rubrics are provided in each assignment's README.

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- Basic understanding of Python syntax
- Familiarity with object-oriented programming

### Installation
No installation required! All assignments use Python standard library only.

### Quick Start
```bash
# Clone or download the repository
cd DataStructure/assignments

# Try the stack assignment
cd stack
python application.py

# Run tests
python test_stack.py
```

## 📚 Additional Resources

### Visualization Tools
- [VisuAlgo](https://visualgo.net/) - Algorithm visualizations
- [Python Tutor](http://pythontutor.com/) - Code execution visualization

### Practice Platforms
- [LeetCode](https://leetcode.com/) - Coding problems by topic
- [HackerRank](https://www.hackerrank.com/) - Data structure challenges

### Reference Books
- "Introduction to Algorithms" (CLRS)
- "Data Structures and Algorithms in Python"
- "Cracking the Coding Interview"

## 💡 Tips for Success

1. **Start Simple**: Begin with basic operations before advanced features
2. **Draw Pictures**: Visualize data structures on paper
3. **Test Incrementally**: Test each method as you implement it
4. **Understand Complexity**: Know why each operation takes the time it does
5. **Practice Problems**: Apply concepts to LeetCode problems
6. **Debug Systematically**: Use print statements and debugger
7. **Read Documentation**: Study the provided README files carefully

## 🤝 Contributing

If you find issues or have suggestions for improvements:
1. Document the issue clearly
2. Provide example code if applicable
3. Suggest a solution if possible

## 📄 License

These assignments are provided for educational purposes.

## 👨‍🏫 For Instructors

### Customization Options
- Adjust complexity requirements
- Add/remove features
- Modify test cases
- Change grading weights

### Assignment Sequencing
Recommended order:
1. Stack (1 week)
2. Queue (1 week)
3. Linked List (1-2 weeks)
4. Tree (2 weeks)
5. Trie (1 week)
6. Graph (2 weeks)

### Assessment Ideas
- Code reviews
- Complexity analysis questions
- Design discussions
- Extension projects
- Performance optimization challenges

---

## 📞 Support

For questions or issues with the assignments, refer to:
1. Individual assignment README files
2. Code comments and docstrings
3. Unit tests for expected behavior
4. Application demos for usage examples

---

**Happy Coding! 🎉**

*Last Updated: 2024*
