"""
Unit Tests for Trie Data Structures

This module provides comprehensive unit tests for trie implementations
and utility functions.

Author: Data Structure Course
Date: 2024
"""

import unittest
from trie import (
    Trie, FrequencyTrie, WildcardTrie,
    longest_common_prefix, word_break, find_all_concatenated_words, replace_words
)


class TestTrie(unittest.TestCase):
    """Test cases for Trie implementation."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.trie = Trie()
    
    def test_initialization(self):
        """Test trie initialization."""
        self.assertTrue(self.trie.is_empty())
        self.assertEqual(self.trie.size(), 0)
        self.assertEqual(len(self.trie), 0)
    
    def test_insert_single_word(self):
        """Test inserting a single word."""
        self.trie.insert("cat")
        self.assertFalse(self.trie.is_empty())
        self.assertEqual(self.trie.size(), 1)
        self.assertTrue(self.trie.search("cat"))
    
    def test_insert_multiple_words(self):
        """Test inserting multiple words."""
        words = ["cat", "car", "card", "dog"]
        for word in words:
            self.trie.insert(word)
        
        self.assertEqual(self.trie.size(), 4)
        for word in words:
            self.assertTrue(self.trie.search(word))
    
    def test_insert_duplicate(self):
        """Test inserting duplicate words."""
        self.trie.insert("cat")
        self.trie.insert("cat")
        
        # Size should not increase for duplicates
        self.assertEqual(self.trie.size(), 1)
        self.assertTrue(self.trie.search("cat"))
    
    def test_search_existing(self):
        """Test searching for existing words."""
        self.trie.insert("cat")
        self.trie.insert("car")
        
        self.assertTrue(self.trie.search("cat"))
        self.assertTrue(self.trie.search("car"))
    
    def test_search_nonexistent(self):
        """Test searching for non-existent words."""
        self.trie.insert("cat")
        
        self.assertFalse(self.trie.search("ca"))
        self.assertFalse(self.trie.search("cats"))
        self.assertFalse(self.trie.search("dog"))
    
    def test_starts_with(self):
        """Test prefix search."""
        self.trie.insert("cat")
        self.trie.insert("car")
        self.trie.insert("card")
        
        self.assertTrue(self.trie.starts_with("ca"))
        self.assertTrue(self.trie.starts_with("car"))
        self.assertTrue(self.trie.starts_with("card"))
        self.assertFalse(self.trie.starts_with("do"))
    
    def test_delete_existing(self):
        """Test deleting existing words."""
        self.trie.insert("cat")
        self.trie.insert("car")
        self.trie.insert("card")
        
        self.assertTrue(self.trie.delete("car"))
        self.assertFalse(self.trie.search("car"))
        self.assertTrue(self.trie.search("cat"))
        self.assertTrue(self.trie.search("card"))
        self.assertEqual(self.trie.size(), 2)
    
    def test_delete_nonexistent(self):
        """Test deleting non-existent words."""
        self.trie.insert("cat")
        
        self.assertFalse(self.trie.delete("dog"))
        self.assertEqual(self.trie.size(), 1)
    
    def test_delete_prefix(self):
        """Test that deleting doesn't affect words with same prefix."""
        self.trie.insert("car")
        self.trie.insert("card")
        
        self.trie.delete("car")
        self.assertTrue(self.trie.search("card"))
        self.assertTrue(self.trie.starts_with("car"))
    
    def test_find_words_with_prefix(self):
        """Test finding all words with prefix."""
        words = ["cat", "car", "card", "care", "dog"]
        for word in words:
            self.trie.insert(word)
        
        car_words = self.trie.find_words_with_prefix("car")
        self.assertEqual(set(car_words), {"car", "card", "care"})
        
        ca_words = self.trie.find_words_with_prefix("ca")
        self.assertEqual(set(ca_words), {"cat", "car", "card", "care"})
        
        do_words = self.trie.find_words_with_prefix("do")
        self.assertEqual(do_words, ["dog"])
    
    def test_find_words_with_nonexistent_prefix(self):
        """Test finding words with non-existent prefix."""
        self.trie.insert("cat")
        
        result = self.trie.find_words_with_prefix("dog")
        self.assertEqual(result, [])
    
    def test_autocomplete(self):
        """Test autocomplete functionality."""
        words = ["cat", "car", "card", "care", "careful", "dog"]
        for word in words:
            self.trie.insert(word)
        
        suggestions = self.trie.autocomplete("car", 3)
        self.assertEqual(len(suggestions), 3)
        self.assertTrue(all(s.startswith("car") for s in suggestions))
    
    def test_get_all_words(self):
        """Test getting all words."""
        words = ["cat", "car", "dog"]
        for word in words:
            self.trie.insert(word)
        
        all_words = self.trie.get_all_words()
        self.assertEqual(set(all_words), set(words))
    
    def test_clear(self):
        """Test clearing the trie."""
        self.trie.insert("cat")
        self.trie.insert("dog")
        
        self.trie.clear()
        self.assertTrue(self.trie.is_empty())
        self.assertEqual(self.trie.size(), 0)
    
    def test_contains_operator(self):
        """Test 'in' operator."""
        self.trie.insert("cat")
        
        self.assertTrue("cat" in self.trie)
        self.assertFalse("dog" in self.trie)
    
    def test_empty_string(self):
        """Test with empty string."""
        self.trie.insert("")
        self.assertTrue(self.trie.search(""))
        self.assertEqual(self.trie.size(), 1)


