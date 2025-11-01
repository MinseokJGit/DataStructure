"""
Linked List Applications Demo

This module demonstrates practical applications of linked list data structures
including browser history, music playlist, LRU cache, and various algorithms.

Author: Data Structure Course
Date: 2024
"""

from linked_list import (
    SinglyLinkedList, DoublyLinkedList, CircularLinkedList,
    Node, DNode, merge_sorted_lists, remove_duplicates, find_kth_from_end
)
import time


class BrowserHistory:
    """
    Browser history implementation using doubly linked list.
    Supports back and forward navigation.
    """
    
    def __init__(self, homepage):
        """
        Initialize browser with homepage.
        
        Args:
            homepage (str): Initial homepage URL
        """
        self.current = DNode(homepage)
        self.current.prev = None
        self.current.next = None
    
    def visit(self, url):
        """
        Visit a new URL.
        
        Args:
            url (str): URL to visit
        """
        new_page = DNode(url)
        new_page.prev = self.current
        self.current.next = new_page
        self.current = new_page
        print(f"Visited: {url}")
    
    def back(self, steps=1):
        """
        Go back in history.
        
        Args:
            steps (int): Number of steps to go back
            
        Returns:
            str: Current URL after going back
        """
        for _ in range(steps):
            if self.current.prev:
                self.current = self.current.prev
            else:
                break
        
        print(f"Back to: {self.current.data}")
        return self.current.data
    
    def forward(self, steps=1):
        """
        Go forward in history.
        
        Args:
            steps (int): Number of steps to go forward
            
        Returns:
            str: Current URL after going forward
        """
        for _ in range(steps):
            if self.current.next:
                self.current = self.current.next
            else:
                break
        
        print(f"Forward to: {self.current.data}")
        return self.current.data
    
    def current_url(self):
        """Get current URL."""
        return self.current.data


class MusicPlaylist:
    """
    Music playlist using circular linked list.
    Supports continuous playback and repeat functionality.
    """
    
    def __init__(self):
        """Initialize empty playlist."""
        self.playlist = CircularLinkedList()
        self.current = None
    
    def add_song(self, song):
        """
        Add a song to the playlist.
        
        Args:
            song (str): Song name
        """
        self.playlist.append(song)
        if not self.current:
            self.current = self.playlist.head
        print(f"Added: {song}")
    
    def play_next(self):
        """
        Play next song in playlist.
        
        Returns:
            str: Next song name
        """
        if not self.current:
            print("Playlist is empty")
            return None
        
        self.current = self.current.next
        print(f"Now playing: {self.current.data}")
        return self.current.data
    
    def play_previous(self):
        """
        Play previous song (requires traversal in circular list).
        
        Returns:
            str: Previous song name
        """
        if not self.current or not self.playlist.head:
            print("Playlist is empty")
            return None
        
        # Find previous node
        prev = self.current
        while prev.next != self.current:
            prev = prev.next
        
        self.current = prev
        print(f"Now playing: {self.current.data}")
        return self.current.data
    
    def current_song(self):
        """Get current song."""
        return self.current.data if self.current else None
    
    def show_playlist(self):
        """Display all songs in playlist."""
        songs = self.playlist.to_list()
        print(f"Playlist ({len(songs)} songs): {songs}")


