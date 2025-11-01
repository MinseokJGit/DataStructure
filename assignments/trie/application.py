"""
Trie Applications Demo

This module demonstrates practical applications of trie data structures
including autocomplete, spell checker, word search, and prefix queries.

Author: Data Structure Course
Date: 2024
"""

from trie import (
    Trie, FrequencyTrie, WildcardTrie,
    longest_common_prefix, word_break, find_all_concatenated_words, replace_words
)
import time


class AutocompleteSystem:
    """
    Autocomplete system using frequency trie.
    Tracks search history and provides ranked suggestions.
    """
    
    def __init__(self, sentences, times):
        """
        Initialize autocomplete system.
        
        Args:
            sentences (list): Initial sentences
            times (list): Frequency of each sentence
        """
        self.trie = FrequencyTrie()
        self.current_input = ""
        
        # Load initial data
        for sentence, count in zip(sentences, times):
            for _ in range(count):
                self.trie.insert(sentence)
    
    def input(self, char):
        """
        Process one character input.
        
        Args:
            char (str): Input character ('#' to end sentence)
            
        Returns:
            list: Top 3 suggestions
        """
        if char == '#':
            # End of sentence, save it
            if self.current_input:
                self.trie.insert(self.current_input)
            self.current_input = ""
            return []
        
        self.current_input += char
        
        # Return top 3 suggestions
        return self.trie.top_k_with_prefix(self.current_input, 3)


class SpellChecker:
    """
    Spell checker using trie.
    Provides spell checking and correction suggestions.
    """
    
    def __init__(self, dictionary):
        """
        Initialize spell checker.
        
        Args:
            dictionary (list): List of correct words
        """
        self.trie = Trie()
        for word in dictionary:
            self.trie.insert(word.lower())
    
    def is_correct(self, word):
        """
        Check if word is spelled correctly.
        
        Args:
            word (str): Word to check
            
        Returns:
            bool: True if correct, False otherwise
        """
        return self.trie.search(word.lower())
    
    def suggest_corrections(self, word, max_suggestions=5):
        """
        Suggest corrections for misspelled word.
        Uses edit distance of 1 (insertion, deletion, substitution).
        
        Args:
            word (str): Misspelled word
            max_suggestions (int): Maximum suggestions to return
            
        Returns:
            list: Suggested corrections
        """
        word = word.lower()
        suggestions = set()
        
        # Deletions
        for i in range(len(word)):
            candidate = word[:i] + word[i+1:]
            if self.trie.search(candidate):
                suggestions.add(candidate)
        
        # Insertions
        for i in range(len(word) + 1):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                candidate = word[:i] + c + word[i:]
                if self.trie.search(candidate):
                    suggestions.add(candidate)
        
        # Substitutions
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c != word[i]:
                    candidate = word[:i] + c + word[i+1:]
                    if self.trie.search(candidate):
                        suggestions.add(candidate)
        
        return list(suggestions)[:max_suggestions]


class ContactList:
    """
    Contact list with prefix search using trie.
    """
    
    def __init__(self):
        """Initialize empty contact list."""
        self.trie = Trie()
        self.contacts = {}  # name -> contact info
    
    def add_contact(self, name, phone, email):
        """
        Add a contact.
        
        Args:
            name (str): Contact name
            phone (str): Phone number
            email (str): Email address
        """
        name_lower = name.lower()
        self.trie.insert(name_lower)
        self.contacts[name_lower] = {
            'name': name,
            'phone': phone,
            'email': email
        }
        print(f"Added contact: {name}")
    
    def search_by_prefix(self, prefix):
        """
        Search contacts by name prefix.
        
        Args:
            prefix (str): Name prefix
            
        Returns:
            list: Matching contacts
        """
        matches = self.trie.find_words_with_prefix(prefix.lower())
        return [self.contacts[name] for name in matches]
    
    def show_all_contacts(self):
        """Display all contacts."""
        all_names = self.trie.get_all_words()
        print(f"\nAll Contacts ({len(all_names)}):")
        for name in sorted(all_names):
            contact = self.contacts[name]
            print(f"  {contact['name']}: {contact['phone']}, {contact['email']}")


class WordSearchGame:
    """
    Word search game using trie for efficient word lookup.
    """
    
    def __init__(self, board, words):
        """
        Initialize word search game.
        
        Args:
            board (list): 2D grid of characters
            words (list): Words to find
        """
        self.board = board
        self.trie = Trie()
        
        for word in words:
            self.trie.insert(word)
    
    def find_words(self):
        """
        Find all words from the word list in the board.
        
        Returns:
            list: Found words
        """
        rows, cols = len(self.board), len(self.board[0])
        found = set()
        
        def dfs(r, c, node, path):
            if node.is_end_of_word:
                found.add(path)
            
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            
            char = self.board[r][c]
            if char not in node.children:
                return
            
            # Mark as visited
            self.board[r][c] = '#'
            
            # Explore all 4 directions
            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                dfs(r + dr, c + dc, node.children[char], path + char)
            
            # Restore
            self.board[r][c] = char
        
        # Try starting from each cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, self.trie.root, "")
        
        return list(found)