class TestFrequencyTrie(unittest.TestCase):
    """Test cases for FrequencyTrie implementation."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.freq_trie = FrequencyTrie()
    
    def test_initialization(self):
        """Test frequency trie initialization."""
        self.assertEqual(self.freq_trie.size(), 0)
    
    def test_insert_and_frequency(self):
        """Test insertion and frequency tracking."""
        self.freq_trie.insert("cat")
        self.assertEqual(self.freq_trie.get_frequency("cat"), 1)
        
        self.freq_trie.insert("cat")
        self.assertEqual(self.freq_trie.get_frequency("cat"), 2)
        
        self.freq_trie.insert("cat")
        self.assertEqual(self.freq_trie.get_frequency("cat"), 3)
    
    def test_get_frequency_nonexistent(self):
        """Test getting frequency of non-existent word."""
        self.assertEqual(self.freq_trie.get_frequency("dog"), 0)
    
    def test_top_k_with_prefix(self):
        """Test getting top k words with prefix."""
        # Insert words with different frequencies
        for _ in range(5):
            self.freq_trie.insert("apple")
        for _ in range(3):
            self.freq_trie.insert("app")
        for _ in range(4):
            self.freq_trie.insert("apply")
        for _ in range(2):
            self.freq_trie.insert("application")
        
        top_2 = self.freq_trie.top_k_with_prefix("app", 2)
        self.assertEqual(len(top_2), 2)
        self.assertEqual(top_2[0], "apple")  # Highest frequency
        self.assertEqual(top_2[1], "apply")
    
    def test_top_k_empty_prefix(self):
        """Test top k with empty prefix."""
        self.freq_trie.insert("cat")
        self.freq_trie.insert("dog")
        
        top_all = self.freq_trie.top_k_with_prefix("", 10)
        self.assertEqual(len(top_all), 2)
    
    def test_size_with_duplicates(self):
        """Test that size counts unique words."""
        self.freq_trie.insert("cat")
        self.freq_trie.insert("cat")
        self.freq_trie.insert("dog")
        
        self.assertEqual(self.freq_trie.size(), 2)


class TestWildcardTrie(unittest.TestCase):
    """Test cases for WildcardTrie implementation."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.wildcard_trie = WildcardTrie()
    
    def test_search_with_wildcard_single(self):
        """Test wildcard search with single wildcard."""
        words = ["cat", "car", "cot", "cut"]
        for word in words:
            self.wildcard_trie.insert(word)
        
        matches = self.wildcard_trie.search_with_wildcard("c.t")
        self.assertEqual(set(matches), {"cat", "cot", "cut"})
    
    def test_search_with_wildcard_multiple(self):
        """Test wildcard search with multiple wildcards."""
        words = ["cat", "car", "cot"]
        for word in words:
            self.wildcard_trie.insert(word)
        
        matches = self.wildcard_trie.search_with_wildcard("c..")
        self.assertEqual(set(matches), {"cat", "car", "cot"})
    
    def test_search_with_wildcard_no_match(self):
        """Test wildcard search with no matches."""
        self.wildcard_trie.insert("cat")
        
        matches = self.wildcard_trie.search_with_wildcard("d.g")
        self.assertEqual(matches, [])
    
    def test_search_without_wildcard(self):
        """Test that regular search still works."""
        self.wildcard_trie.insert("cat")
        
        matches = self.wildcard_trie.search_with_wildcard("cat")
        self.assertEqual(matches, ["cat"])


