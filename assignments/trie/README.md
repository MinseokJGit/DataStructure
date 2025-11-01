# Trie (Prefix Tree) Assignment

This assignment contains complete implementations of trie data structures and their applications.

## Files Overview

### 1. `trie.py` - Core Implementation
Contains multiple trie implementations:
- **Trie**: Standard prefix tree with insert, search, delete, prefix queries
- **FrequencyTrie**: Tracks word frequencies for ranked autocomplete
- **WildcardTrie**: Supports wildcard pattern matching with '.'
- **Utility functions**: Longest common prefix, word break, concatenated words, replace words

### 2. `application.py` - Practical Applications
Demonstrates real-world use cases of tries:
- **Basic Operations**: Insert, search, delete, prefix queries
- **Autocomplete System**: Google-style autocomplete with frequency ranking
- **Spell Checker**: Spell checking with correction suggestions
- **Frequency Trie**: Track and rank word popularity
- **Wildcard Search**: Pattern matching with wildcards
- **Contact List**: Prefix-based contact search
- **Utility Functions**: LCP, word break, concatenated words
- **Word Search Game**: Find words in 2D grid
- **Performance Comparison**: Trie vs list search

### 3. `test_trie.py` - Unit Tests
Comprehensive test suite covering:
- Basic trie operations (insert, search, delete)
- Prefix queries and autocomplete
- Frequency tracking
- Wildcard pattern matching
- Utility functions
- Edge cases (empty string, long words, special characters)

## Key Concepts Demonstrated

### Trie Structure

**Visual Example:**
```
Words: ["cat", "car", "card", "dog"]

Trie structure:
         root
        /    \
       c      d
       |      |
       a      o
      / \     |
     t*  r*   g*
         |
         d*

* = end of word
```

**Node Structure:**
```python
class TrieNode:
    def __init__(self):
        self.children = {}  # char -> TrieNode
        self.is_end_of_word = False
```

### Operations Complexity

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Insert | O(m) | O(m) worst case |
| Search | O(m) | O(1) |
| Delete | O(m) | O(1) |
| Prefix Search | O(p) | O(1) |
| Find Words with Prefix | O(p + n*k) | O(n*k) |
| Autocomplete | O(p + k) | O(k) |

Where:
- m = length of word
- p = length of prefix
- n = number of words with prefix
- k = number of results

### Key Advantages

**vs Hash Table:**
- ✓ Prefix queries in O(p) time
- ✓ Autocomplete functionality
- ✓ Lexicographic ordering
- ✓ Space efficient for shared prefixes

**vs Binary Search Tree:**
- ✓ O(m) search independent of dataset size
- ✓ Natural prefix support
- ✓ No rebalancing needed

## Running the Code

### Run the comprehensive demo:
```bash
python application.py
```

### Run the unit tests:
```bash
python test_trie.py
```

### Example Usage:

#### Basic Trie:
```python
from trie import Trie

trie = Trie()

# Insert words
trie.insert("cat")
trie.insert("car")
trie.insert("card")

# Search
print(trie.search("car"))  # True
print(trie.search("ca"))   # False (not marked as word)

# Prefix search
print(trie.starts_with("car"))  # True
print(trie.find_words_with_prefix("car"))  # ['car', 'card']

# Autocomplete
print(trie.autocomplete("ca", 3))  # ['car', 'card', 'cat']

# Delete
trie.delete("car")
print(trie.search("car"))   # False
print(trie.search("card"))  # True (still exists)
```

#### Frequency Trie:
```python
from trie import FrequencyTrie

freq_trie = FrequencyTrie()

# Insert with frequencies
for _ in range(5):
    freq_trie.insert("apple")
for _ in range(3):
    freq_trie.insert("app")

# Get frequency
print(freq_trie.get_frequency("apple"))  # 5

# Top k with prefix
print(freq_trie.top_k_with_prefix("app", 2))  # ['apple', 'app']
```

#### Wildcard Search:
```python
from trie import WildcardTrie

trie = WildcardTrie()
trie.insert("cat")
trie.insert("car")
trie.insert("cot")

# Wildcard search
print(trie.search_with_wildcard("c.t"))  # ['cat', 'cot']
print(trie.search_with_wildcard("c.."))  # ['cat', 'car', 'cot']
```

## Assignment Instructions for Students

When adapting this for student assignments:

1. **Hide Core Functions**: Remove implementations of key methods
2. **Provide Template**: Give students the class structure with empty method bodies
3. **Include Tests**: Provide the test file for verification
4. **Progressive Difficulty**: 
   - Start with insert and search
   - Then implement prefix queries
   - Add delete operation
   - Advanced: Frequency tracking, wildcards

### Student Implementation Template:

#### Basic Trie Template:
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self._size = 0
    
    def insert(self, word):
        # TODO: Insert word into trie
        # 1. Start at root
        # 2. For each character:
        #    - If child doesn't exist, create it
        #    - Move to child
        # 3. Mark last node as end of word
        # 4. Update size if new word
        pass
    
    def search(self, word):
        # TODO: Search for exact word
        # 1. Start at root
        # 2. For each character:
        #    - If child doesn't exist, return False
        #    - Move to child
        # 3. Return whether last node is end of word
        pass
    
    def starts_with(self, prefix):
        # TODO: Check if any word starts with prefix
        # Similar to search but don't check is_end_of_word
        pass
    
    def delete(self, word):
        # TODO: Delete word from trie
        # Use recursive helper function
        # Handle three cases:
        #   1. Word doesn't exist
        #   2. Word is prefix of another word
        #   3. Word shares prefix with other words
        pass
```

## Learning Objectives

By completing this assignment, students will:
1. Understand tree-based string storage
2. Implement trie with insert, search, delete operations
3. Master prefix-based queries
4. Apply tries to solve real-world problems
5. Analyze time and space complexity trade-offs
6. Understand when to use tries vs other data structures
7. Implement advanced features (frequency tracking, wildcards)

## Common Pitfalls for Students

1. **Forgetting end marker**: Not marking end of word, causing search to fail
2. **Delete complexity**: Not handling all cases in deletion
3. **Memory management**: Creating unnecessary nodes
4. **Prefix vs word**: Confusing prefix existence with word existence
5. **Case sensitivity**: Not considering case in comparisons
6. **Empty string**: Not handling empty string edge case
7. **Shared prefixes**: Incorrectly deleting shared prefix nodes

## Key Algorithms

### 1. Insert
```python
def insert(self, word):
    node = self.root
    
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    
    node.is_end_of_word = True
```

### 2. Search
```python
def search(self, word):
    node = self.root
    
    for char in word:
        if char not in node.children:
            return False
        node = node.children[char]
    
    return node.is_end_of_word
```

### 3. Delete (Recursive)
```python
def delete(self, word):
    def _delete_recursive(node, word, index):
        if index == len(word):
            if not node.is_end_of_word:
                return False
            
            node.is_end_of_word = False
            return len(node.children) == 0
        
        char = word[index]
        if char not in node.children:
            return False
        
        should_delete = _delete_recursive(
            node.children[char], word, index + 1
        )
        
        if should_delete:
            del node.children[char]
            return len(node.children) == 0 and not node.is_end_of_word
        
        return False
    
    return _delete_recursive(self.root, word, 0)
```

### 4. Find Words with Prefix (DFS)
```python
def find_words_with_prefix(self, prefix):
    node = self.root
    
    # Navigate to prefix
    for char in prefix:
        if char not in node.children:
            return []
        node = node.children[char]
    
    # Collect all words
    words = []
    
    def dfs(node, current):
        if node.is_end_of_word:
            words.append(current)
        
        for char, child in node.children.items():
            dfs(child, current + char)
    
    dfs(node, prefix)
    return words