def demo_basic_operations():
    """Demonstrate basic trie operations."""
    print("=== BASIC TRIE OPERATIONS ===\n")
    
    trie = Trie()
    
    # Insert words
    words = ["cat", "car", "card", "care", "careful", "dog", "dodge"]
    print(f"Inserting words: {words}")
    for word in words:
        trie.insert(word)
    
    print(f"Trie size: {trie.size()}")
    print(f"All words: {trie.get_all_words()}")
    
    # Search
    print(f"\nSearch 'car': {trie.search('car')}")
    print(f"Search 'ca': {trie.search('ca')}")
    print(f"Search 'cars': {trie.search('cars')}")
    
    # Prefix search
    print(f"\nStarts with 'car': {trie.starts_with('car')}")
    print(f"Starts with 'do': {trie.starts_with('do')}")
    print(f"Starts with 'bat': {trie.starts_with('bat')}")
    
    # Find words with prefix
    print(f"\nWords with prefix 'car': {trie.find_words_with_prefix('car')}")
    print(f"Words with prefix 'do': {trie.find_words_with_prefix('do')}")
    
    # Delete
    print(f"\nDeleting 'car': {trie.delete('car')}")
    print(f"Words with prefix 'car': {trie.find_words_with_prefix('car')}")
    print(f"Search 'car': {trie.search('car')}")
    print(f"Search 'card': {trie.search('card')}")
    
    print("\n" + "="*50 + "\n")


def demo_autocomplete():
    """Demonstrate autocomplete system."""
    print("=== AUTOCOMPLETE SYSTEM ===\n")
    
    sentences = [
        "i love you",
        "island",
        "i love leetcode",
        "ironman",
        "i love coding"
    ]
    times = [5, 3, 2, 2, 1]
    
    system = AutocompleteSystem(sentences, times)
    
    print("Initial sentences with frequencies:")
    for sentence, count in zip(sentences, times):
        print(f"  '{sentence}': {count}")
    
    print("\nTyping 'i':")
    suggestions = system.input('i')
    print(f"  Suggestions: {suggestions}")
    
    print("\nTyping ' ':")
    suggestions = system.input(' ')
    print(f"  Suggestions: {suggestions}")
    
    print("\nTyping 'l':")
    suggestions = system.input('l')
    print(f"  Suggestions: {suggestions}")
    
    print("\nTyping 'o':")
    suggestions = system.input('o')
    print(f"  Suggestions: {suggestions}")
    
    print("\nEnding sentence with '#':")
    system.input('#')
    
    print("\n" + "="*50 + "\n")


def demo_spell_checker():
    """Demonstrate spell checker."""
    print("=== SPELL CHECKER ===\n")
    
    dictionary = [
        "cat", "car", "card", "care", "careful",
        "dog", "dodge", "door", "done",
        "hello", "help", "hero", "house"
    ]
    
    checker = SpellChecker(dictionary)
    
    print(f"Dictionary: {dictionary}\n")
    
    # Check correct words
    test_words = ["cat", "car", "cra", "dgo", "helo", "xyz"]
    
    print("Spell checking:")
    for word in test_words:
        is_correct = checker.is_correct(word)
        status = "✓ Correct" if is_correct else "✗ Incorrect"
        print(f"  '{word}': {status}")
        
        if not is_correct:
            suggestions = checker.suggest_corrections(word)
            if suggestions:
                print(f"    Suggestions: {suggestions}")
    
    print("\n" + "="*50 + "\n")


def demo_frequency_trie():
    """Demonstrate frequency trie."""
    print("=== FREQUENCY TRIE ===\n")
    
    freq_trie = FrequencyTrie()
    
    # Insert words with different frequencies
    words_with_freq = [
        ("apple", 5),
        ("app", 3),
        ("application", 2),
        ("apply", 4),
        ("banana", 1),
        ("band", 2)
    ]
    
    print("Inserting words with frequencies:")
    for word, freq in words_with_freq:
        for _ in range(freq):
            freq_trie.insert(word)
        print(f"  '{word}': {freq}")
    
    # Query frequencies
    print(f"\nFrequency of 'apple': {freq_trie.get_frequency('apple')}")
    print(f"Frequency of 'app': {freq_trie.get_frequency('app')}")
    print(f"Frequency of 'xyz': {freq_trie.get_frequency('xyz')}")
    
    # Top k with prefix
    print(f"\nTop 3 words with prefix 'app':")
    top_words = freq_trie.top_k_with_prefix('app', 3)
    for i, word in enumerate(top_words, 1):
        print(f"  {i}. {word} (freq: {freq_trie.get_frequency(word)})")
    
    print("\n" + "="*50 + "\n")


def demo_wildcard_search():
    """Demonstrate wildcard search."""
    print("=== WILDCARD SEARCH ===\n")
    
    trie = WildcardTrie()
    
    words = ["cat", "car", "card", "cart", "dog", "dot", "cot"]
    print(f"Words: {words}\n")
    
    for word in words:
        trie.insert(word)
    
    # Wildcard searches
    patterns = ["c.r", "c..", "..t", "c..d"]
    
    print("Wildcard searches:")
    for pattern in patterns:
        matches = trie.search_with_wildcard(pattern)
        print(f"  Pattern '{pattern}': {matches}")
    
    print("\n" + "="*50 + "\n")