class TestUtilityFunctions(unittest.TestCase):
    """Test cases for utility functions."""
    
    def test_longest_common_prefix_exists(self):
        """Test longest common prefix when it exists."""
        words = ["flower", "flow", "flight"]
        lcp = longest_common_prefix(words)
        self.assertEqual(lcp, "fl")
    
    def test_longest_common_prefix_none(self):
        """Test longest common prefix when none exists."""
        words = ["dog", "racecar", "car"]
        lcp = longest_common_prefix(words)
        self.assertEqual(lcp, "")
    
    def test_longest_common_prefix_empty_list(self):
        """Test longest common prefix with empty list."""
        lcp = longest_common_prefix([])
        self.assertEqual(lcp, "")
    
    def test_longest_common_prefix_single_word(self):
        """Test longest common prefix with single word."""
        lcp = longest_common_prefix(["hello"])
        self.assertEqual(lcp, "hello")
    
    def test_word_break_true(self):
        """Test word break when segmentation is possible."""
        self.assertTrue(word_break("leetcode", ["leet", "code"]))
        self.assertTrue(word_break("applepenapple", ["apple", "pen"]))
    
    def test_word_break_false(self):
        """Test word break when segmentation is not possible."""
        self.assertFalse(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    
    def test_word_break_empty_string(self):
        """Test word break with empty string."""
        self.assertTrue(word_break("", ["cat", "dog"]))
    
    def test_find_concatenated_words(self):
        """Test finding concatenated words."""
        words = ["cat", "cats", "dog", "catsdog", "s"]
        result = find_all_concatenated_words(words)
        self.assertIn("cats", result)
        self.assertIn("catsdog", result)
    
    def test_find_concatenated_words_none(self):
        """Test when no concatenated words exist."""
        words = ["cat", "dog", "bird"]
        result = find_all_concatenated_words(words)
        self.assertEqual(result, [])
    
    def test_replace_words(self):
        """Test replacing words with roots."""
        dictionary = ["cat", "bat", "rat"]
        sentence = "the cattle was rattled by the battery"
        result = replace_words(dictionary, sentence)
        self.assertEqual(result, "the cat was rat by the bat")
    
    def test_replace_words_no_roots(self):
        """Test replace words when no roots match."""
        dictionary = ["a", "b"]
        sentence = "the dog"
        result = replace_words(dictionary, sentence)
        self.assertEqual(result, "the dog")


class TestEdgeCases(unittest.TestCase):
    """Test edge cases for trie structures."""
    
    def test_single_character_words(self):
        """Test with single character words."""
        trie = Trie()
        trie.insert("a")
        trie.insert("b")
        trie.insert("c")
        
        self.assertTrue(trie.search("a"))
        self.assertTrue(trie.search("b"))
        self.assertEqual(trie.size(), 3)
    
    def test_very_long_word(self):
        """Test with very long word."""
        trie = Trie()
        long_word = "a" * 1000
        
        trie.insert(long_word)
        self.assertTrue(trie.search(long_word))
    
    def test_special_characters(self):
        """Test with special characters."""
        trie = Trie()
        trie.insert("hello-world")
        trie.insert("test_case")
        trie.insert("foo.bar")
        
        self.assertTrue(trie.search("hello-world"))
        self.assertTrue(trie.search("test_case"))
        self.assertTrue(trie.search("foo.bar"))
    
    def test_case_sensitivity(self):
        """Test that trie is case-sensitive."""
        trie = Trie()
        trie.insert("Cat")
        trie.insert("cat")
        
        self.assertTrue(trie.search("Cat"))
        self.assertTrue(trie.search("cat"))
        self.assertEqual(trie.size(), 2)
    
    def test_numbers_in_words(self):
        """Test with numbers in words."""
        trie = Trie()
        trie.insert("test123")
        trie.insert("abc456")
        
        self.assertTrue(trie.search("test123"))
        self.assertTrue(trie.search("abc456"))
    
    def test_prefix_is_word(self):
        """Test when prefix is itself a word."""
        trie = Trie()
        trie.insert("car")
        trie.insert("card")
        
        self.assertTrue(trie.search("car"))
        self.assertTrue(trie.search("card"))
        self.assertTrue(trie.starts_with("car"))
    
    def test_large_number_of_words(self):
        """Test with large number of words."""
        trie = Trie()
        
        # Insert 1000 words
        for i in range(1000):
            trie.insert(f"word{i}")
        
        self.assertEqual(trie.size(), 1000)
        self.assertTrue(trie.search("word500"))
        self.assertFalse(trie.search("word1000"))
    
    def test_overlapping_prefixes(self):
        """Test with many overlapping prefixes."""
        trie = Trie()
        words = ["a", "ab", "abc", "abcd", "abcde"]
        
        for word in words:
            trie.insert(word)
        
        for word in words:
            self.assertTrue(trie.search(word))
        
        self.assertEqual(trie.size(), 5)


def run_tests():
    """Run all tests."""
    unittest.main(verbosity=2)


if __name__ == '__main__':
    run_tests()
