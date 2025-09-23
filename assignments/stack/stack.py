"""
Stack Data Structure Implementation

This module provides a complete implementation of a stack data structure
using both array-based and linked list-based approaches.

Author: Data Structure Course
Date: 2024
"""


class ArrayStack:
    """
    Array-based stack implementation using Python list.
    
    Provides O(1) amortized time complexity for all operations.
    """
    
    def __init__(self):
        """Initialize an empty stack."""
        self._data = []
    
    def push(self, item):
        """
        Add an item to the top of the stack.
        
        Args:
            item: The item to be added to the stack
            
        Time Complexity: O(1) amortized
        """
        self._data.append(item)
    
    def pop(self):
        """
        Remove and return the top item from the stack.
        
        Returns:
            The top item from the stack
            
        Raises:
            IndexError: If the stack is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()
    
    def peek(self):
        """
        Return the top item without removing it.
        
        Returns:
            The top item from the stack
            
        Raises:
            IndexError: If the stack is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._data[-1]
    
    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if stack is empty, False otherwise
            
        Time Complexity: O(1)
        """
        return len(self._data) == 0
    
    def size(self):
        """
        Get the number of items in the stack.
        
        Returns:
            int: Number of items in the stack
            
        Time Complexity: O(1)
        """
        return len(self._data)
    
    def __str__(self):
        """String representation of the stack."""
        return f"ArrayStack({self._data})"
    
    def __repr__(self):
        """Developer representation of the stack."""
        return f"ArrayStack({self._data})"


class Node:
    """
    Node class for linked list implementation.
    """
    
    def __init__(self, data, next_node=None):
        """
        Initialize a node.
        
        Args:
            data: The data to store in the node
            next_node: Reference to the next node (default: None)
        """
        self.data = data
        self.next = next_node


class LinkedListStack:
    """
    Linked list-based stack implementation.
    
    Provides guaranteed O(1) time complexity for all operations.
    """
    
    def __init__(self):
        """Initialize an empty stack."""
        self._head = None
        self._size = 0
    
    def push(self, item):
        """
        Add an item to the top of the stack.
        
        Args:
            item: The item to be added to the stack
            
        Time Complexity: O(1)
        """
        new_node = Node(item, self._head)
        self._head = new_node
        self._size += 1
    
    def pop(self):
        """
        Remove and return the top item from the stack.
        
        Returns:
            The top item from the stack
            
        Raises:
            IndexError: If the stack is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        
        data = self._head.data
        self._head = self._head.next
        self._size -= 1
        return data
    
    def peek(self):
        """
        Return the top item without removing it.
        
        Returns:
            The top item from the stack
            
        Raises:
            IndexError: If the stack is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._head.data
    
    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if stack is empty, False otherwise
            
        Time Complexity: O(1)
        """
        return self._head is None
    
    def size(self):
        """
        Get the number of items in the stack.
        
        Returns:
            int: Number of items in the stack
            
        Time Complexity: O(1)
        """
        return self._size
    
    def __str__(self):
        """String representation of the stack."""
        items = []
        current = self._head
        while current:
            items.append(current.data)
            current = current.next
        return f"LinkedListStack({items})"
    
    def __repr__(self):
        """Developer representation of the stack."""
        return self.__str__()


# Utility functions for stack operations
def is_balanced_parentheses(expression):
    """
    Check if parentheses in an expression are balanced.
    
    Args:
        expression (str): The expression to check
        
    Returns:
        bool: True if balanced, False otherwise
        
    Examples:
        >>> is_balanced_parentheses("(())")
        True
        >>> is_balanced_parentheses("([)]")
        False
    """
    stack = ArrayStack()
    opening = "([{"
    closing = ")]}"
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty():
                return False
            if stack.pop() != pairs[char]:
                return False
    
    return stack.is_empty()


def evaluate_postfix(expression):
    """
    Evaluate a postfix expression.
    
    Args:
        expression (str): Space-separated postfix expression
        
    Returns:
        float: Result of the evaluation
        
    Examples:
        >>> evaluate_postfix("3 4 + 2 *")
        14.0
        >>> evaluate_postfix("15 7 1 1 + − / 3 × 2 1 1 + + −")
        5.0
    """
    stack = ArrayStack()
    tokens = expression.split()
    
    for token in tokens:
        if token in ['+', '-', '*', '/']:
            if stack.size() < 2:
                raise ValueError("Invalid postfix expression")
            
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                if operand2 == 0:
                    raise ValueError("Division by zero")
                result = operand1 / operand2
            
            stack.push(result)
        else:
            try:
                number = float(token)
                stack.push(number)
            except ValueError:
                raise ValueError(f"Invalid token: {token}")
    
    if stack.size() != 1:
        raise ValueError("Invalid postfix expression")
    
    return stack.pop()


def infix_to_postfix(expression):
    """
    Convert infix expression to postfix notation.
    
    Args:
        expression (str): Infix expression with spaces between tokens
        
    Returns:
        str: Postfix expression
        
    Examples:
        >>> infix_to_postfix("3 + 4 * 2")
        "3 4 2 * +"
        >>> infix_to_postfix("( 3 + 4 ) * 2")
        "3 4 + 2 *"
    """
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = ArrayStack()
    output = []
    tokens = expression.split()
    
    for token in tokens:
        if token.replace('.', '').replace('-', '').isdigit() or token.isalpha():
            # Number (including negative numbers and decimals) or variable
            output.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            if not stack.is_empty():
                stack.pop()  # Remove the '('
        elif token in precedence:
            while (not stack.is_empty() and 
                   stack.peek() != '(' and 
                   stack.peek() in precedence and
                   precedence[stack.peek()] >= precedence[token]):
                output.append(stack.pop())
            stack.push(token)
    
    while not stack.is_empty():
        output.append(stack.pop())
    
    return ' '.join(output)


# Default stack implementation (using ArrayStack for simplicity)
Stack = ArrayStack