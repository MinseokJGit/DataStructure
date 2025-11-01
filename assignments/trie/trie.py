"""
Trie (Prefix Tree) Data Structure Implementation

This module provides complete implementations of trie structures:
Standard Trie, Frequency Trie, and utility functions for prefix-based operations.

Author: Data Structure Course
Date: 2024
"""

from collections import deque


class TrieNode:
    """
    Node class for trie.
    """
    
    def __init__(self):
        """
        Initialize a trie node.
        """
        self.children = {}  # Map from character to TrieNode
        self.is_end_of_word = False


class Trie:
    """
    Standard Trie (Prefix Tree) implementation.
    
    Efficient for prefix-based queries.
    All operations are O(m) where m is the length of the word/prefix.
    """
    
    def __init__(self):
        """Initialize an empty trie."""
        self.root = TrieNode()
        self._size = 0
    
    def insert(self, word):
        """
        Insert a word into the trie.
        
        Args:
            word (str): The word to insert
            
        Time Complexity: O(m) where m = len(word)
        """
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        if not node.is_end_of_word:
            node.is_end_of_word = True
            self._size += 1
    
    def search(self, word):
        """
        Search for an exact word in the trie.
        
        Args:
            word (str): The word to search for
            
        Returns:
            bool: True if word exists, False otherwise
            
        Time Complexity: O(m)
        """
        node = self.root
        
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        """
        Check if any word in the trie starts with the given prefix.
        
        Args:
            prefix (str): The prefix to check
            
        Returns:
            bool: True if prefix exists, False otherwise
            
        Time Complexity: O(m)
        """
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True
    
    def delete(self, word):
        """
        Delete a word from the trie.

        Args:
            word (str): The word to delete

        Returns:
            bool: True if word was deleted, False if word didn't exist

        Time Complexity: O(m)
        """
        # Track if word was found and deleted
        deleted = [False]

        def _delete_recursive(node, word, index):
            if index == len(word):
                # Reached end of word
                if not node.is_end_of_word:
                    return False  # Word doesn't exist

                node.is_end_of_word = False
                self._size -= 1
                deleted[0] = True

                # Return True if node has no children (can be deleted)
                return len(node.children) == 0

            char = word[index]
            if char not in node.children:
                return False  # Word doesn't exist

            child = node.children[char]
            should_delete_child = _delete_recursive(child, word, index + 1)

            # If recursive call returned False, word didn't exist
            if should_delete_child is False:
                return False

            # Child node can be deleted
            if should_delete_child:
                del node.children[char]
                # Return True if current node can also be deleted
                return len(node.children) == 0 and not node.is_end_of_word

            # Child node cannot be deleted (it has other children or is end of another word)
            return False

        _delete_recursive(self.root, word, 0)
        return deleted[0]
    
    def find_words_with_prefix(self, prefix):
        """
        Find all words that start with the given prefix.
        
        Args:
            prefix (str): The prefix to search for
            
        Returns:
            list: List of all words with the prefix
            
        Time Complexity: O(p + n*m) where p = len(prefix), n = number of words, m = avg word length
        """
        node = self.root
        
        # Navigate to the prefix node
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        # Collect all words from this node
        words = []
        self._collect_words(node, prefix, words)
        return words
    
    def _collect_words(self, node, current_word, words):
        """
        Helper method to collect all words from a node using DFS.
        
        Args:
            node (TrieNode): Current node
            current_word (str): Word formed so far
            words (list): List to collect words
        """
        if node.is_end_of_word:
            words.append(current_word)
        
        for char, child in sorted(node.children.items()):
            self._collect_words(child, current_word + char, words)
    
    def autocomplete(self, prefix, max_results=5):
        """
        Get autocomplete suggestions for a prefix.
        
        Args:
            prefix (str): The prefix to autocomplete
            max_results (int): Maximum number of suggestions
            
        Returns:
            list: List of suggested words
            
        Time Complexity: O(p + k) where p = len(prefix), k = max_results
        """
        node = self.root
        
        # Navigate to prefix
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        # BFS to find closest words
        results = []
        queue = deque([(node, prefix)])
        
        while queue and len(results) < max_results:
            current, word = queue.popleft()
            
            if current.is_end_of_word:
                results.append(word)
            
            for char, child in sorted(current.children.items()):
                queue.append((child, word + char))
        
        return results
    
    def get_all_words(self):
        """
        Get all words in the trie.
        
        Returns:
            list: List of all words
        """
        return self.find_words_with_prefix("")
    
    def size(self):
        """Get the number of words in the trie."""
        return self._size
    
    def is_empty(self):
        """Check if the trie is empty."""
        return self._size == 0
    
    def clear(self):
        """Clear all words from the trie."""
        self.root = TrieNode()
        self._size = 0
    
    def __len__(self):
        """Return the number of words in the trie."""
        return self._size
    
    def __contains__(self, word):
        """Check if word is in trie using 'in' operator."""
        return self.search(word)
    
    def __str__(self):
        """String representation of the trie."""
        words = self.get_all_words()
        return f"Trie({words[:10]}{'...' if len(words) > 10 else ''})"
    
    def __repr__(self):
        """Developer representation of the trie."""
        return f"Trie(size={self._size})"


class FrequencyTrieNode:
    """
    Node class for frequency trie.
    """
    
    def __init__(self):
        """Initialize a frequency trie node."""
        self.children = {}
        self.count = 0  # Number of times word was inserted