```

## Real-World Applications

### 1. Autocomplete
- **Use**: Search engines, IDEs, mobile keyboards
- **Why Trie**: Fast prefix matching, ranked suggestions
- **Example**: Google search suggestions

### 2. Spell Checker
- **Use**: Word processors, text editors
- **Why Trie**: Quick dictionary lookup, correction suggestions
- **Example**: Microsoft Word, Grammarly

### 3. IP Routing
- **Use**: Network routers
- **Why Trie**: Longest prefix matching for routing tables
- **Example**: Internet routing protocols

### 4. Contact Search
- **Use**: Phone apps, email clients
- **Why Trie**: Fast prefix-based name search
- **Example**: iPhone contacts

### 5. Word Games
- **Use**: Scrabble, Boggle, crossword solvers
- **Why Trie**: Efficient word validation and search
- **Example**: Word game apps

### 6. Text Prediction
- **Use**: Predictive text, T9 input
- **Why Trie**: Fast word completion
- **Example**: Mobile phone keyboards

## Comparison with Other Structures

### Trie vs Hash Table

| Feature | Trie | Hash Table |
|---------|------|------------|
| Search | O(m) | O(1) average |
| Prefix queries | O(p) | O(n) |
| Autocomplete | Native | Requires iteration |
| Space | O(ALPHABET * N * M) | O(N * M) |
| Ordering | Lexicographic | None |

### Trie vs BST

| Feature | Trie | BST |
|---------|------|-----|
| Search | O(m) | O(log n) |
| Insert | O(m) | O(log n) |
| Prefix queries | O(p) | O(log n + k) |
| Space | Higher | Lower |
| Balance | Not needed | May need rebalancing |

### When to Use Trie

**Use Trie when:**
- ✓ Need prefix-based queries
- ✓ Implementing autocomplete
- ✓ Many words share common prefixes
- ✓ Need lexicographic ordering
- ✓ Alphabet size is reasonable

**Don't use Trie when:**
- ✗ Only need exact match (use hash table)
- ✗ No prefix queries needed
- ✗ Memory is very constrained
- ✗ Alphabet size is huge

## Memory Optimization

### Standard Trie
```python
# Each node: dict + bool ≈ 100+ bytes
# For "cat", "car", "card": 6 nodes ≈ 600 bytes
```

### Compressed Trie (Radix Tree)
```python
# Merge single-child chains
# "test", "testing" → 3 nodes instead of 9
# 67% space reduction
```

### Array-based Trie
```python
# For lowercase a-z only
class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # Fixed size
        self.is_end = False
```

## Testing Your Implementation

Run the tests to verify your implementation:
```bash
python test_trie.py
```

Expected output:
```
test_insert_single_word (__main__.TestTrie) ... ok
test_search_existing (__main__.TestTrie) ... ok
test_delete_existing (__main__.TestTrie) ... ok
...
----------------------------------------------------------------------
Ran 50 tests in 0.XXXs

OK
```

## Debugging Tips

1. **Visualize**: Draw the trie structure on paper
2. **Print traversal**: Print characters as you traverse
3. **Check end markers**: Verify is_end_of_word is set correctly
4. **Test prefixes**: Ensure prefix search works independently
5. **Trace deletion**: Step through delete logic carefully
6. **Use small examples**: Test with 2-3 words first
7. **Verify children**: Check that children dict is updated correctly

## Grading Rubric (for Instructors)

| Component | Points | Criteria |
|-----------|--------|----------|
| Insert | 15 | Correct implementation |
| Search | 15 | Exact word search |
| Prefix Search | 15 | starts_with and find_words |
| Delete | 20 | All cases handled correctly |
| Autocomplete | 10 | Limited results |
| Frequency Trie (bonus) | 10 | Track and rank by frequency |
| Code Quality | 10 | Documentation, style |
| Testing | 5 | All tests pass |
| **Total** | **100** | |

## Advanced Topics (Extensions)

1. **Compressed Trie (Radix Tree)**: Merge single-child chains
2. **Ternary Search Tree**: Space-efficient alternative
3. **Suffix Trie**: Store all suffixes for pattern matching
4. **AC Automaton**: Multiple pattern matching
5. **Persistent Trie**: Version control for tries
6. **Concurrent Trie**: Thread-safe implementation

## Common Interview Questions

1. Implement Trie (insert, search, starts_with)
2. Word Search II (find words in 2D grid)
3. Replace Words (replace with shortest root)
4. Word Break (segment string into dictionary words)
5. Longest Word in Dictionary
6. Design Add and Search Words Data Structure (with wildcards)
7. Concatenated Words
8. Implement Magic Dictionary
9. Maximum XOR of Two Numbers (using binary trie)
10. Design Search Autocomplete System

## Tips for Success

1. **Understand the structure**: Draw tries for small examples
2. **Master recursion**: Delete operation is naturally recursive
3. **Test incrementally**: Test each method as you implement
4. **Handle edge cases**: Empty string, single character, duplicates
5. **Think about prefixes**: Core concept of tries
6. **Use helper methods**: Separate recursive logic
7. **Optimize later**: Get it working first, then optimize
8. **Practice problems**: LeetCode trie problems

## Additional Resources

- **Visualization**: [VisuAlgo - Trie](https://visualgo.net/en/trie)
- **Practice**: LeetCode trie tag problems
- **Reading**: "Introduction to Algorithms" (CLRS) - String Matching
- **Video**: MIT OpenCourseWare - Tries lecture

Good luck with your implementation!