def demo_contact_list():
    """Demonstrate contact list."""
    print("=== CONTACT LIST ===\n")
    
    contacts = ContactList()
    
    # Add contacts
    print("Adding contacts:")
    contacts.add_contact("Alice Smith", "555-0101", "alice@email.com")
    contacts.add_contact("Bob Johnson", "555-0102", "bob@email.com")
    contacts.add_contact("Alice Brown", "555-0103", "alice.b@email.com")
    contacts.add_contact("Charlie Davis", "555-0104", "charlie@email.com")
    contacts.add_contact("David Wilson", "555-0105", "david@email.com")
    
    # Search by prefix
    print(f"\nSearching for 'ali':")
    matches = contacts.search_by_prefix("ali")
    for contact in matches:
        print(f"  {contact['name']}: {contact['phone']}")
    
    print(f"\nSearching for 'd':")
    matches = contacts.search_by_prefix("d")
    for contact in matches:
        print(f"  {contact['name']}: {contact['phone']}")
    
    contacts.show_all_contacts()
    
    print("\n" + "="*50 + "\n")


def demo_utility_functions():
    """Demonstrate utility functions."""
    print("=== UTILITY FUNCTIONS ===\n")
    
    # Longest common prefix
    print("Longest Common Prefix:")
    words1 = ["flower", "flow", "flight"]
    lcp1 = longest_common_prefix(words1)
    print(f"  {words1} -> '{lcp1}'")
    
    words2 = ["dog", "racecar", "car"]
    lcp2 = longest_common_prefix(words2)
    print(f"  {words2} -> '{lcp2}'")
    
    # Word break
    print(f"\nWord Break:")
    s1 = "leetcode"
    dict1 = ["leet", "code"]
    result1 = word_break(s1, dict1)
    print(f"  '{s1}' with {dict1} -> {result1}")
    
    s2 = "applepenapple"
    dict2 = ["apple", "pen"]
    result2 = word_break(s2, dict2)
    print(f"  '{s2}' with {dict2} -> {result2}")
    
    # Concatenated words
    print(f"\nConcatenated Words:")
    words3 = ["cat", "cats", "dog", "catsdog", "catsdogcats"]
    concat = find_all_concatenated_words(words3)
    print(f"  {words3}")
    print(f"  Concatenated: {concat}")
    
    # Replace words
    print(f"\nReplace Words:")
    dictionary = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    result = replace_words(dictionary, sentence)
    print(f"  Dictionary: {dictionary}")
    print(f"  Original: '{sentence}'")
    print(f"  Replaced: '{result}'")
    
    print("\n" + "="*50 + "\n")


def demo_word_search_game():
    """Demonstrate word search game."""
    print("=== WORD SEARCH GAME ===\n")
    
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    
    words = ["oath", "pea", "eat", "rain", "oat", "hike"]
    
    print("Board:")
    for row in board:
        print("  " + " ".join(row))
    
    print(f"\nWords to find: {words}")
    
    game = WordSearchGame(board, words)
    found = game.find_words()
    
    print(f"\nFound words: {found}")
    
    print("\n" + "="*50 + "\n")


def demo_performance():
    """Demonstrate performance characteristics."""
    print("=== PERFORMANCE COMPARISON ===\n")
    
    # Generate test data
    words = [f"word{i}" for i in range(10000)]
    
    # Trie insertion
    trie = Trie()
    start = time.time()
    for word in words:
        trie.insert(word)
    trie_insert_time = time.time() - start
    
    # Trie search
    start = time.time()
    for word in words[:1000]:
        trie.search(word)
    trie_search_time = time.time() - start
    
    # List search (for comparison)
    word_list = words[:]
    start = time.time()
    for word in words[:1000]:
        word in word_list
    list_search_time = time.time() - start
    
    print(f"Operations on {len(words)} words:\n")
    print(f"{'Operation':<20} {'Trie':<15} {'List':<15}")
    print("-" * 50)
    print(f"{'Insert all':<20} {trie_insert_time:<15.6f} {'N/A':<15}")
    print(f"{'Search 1000':<20} {trie_search_time:<15.6f} {list_search_time:<15.6f}")
    
    print("\nKey observations:")
    print("- Trie: O(m) search where m = word length")
    print("- List: O(n*m) search where n = number of words")
    print(f"- Speedup: {list_search_time/trie_search_time:.1f}x faster")
    
    print("\n" + "="*50 + "\n")


def main():
    """Run all demonstrations."""
    print("TRIE DATA STRUCTURE - COMPREHENSIVE DEMO")
    print("="*50)
    print()
    
    demo_basic_operations()
    demo_autocomplete()
    demo_spell_checker()
    demo_frequency_trie()
    demo_wildcard_search()
    demo_contact_list()
    demo_utility_functions()
    demo_word_search_game()
    demo_performance()
    
    print("All demonstrations completed!")


if __name__ == "__main__":
    main()
