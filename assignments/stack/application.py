"""
Stack Applications Demo

This module demonstrates practical applications of stack data structure
including expression evaluation, parentheses checking, undo/redo functionality,
and function call simulation.

Author: Data Structure Course
Date: 2024
"""

from stack import ArrayStack, LinkedListStack, is_balanced_parentheses, evaluate_postfix, infix_to_postfix


class TextEditor:
    """
    Simple text editor that demonstrates undo/redo functionality using stacks.
    """
    
    def __init__(self):
        """Initialize the text editor with empty content and stacks."""
        self.content = ""
        self.undo_stack = ArrayStack()
        self.redo_stack = ArrayStack()
    
    def type_text(self, text):
        """
        Add text to the content.
        
        Args:
            text (str): Text to add
        """
        # Save current state for undo
        self.undo_stack.push(('type', self.content))
        
        # Clear redo stack when new action is performed
        self.redo_stack = ArrayStack()
        
        # Perform action
        self.content += text
        print(f"Typed: '{text}' -> Content: '{self.content}'")
    
    def delete_chars(self, count):
        """
        Delete characters from the end of content.
        
        Args:
            count (int): Number of characters to delete
        """
        if count > len(self.content):
            count = len(self.content)
        
        # Save current state for undo
        deleted_text = self.content[-count:] if count > 0 else ""
        self.undo_stack.push(('delete', self.content))
        
        # Clear redo stack
        self.redo_stack = ArrayStack()
        
        # Perform action
        self.content = self.content[:-count]
        print(f"Deleted {count} chars ('{deleted_text}') -> Content: '{self.content}'")
    
    def undo(self):
        """Undo the last action."""
        if self.undo_stack.is_empty():
            print("Nothing to undo")
            return
        
        # Save current state for redo
        self.redo_stack.push(('restore', self.content))
        
        # Restore previous state
        action, previous_content = self.undo_stack.pop()
        self.content = previous_content
        print(f"Undo -> Content: '{self.content}'")
    
    def redo(self):
        """Redo the last undone action."""
        if self.redo_stack.is_empty():
            print("Nothing to redo")
            return
        
        # Save current state for undo
        self.undo_stack.push(('restore', self.content))
        
        # Restore redo state
        action, redo_content = self.redo_stack.pop()
        self.content = redo_content
        print(f"Redo -> Content: '{self.content}'")
    
    def show_status(self):
        """Show current editor status."""
        print(f"Content: '{self.content}'")
        print(f"Can undo: {not self.undo_stack.is_empty()}")
        print(f"Can redo: {not self.redo_stack.is_empty()}")


class FunctionCallSimulator:
    """
    Simulates function call stack to demonstrate how recursion works.
    """
    
    def __init__(self):
        """Initialize the call stack."""
        self.call_stack = ArrayStack()
        self.call_count = 0
    
    def call_function(self, function_name, parameters):
        """
        Simulate calling a function.
        
        Args:
            function_name (str): Name of the function
            parameters (dict): Function parameters
        """
        self.call_count += 1
        frame = {
            'function': function_name,
            'parameters': parameters,
            'call_id': self.call_count,
            'local_vars': {}
        }
        
        self.call_stack.push(frame)
        print(f"→ Calling {function_name}({parameters}) [Call #{self.call_count}]")
        self.show_call_stack()
    
    def return_from_function(self, return_value=None):
        """
        Simulate returning from a function.
        
        Args:
            return_value: Value returned by the function
        """
        if self.call_stack.is_empty():
            print("No function to return from!")
            return
        
        frame = self.call_stack.pop()
        print(f"← Returning from {frame['function']} with value: {return_value}")
        self.show_call_stack()
    
    def show_call_stack(self):
        """Display the current call stack."""
        if self.call_stack.is_empty():
            print("Call stack: [empty]")
            return
        
        print("Call stack (top to bottom):")
        temp_stack = ArrayStack()
        
        # Pop all items to display them
        while not self.call_stack.is_empty():
            frame = self.call_stack.pop()
            temp_stack.push(frame)
        
        # Display and restore
        level = temp_stack.size()
        while not temp_stack.is_empty():
            frame = temp_stack.pop()
            indent = "  " * (level - temp_stack.size() - 1)
            print(f"{indent}└─ {frame['function']}({frame['parameters']}) [#{frame['call_id']}]")
            self.call_stack.push(frame)
        print()


def demo_basic_operations():
    """Demonstrate basic stack operations."""
    print("=== BASIC STACK OPERATIONS DEMO ===\n")
    
    # Array-based stack
    print("Array-based Stack:")
    array_stack = ArrayStack()
    
    # Push operations
    for item in [10, 20, 30, 40]:
        array_stack.push(item)
        print(f"Pushed {item}, stack: {array_stack}")
    
    # Peek operation
    print(f"Top element: {array_stack.peek()}")
    
    # Pop operations
    while not array_stack.is_empty():
        item = array_stack.pop()
        print(f"Popped {item}, stack: {array_stack}")
    
    print()
    
    # Linked list-based stack
    print("Linked List-based Stack:")
    ll_stack = LinkedListStack()
    
    for item in ['A', 'B', 'C', 'D']:
        ll_stack.push(item)
        print(f"Pushed {item}, stack: {ll_stack}")
    
    print(f"Stack size: {ll_stack.size()}")
    
    while not ll_stack.is_empty():
        item = ll_stack.pop()
        print(f"Popped {item}, stack: {ll_stack}")
    
    print("\n" + "="*50 + "\n")