class LRUCache:
    """
    LRU (Least Recently Used) Cache using doubly linked list and hash map.
    Provides O(1) get and put operations.
    """
    
    def __init__(self, capacity):
        """
        Initialize LRU cache with capacity.
        
        Args:
            capacity (int): Maximum number of items
        """
        self.capacity = capacity
        self.cache = {}  # key -> DNode
        
        # Sentinel nodes
        self.head = DNode(None)
        self.tail = DNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node):
        """Remove a node from the linked list."""
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add_to_head(self, node):
        """Add a node right after head (most recently used)."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def get(self, key):
        """
        Get value for a key.
        
        Args:
            key: Cache key
            
        Returns:
            Value if found, -1 otherwise
        """
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            print(f"Cache hit: {key} -> {node.data[1]}")
            return node.data[1]
        
        print(f"Cache miss: {key}")
        return -1
    
    def put(self, key, value):
        """
        Put a key-value pair in cache.
        
        Args:
            key: Cache key
            value: Cache value
        """
        if key in self.cache:
            self._remove(self.cache[key])
        
        node = DNode((key, value))
        self._add_to_head(node)
        self.cache[key] = node
        
        if len(self.cache) > self.capacity:
            # Remove least recently used (before tail)
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.data[0]]
            print(f"Evicted: {lru.data[0]}")
        
        print(f"Put: {key} -> {value}")
    
    def show_cache(self):
        """Display current cache contents."""
        items = []
        current = self.head.next
        while current != self.tail:
            items.append(f"{current.data[0]}:{current.data[1]}")
            current = current.next
        print(f"Cache (MRU -> LRU): {' -> '.join(items)}")


class UndoRedoManager:
    """
    Undo/Redo functionality using doubly linked list.
    """
    
    def __init__(self):
        """Initialize undo/redo manager."""
        self.current = None
    
    def do_action(self, action):
        """
        Perform an action.
        
        Args:
            action (str): Action description
        """
        new_node = DNode(action)
        
        if self.current:
            new_node.prev = self.current
            self.current.next = new_node
        
        self.current = new_node
        print(f"Action: {action}")
    
    def undo(self):
        """
        Undo last action.
        
        Returns:
            str: Undone action, or None if nothing to undo
        """
        if not self.current:
            print("Nothing to undo")
            return None
        
        action = self.current.data
        
        if self.current.prev:
            self.current = self.current.prev
            print(f"Undo: {action}")
        else:
            print("Reached beginning of history")
        
        return action
    
    def redo(self):
        """
        Redo last undone action.
        
        Returns:
            str: Redone action, or None if nothing to redo
        """
        if not self.current or not self.current.next:
            print("Nothing to redo")
            return None
        
        self.current = self.current.next
        action = self.current.data
        print(f"Redo: {action}")
        return action
    
    def current_state(self):
        """Get current action."""
        return self.current.data if self.current else "Initial state"


def demo_basic_operations():
    """Demonstrate basic linked list operations."""
    print("=== BASIC LINKED LIST OPERATIONS ===\n")
    
    # Singly linked list
    print("Singly Linked List:")
    sll = SinglyLinkedList()
    
    for item in [10, 20, 30, 40]:
        sll.append(item)
        print(f"Appended {item}: {sll}")
    
    sll.prepend(5)
    print(f"Prepended 5: {sll}")
    
    sll.insert_at(2, 15)
    print(f"Inserted 15 at index 2: {sll}")
    
    print(f"Element at index 3: {sll.get(3)}")
    print(f"Middle element: {sll.find_middle()}")
    
    sll.delete_first()
    print(f"Deleted first: {sll}")
    
    sll.delete_last()
    print(f"Deleted last: {sll}")
    
    sll.delete_value(20)
    print(f"Deleted value 20: {sll}")
    
    print()
    
    # Doubly linked list
    print("Doubly Linked List:")
    dll = DoublyLinkedList()
    
    for item in ['A', 'B', 'C', 'D']:
        dll.append(item)
    
    print(f"Forward: {dll.to_list()}")
    print(f"Backward: {dll.to_list_reverse()}")
    
    dll.reverse()
    print(f"After reverse: {dll.to_list()}")
    
    print()
    
    # Circular linked list
    print("Circular Linked List:")
    cll = CircularLinkedList()
    
    for item in [1, 2, 3, 4]:
        cll.append(item)
    
    print(f"Circular list: {cll}")
    print(f"Size: {cll.size()}")
    
    print("\n" + "="*50 + "\n")


def demo_browser_history():
    """Demonstrate browser history."""
    print("=== BROWSER HISTORY DEMO ===\n")
    
    browser = BrowserHistory("google.com")
    print(f"Starting at: {browser.current_url()}\n")
    
    browser.visit("youtube.com")
    browser.visit("github.com")
    browser.visit("stackoverflow.com")
    
    print()
    browser.back(2)
    browser.forward(1)
    browser.visit("reddit.com")
    
    print(f"\nCurrent page: {browser.current_url()}")
    
    print("\n" + "="*50 + "\n")


def demo_music_playlist():
    """Demonstrate music playlist."""
    print("=== MUSIC PLAYLIST DEMO ===\n")
    
    playlist = MusicPlaylist()
    
    songs = ["Song A", "Song B", "Song C", "Song D", "Song E"]
    for song in songs:
        playlist.add_song(song)
    
    print()
    playlist.show_playlist()
    
    print(f"\nCurrent: {playlist.current_song()}")
    
    print("\nPlaying through playlist:")
    for _ in range(7):  # Play more than playlist size to show circular
        playlist.play_next()
    
    print("\nGoing back:")
    for _ in range(3):
        playlist.play_previous()
    
    print("\n" + "="*50 + "\n")


def demo_lru_cache():
    """Demonstrate LRU cache."""
    print("=== LRU CACHE DEMO ===\n")
    
    cache = LRUCache(3)
    
    print("Adding items to cache (capacity=3):\n")
    cache.put(1, "One")
    cache.put(2, "Two")
    cache.put(3, "Three")
    
    print()
    cache.show_cache()
    
    print("\nAccessing item 1:")
    cache.get(1)
    cache.show_cache()
    
    print("\nAdding item 4 (will evict LRU):")
    cache.put(4, "Four")
    cache.show_cache()
    
    print("\nTrying to access evicted item 2:")
    cache.get(2)
    
    print("\n" + "="*50 + "\n")


def demo_undo_redo():
    """Demonstrate undo/redo functionality."""
    print("=== UNDO/REDO DEMO ===\n")
    
    manager = UndoRedoManager()
    
    print("Performing actions:")
    manager.do_action("Type 'Hello'")
    manager.do_action("Type ' World'")
    manager.do_action("Delete 'World'")
    manager.do_action("Type ' Python'")
    
    print(f"\nCurrent state: {manager.current_state()}")
    
    print("\nUndo operations:")
    manager.undo()
    manager.undo()
    
    print(f"\nCurrent state: {manager.current_state()}")
    
    print("\nRedo operations:")
    manager.redo()
    
    print(f"\nCurrent state: {manager.current_state()}")
    
    print("\n" + "="*50 + "\n")


def demo_reverse_list():
    """Demonstrate list reversal."""
    print("=== LIST REVERSAL DEMO ===\n")
    
    sll = SinglyLinkedList()
    for i in range(1, 6):
        sll.append(i)
    
    print(f"Original list: {sll}")
    
    sll.reverse()
    print(f"Reversed list: {sll}")
    
    print()
    
    dll = DoublyLinkedList()
    for char in ['A', 'B', 'C', 'D', 'E']:
        dll.append(char)
    
    print(f"Original doubly linked list: {dll}")
    
    dll.reverse()
    print(f"Reversed doubly linked list: {dll}")
    
    print("\n" + "="*50 + "\n")


def demo_merge_sorted_lists():
    """Demonstrate merging sorted lists."""
    print("=== MERGE SORTED LISTS DEMO ===\n")
    
    list1 = SinglyLinkedList()
    for item in [1, 3, 5, 7]:
        list1.append(item)
    
    list2 = SinglyLinkedList()
    for item in [2, 4, 6, 8]:
        list2.append(item)
    
    print(f"List 1: {list1}")
    print(f"List 2: {list2}")
    
    merged = merge_sorted_lists(list1, list2)
    print(f"Merged: {merged}")
    
    print("\n" + "="*50 + "\n")


def demo_remove_duplicates():
    """Demonstrate removing duplicates."""
    print("=== REMOVE DUPLICATES DEMO ===\n")
    
    sll = SinglyLinkedList()
    for item in [1, 2, 3, 2, 4, 1, 5, 3]:
        sll.append(item)
    
    print(f"Original list: {sll}")
    
    remove_duplicates(sll)
    print(f"After removing duplicates: {sll}")
    
    print("\n" + "="*50 + "\n")


def demo_find_kth_from_end():
    """Demonstrate finding k-th element from end."""
    print("=== FIND K-TH FROM END DEMO ===\n")
    
    sll = SinglyLinkedList()
    for i in range(1, 11):
        sll.append(i)
    
    print(f"List: {sll}")
    
    for k in [1, 3, 5, 10]:
        result = find_kth_from_end(sll, k)
        print(f"{k}-th element from end: {result}")
    
    print("\n" + "="*50 + "\n")


def demo_cycle_detection():
    """Demonstrate cycle detection."""
    print("=== CYCLE DETECTION DEMO ===\n")
    
    # List without cycle
    sll1 = SinglyLinkedList()
    for i in range(1, 6):
        sll1.append(i)
    
    print(f"List 1: {sll1}")
    print(f"Has cycle: {sll1.has_cycle()}")
    
    # List with cycle (manually create)
    sll2 = SinglyLinkedList()
    for i in range(1, 6):
        sll2.append(i)
    
    # Create cycle: last node points to node at index 2
    current = sll2.head
    node_at_2 = None
    index = 0
    
    while current.next:
        if index == 2:
            node_at_2 = current
        current = current.next
        index += 1
    
    # Create cycle
    current.next = node_at_2
    
    print(f"\nList 2 (with cycle):")
    print(f"Has cycle: {sll2.has_cycle()}")
    
    print("\n" + "="*50 + "\n")


def demo_performance_comparison():
    """Compare performance of different list types."""
    print("=== PERFORMANCE COMPARISON ===\n")
    
    test_size = 1000
    
    # Singly linked list
    sll = SinglyLinkedList()
    start = time.time()
    for i in range(test_size):
        sll.append(i)
    sll_append_time = time.time() - start
    
    start = time.time()
    for i in range(test_size):
        sll.get(i)
    sll_access_time = time.time() - start
    
    # Doubly linked list
    dll = DoublyLinkedList()
    start = time.time()
    for i in range(test_size):
        dll.append(i)
    dll_append_time = time.time() - start
    
    start = time.time()
    for i in range(test_size):
        dll.get(i)
    dll_access_time = time.time() - start
    
    # Python list (for comparison)
    py_list = []
    start = time.time()
    for i in range(test_size):
        py_list.append(i)
    py_append_time = time.time() - start
    
    start = time.time()
    for i in range(test_size):
        _ = py_list[i]
    py_access_time = time.time() - start
    
    print(f"Operations on {test_size} elements:\n")
    print(f"{'Structure':<20} {'Append (s)':<15} {'Access (s)':<15}")
    print("-" * 50)
    print(f"{'Singly Linked':<20} {sll_append_time:<15.6f} {sll_access_time:<15.6f}")
    print(f"{'Doubly Linked':<20} {dll_append_time:<15.6f} {dll_access_time:<15.6f}")
    print(f"{'Python List':<20} {py_append_time:<15.6f} {py_access_time:<15.6f}")
    
    print("\nKey observations:")
    print("- Linked lists: O(1) append, O(n) access")
    print("- Python list: O(1) amortized append, O(1) access")
    print("- Doubly linked: Faster access from end (bidirectional)")
    
    print("\n" + "="*50 + "\n")


def demo_iteration():
    """Demonstrate iteration over linked lists."""
    print("=== ITERATION DEMO ===\n")
    
    sll = SinglyLinkedList()
    for i in range(1, 6):
        sll.append(i)
    
    print("Iterating over singly linked list:")
    for item in sll:
        print(f"  {item}", end="")
    print()
    
    print("\nUsing list comprehension:")
    squared = [x**2 for x in sll]
    print(f"  Squared: {squared}")
    
    print("\nFiltering even numbers:")
    evens = [x for x in sll if x % 2 == 0]
    print(f"  Evens: {evens}")
    
    print("\n" + "="*50 + "\n")


def main():
    """Run all demonstrations."""
    print("LINKED LIST DATA STRUCTURE - COMPREHENSIVE DEMO")
    print("="*50)
    print()
    
    demo_basic_operations()
    demo_browser_history()
    demo_music_playlist()
    demo_lru_cache()
    demo_undo_redo()
    demo_reverse_list()
    demo_merge_sorted_lists()
    demo_remove_duplicates()
    demo_find_kth_from_end()
    demo_cycle_detection()
    demo_iteration()
    demo_performance_comparison()
    
    print("All demonstrations completed!")


if __name__ == "__main__":
    main()
