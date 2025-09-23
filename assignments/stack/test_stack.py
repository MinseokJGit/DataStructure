"""
Unit tests for stack implementation.

This module provides comprehensive tests for both ArrayStack and LinkedListStack
implementations to ensure correctness of all operations.

Author: Data Structure Course  
Date: 2024
"""

from stack import ArrayStack, LinkedListStack, is_balanced_parentheses, evaluate_postfix, infix_to_postfix


def test_array_stack_basic_operations():
    """Test basic operations of ArrayStack."""
    stack = ArrayStack()
    
    # Test empty stack
    assert stack.is_empty() == True
    assert stack.size() == 0
    
    # Test push and size
    stack.push(1)
    assert stack.size() == 1
    assert stack.is_empty() == False
    
    stack.push(2)
    stack.push(3)
    assert stack.size() == 3
    
    # Test peek
    assert stack.peek() == 3
    assert stack.size() == 3  # peek shouldn't remove item
    
    # Test pop
    assert stack.pop() == 3
    assert stack.size() == 2
    assert stack.peek() == 2
    
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.is_empty() == True


def test_linked_list_stack_basic_operations():
    """Test basic operations of LinkedListStack."""
    stack = LinkedListStack()
    
    # Test empty stack
    assert stack.is_empty() == True
    assert stack.size() == 0
    
    # Test push and size
    stack.push('a')
    assert stack.size() == 1
    assert stack.is_empty() == False
    
    stack.push('b')
    stack.push('c')
    assert stack.size() == 3
    
    # Test peek
    assert stack.peek() == 'c'
    assert stack.size() == 3  # peek shouldn't remove item
    
    # Test pop
    assert stack.pop() == 'c'
    assert stack.size() == 2
    assert stack.peek() == 'b'
    
    assert stack.pop() == 'b'
    assert stack.pop() == 'a'
    assert stack.is_empty() == True


def test_stack_exceptions():
    """Test that stacks raise appropriate exceptions."""
    array_stack = ArrayStack()
    ll_stack = LinkedListStack()
    
    # Test pop from empty stack
    try:
        array_stack.pop()
        assert False, "Should raise IndexError"
    except IndexError:
        pass
    
    try:
        ll_stack.pop()
        assert False, "Should raise IndexError"
    except IndexError:
        pass
    
    # Test peek from empty stack
    try:
        array_stack.peek()
        assert False, "Should raise IndexError"
    except IndexError:
        pass
    
    try:
        ll_stack.peek()
        assert False, "Should raise IndexError"
    except IndexError:
        pass


def test_balanced_parentheses():
    """Test parentheses balancing function."""
    # Balanced expressions
    assert is_balanced_parentheses("()") == True
    assert is_balanced_parentheses("([{}])") == True
    assert is_balanced_parentheses("((()))") == True
    assert is_balanced_parentheses("") == True
    assert is_balanced_parentheses("a(b[c{d}e]f)g") == True
    
    # Unbalanced expressions
    assert is_balanced_parentheses("(") == False
    assert is_balanced_parentheses(")") == False
    assert is_balanced_parentheses("([)]") == False
    assert is_balanced_parentheses("((())") == False
    assert is_balanced_parentheses("())") == False


def test_postfix_evaluation():
    """Test postfix expression evaluation."""
    assert evaluate_postfix("3 4 +") == 7.0
    assert evaluate_postfix("3 4 + 2 *") == 14.0
    assert evaluate_postfix("15 7 1 1 + - / 3 * 2 1 1 + + -") == 5.0
    assert evaluate_postfix("5") == 5.0
    assert evaluate_postfix("2 3 + 4 5 + *") == 45.0


def test_infix_to_postfix():
    """Test infix to postfix conversion."""
    assert infix_to_postfix("3 + 4") == "3 4 +"
    assert infix_to_postfix("3 + 4 * 2") == "3 4 2 * +"
    assert infix_to_postfix("( 3 + 4 ) * 2") == "3 4 + 2 *"
    assert infix_to_postfix("A * B + C") == "A B * C +"


def run_all_tests():
    """Run all tests manually (for environments without pytest)."""
    print("Running stack tests...")
    
    try:
        test_array_stack_basic_operations()
        print("✓ ArrayStack basic operations test passed")
        
        test_linked_list_stack_basic_operations()
        print("✓ LinkedListStack basic operations test passed")
        
        test_stack_exceptions()
        print("✓ Stack exceptions test passed")
        
        test_balanced_parentheses()
        print("✓ Balanced parentheses test passed")
        
        test_postfix_evaluation()
        print("✓ Postfix evaluation test passed")
        
        test_infix_to_postfix()
        print("✓ Infix to postfix test passed")
        
        print("\nAll tests passed! ✓")
        
    except Exception as e:
        print(f"Test failed: {e}")
        raise


if __name__ == "__main__":
    run_all_tests()