def demo_parentheses_checking():
    """Demonstrate parentheses balancing."""
    print("=== PARENTHESES BALANCING DEMO ===\n")
    
    test_expressions = [
        "(())",
        "([{}])",
        "(((",
        "([)]",
        "{[()]}",
        "((()))",
        "([{}()])",
        "((())",
        "",
        "abc(def[ghi{jkl}mno]pqr)stu"
    ]
    
    for expr in test_expressions:
        result = is_balanced_parentheses(expr)
        status = "✓ Balanced" if result else "✗ Not balanced"
        print(f"'{expr}' -> {status}")
    
    print("\n" + "="*50 + "\n")


def demo_expression_evaluation():
    """Demonstrate expression evaluation."""
    print("=== EXPRESSION EVALUATION DEMO ===\n")
    
    # Postfix evaluation
    print("Postfix Expression Evaluation:")
    postfix_expressions = [
        "3 4 + 2 *",
        "15 7 1 1 + - / 3 * 2 1 1 + + -",
        "5 1 2 + 4 * + 3 -",
        "2 3 + 4 5 + *"
    ]
    
    for expr in postfix_expressions:
        try:
            result = evaluate_postfix(expr)
            print(f"'{expr}' = {result}")
        except Exception as e:
            print(f"'{expr}' -> Error: {e}")
    
    print()
    
    # Infix to postfix conversion
    print("Infix to Postfix Conversion:")
    infix_expressions = [
        "3 + 4 * 2",
        "( 3 + 4 ) * 2",
        "A + B * C",
        "( A + B ) * ( C - D )",
        "A * B + C / D"
    ]
    
    for expr in infix_expressions:
        try:
            postfix = infix_to_postfix(expr)
            print(f"'{expr}' -> '{postfix}'")
        except Exception as e:
            print(f"'{expr}' -> Error: {e}")
    
    print("\n" + "="*50 + "\n")


def demo_text_editor():
    """Demonstrate undo/redo functionality."""
    print("=== TEXT EDITOR UNDO/REDO DEMO ===\n")
    
    editor = TextEditor()
    
    # Simulate typing
    editor.type_text("Hello")
    editor.type_text(" World")
    editor.type_text("!")
    
    print()
    editor.show_status()
    print()
    
    # Delete some characters
    editor.delete_chars(1)  # Remove "!"
    editor.delete_chars(6)  # Remove " World"
    
    print()
    editor.show_status()
    print()
    
    # Undo operations
    print("Performing undo operations:")
    editor.undo()  # Restore " World"
    editor.undo()  # Restore "!"
    editor.undo()  # Restore to "Hello World"
    
    print()
    editor.show_status()
    print()
    
    # Redo operations
    print("Performing redo operations:")
    editor.redo()  # Remove " World"
    editor.redo()  # Remove "!"
    
    print()
    editor.show_status()
    
    print("\n" + "="*50 + "\n")


def demo_function_calls():
    """Demonstrate function call stack simulation."""
    print("=== FUNCTION CALL STACK DEMO ===\n")
    
    simulator = FunctionCallSimulator()
    
    # Simulate factorial calculation: factorial(3)
    print("Simulating factorial(3) calculation:\n")
    
    simulator.call_function("factorial", {"n": 3})
    simulator.call_function("factorial", {"n": 2})
    simulator.call_function("factorial", {"n": 1})
    
    # Base case reached, start returning
    simulator.return_from_function(1)  # factorial(1) returns 1
    simulator.return_from_function(2)  # factorial(2) returns 2 * 1 = 2
    simulator.return_from_function(6)  # factorial(3) returns 3 * 2 = 6
    
    print("Factorial calculation complete!")
    
    print("\n" + "="*50 + "\n")


def demo_stack_comparison():
    """Compare array-based vs linked list-based stacks."""
    print("=== STACK IMPLEMENTATION COMPARISON ===\n")
    
    import time
    
    # Test with larger dataset
    test_size = 10000
    
    # Array-based stack performance
    array_stack = ArrayStack()
    
    start_time = time.time()
    for i in range(test_size):
        array_stack.push(i)
    
    for i in range(test_size):
        array_stack.pop()
    
    array_time = time.time() - start_time
    
    # Linked list-based stack performance
    ll_stack = LinkedListStack()
    
    start_time = time.time()
    for i in range(test_size):
        ll_stack.push(i)
    
    for i in range(test_size):
        ll_stack.pop()
    
    ll_time = time.time() - start_time
    
    print(f"Performance test with {test_size} operations:")
    print(f"Array-based stack: {array_time:.6f} seconds")
    print(f"Linked list-based stack: {ll_time:.6f} seconds")
    
    if array_time < ll_time:
        print("Array-based stack is faster (better cache locality)")
    else:
        print("Linked list-based stack is faster")
    
    print("\nMemory characteristics:")
    print("Array-based: Better cache locality, occasional resize cost")
    print("Linked list-based: More memory per element, guaranteed O(1)")
    
    print("\n" + "="*50 + "\n")


def main():
    """Run all demonstrations."""
    print("STACK DATA STRUCTURE - COMPREHENSIVE DEMO")
    print("="*50)
    print()
    
    demo_basic_operations()
    demo_parentheses_checking()
    demo_expression_evaluation()
    demo_text_editor()
    demo_function_calls()
    demo_stack_comparison()
    
    print("All demonstrations completed!")


if __name__ == "__main__":
    main()