class FrequencyTrie:
    """
    Trie that tracks word frequencies.
    
    Useful for autocomplete with popularity ranking.
    """
    
    def __init__(self):
        """Initialize an empty frequency trie."""
        self.root = FrequencyTrieNode()
        self._size = 0
    
    def insert(self, word):
        """
        Insert a word and increment its frequency.
        
        Args:
            word (str): The word to insert
            
        Time Complexity: O(m)
        """
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = FrequencyTrieNode()
            node = node.children[char]
        
        if node.count == 0:
            self._size += 1
        node.count += 1
    
    def get_frequency(self, word):
        """
        Get the frequency of a word.
        
        Args:
            word (str): The word to query
            
        Returns:
            int: Frequency of the word (0 if not found)
            
        Time Complexity: O(m)
        """
        node = self.root
        
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        
        return node.count
    
    def top_k_with_prefix(self, prefix, k):
        """
        Get top k most frequent words with given prefix.
        
        Args:
            prefix (str): The prefix to search for
            k (int): Number of results to return
            
        Returns:
            list: Top k words sorted by frequency
            
        Time Complexity: O(p + n log n) where p = len(prefix), n = words with prefix
        """
        node = self.root
        
        # Navigate to prefix
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        # Collect all words with frequencies
        words = []
        self._collect_with_frequency(node, prefix, words)
        
        # Sort by frequency (descending) and return top k
        words.sort(key=lambda x: (-x[1], x[0]))  # Sort by freq desc, then alphabetically
        return [word for word, freq in words[:k]]
    
    def _collect_with_frequency(self, node, word, words):
        """Helper method to collect words with their frequencies."""
        if node.count > 0:
            words.append((word, node.count))
        
        for char, child in node.children.items():
            self._collect_with_frequency(child, word + char, words)
    
    def size(self):
        """Get the number of unique words in the trie."""
        return self._size
    
    def __len__(self):
        """Return the number of unique words in the trie."""
        return self._size


class WildcardTrie(Trie):
    """
    Trie with wildcard search support.
    
    Supports '.' as wildcard for any single character.
    """
    
    def search_with_wildcard(self, pattern):
        """
        Search for words matching a pattern with wildcards.
        
        Args:
            pattern (str): Pattern with '.' as wildcard
            
        Returns:
            list: All words matching the pattern
            
        Example:
            search_with_wildcard("c.t") matches "cat", "cot", "cut"
        """
        results = []
        self._search_wildcard_helper(self.root, pattern, 0, "", results)
        return results
    
    def _search_wildcard_helper(self, node, pattern, index, current, results):
        """Helper method for wildcard search."""
        if index == len(pattern):
            if node.is_end_of_word:
                results.append(current)
            return
        
        char = pattern[index]
        
        if char == '.':
            # Wildcard: try all children
            for ch, child in node.children.items():
                self._search_wildcard_helper(child, pattern, index + 1, current + ch, results)
        else:
            # Regular character
            if char in node.children:
                self._search_wildcard_helper(node.children[char], pattern, index + 1, current + char, results)


# Utility functions
def longest_common_prefix(words):
    """
    Find the longest common prefix of a list of words using trie.
    
    Args:
        words (list): List of words
        
    Returns:
        str: Longest common prefix
        
    Time Complexity: O(n*m) where n = number of words, m = avg length
    """
    if not words:
        return ""
    
    trie = Trie()
    
    # Insert all words
    for word in words:
        trie.insert(word)
    
    # Traverse until branching or end of word
    node = trie.root
    prefix = ""
    
    while len(node.children) == 1 and not node.is_end_of_word:
        char = next(iter(node.children))
        prefix += char
        node = node.children[char]
    
    return prefix


def word_break(s, word_dict):
    """
    Check if string can be segmented into dictionary words using trie.
    
    Args:
        s (str): String to segment
        word_dict (list): List of dictionary words
        
    Returns:
        bool: True if string can be segmented
        
    Example:
        word_break("leetcode", ["leet", "code"]) -> True
    """
    trie = Trie()
    for word in word_dict:
        trie.insert(word)
    
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and trie.search(s[j:i]):
                dp[i] = True
                break
    
    return dp[n]


def find_all_concatenated_words(words):
    """
    Find all words that are concatenations of other words.
    
    Args:
        words (list): List of words
        
    Returns:
        list: Words that are concatenations
        
    Example:
        find_all_concatenated_words(["cat", "cats", "dog", "catsdog"])
        -> ["cats", "catsdog"]
    """
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    result = []
    
    for word in words:
        # Check if word can be formed by other words
        n = len(word)
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(1, n + 1):
            for j in range(i):
                # Don't use the word itself
                if j == 0 and i == n:
                    continue
                
                if dp[j] and trie.search(word[j:i]):
                    dp[i] = True
                    break
        
        if dp[n]:
            result.append(word)
    
    return result


def replace_words(dictionary, sentence):
    """
    Replace words in sentence with their shortest root from dictionary.
    
    Args:
        dictionary (list): List of root words
        sentence (str): Sentence to process
        
    Returns:
        str: Sentence with words replaced by roots
        
    Example:
        replace_words(["cat", "bat", "rat"], "the cattle was rattled by the battery")
        -> "the cat was rat by the bat"
    """
    trie = Trie()
    for root in dictionary:
        trie.insert(root)
    
    def find_root(word):
        """Find shortest root for a word."""
        node = trie.root
        prefix = ""
        
        for char in word:
            if char not in node.children:
                return word
            
            prefix += char
            node = node.children[char]
            
            if node.is_end_of_word:
                return prefix
        
        return word
    
    words = sentence.split()
    return ' '.join(find_root(word) for word in words)
