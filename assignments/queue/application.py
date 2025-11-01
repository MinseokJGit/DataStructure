"""
Queue Applications Demo

This module demonstrates practical applications of queue data structures
including task scheduling, breadth-first search, printer queue simulation,
and producer-consumer patterns.

Author: Data Structure Course
Date: 2024
"""

from queue import (
    ArrayQueue, LinkedListQueue, CircularQueue, Deque,
    hot_potato, is_palindrome, generate_binary_numbers
)
import time
import random


class Task:
    """Represents a task with priority and description."""
    
    def __init__(self, task_id, description, priority=0):
        """
        Initialize a task.
        
        Args:
            task_id: Unique identifier for the task
            description: Task description
            priority: Task priority (higher = more important)
        """
        self.task_id = task_id
        self.description = description
        self.priority = priority
        self.timestamp = time.time()
    
    def __str__(self):
        return f"Task#{self.task_id}: {self.description} (priority={self.priority})"
    
    def __repr__(self):
        return self.__str__()


class TaskScheduler:
    """
    Simple task scheduler using a queue (FIFO scheduling).
    """
    
    def __init__(self):
        """Initialize the task scheduler."""
        self.task_queue = LinkedListQueue()
        self.completed_tasks = []
    
    def add_task(self, task):
        """
        Add a task to the scheduler.
        
        Args:
            task (Task): Task to be added
        """
        self.task_queue.enqueue(task)
        print(f"Added: {task}")
    
    def process_next_task(self):
        """Process the next task in the queue."""
        if self.task_queue.is_empty():
            print("No tasks to process")
            return None
        
        task = self.task_queue.dequeue()
        print(f"Processing: {task}")
        
        # Simulate task processing
        time.sleep(0.1)
        
        self.completed_tasks.append(task)
        print(f"Completed: {task}")
        return task
    
    def process_all_tasks(self):
        """Process all tasks in the queue."""
        print(f"\nProcessing {self.task_queue.size()} tasks...")
        
        while not self.task_queue.is_empty():
            self.process_next_task()
        
        print(f"\nAll tasks completed! Total: {len(self.completed_tasks)}")
    
    def show_status(self):
        """Display scheduler status."""
        print(f"\nScheduler Status:")
        print(f"Pending tasks: {self.task_queue.size()}")
        print(f"Completed tasks: {len(self.completed_tasks)}")


class PrintJob:
    """Represents a print job."""
    
    def __init__(self, job_id, pages, owner):
        """
        Initialize a print job.
        
        Args:
            job_id: Unique identifier
            pages: Number of pages to print
            owner: Owner of the print job
        """
        self.job_id = job_id
        self.pages = pages
        self.owner = owner
        self.timestamp = time.time()
    
    def __str__(self):
        return f"PrintJob#{self.job_id} ({self.owner}, {self.pages} pages)"


class PrinterQueue:
    """
    Simulates a printer queue managing multiple print jobs.
    """
    
    def __init__(self, pages_per_second=2):
        """
        Initialize the printer queue.
        
        Args:
            pages_per_second: Printer speed
        """
        self.print_queue = LinkedListQueue()
        self.pages_per_second = pages_per_second
        self.total_jobs_printed = 0
    
    def submit_job(self, job):
        """
        Submit a print job.
        
        Args:
            job (PrintJob): Print job to submit
        """
        self.print_queue.enqueue(job)
        print(f"Submitted: {job}")
    
    def print_next_job(self):
        """Print the next job in the queue."""
        if self.print_queue.is_empty():
            print("No jobs in queue")
            return
        
        job = self.print_queue.dequeue()
        print(f"\nPrinting: {job}")
        
        # Simulate printing time
        print_time = job.pages / self.pages_per_second
        print(f"Estimated time: {print_time:.1f} seconds")
        
        time.sleep(min(print_time, 0.5))  # Cap simulation time
        
        self.total_jobs_printed += 1
        print(f"Completed: {job}")
    
    def print_all_jobs(self):
        """Print all jobs in the queue."""
        jobs_count = self.print_queue.size()
        print(f"\nPrinting {jobs_count} jobs...")
        
        while not self.print_queue.is_empty():
            self.print_next_job()
        
        print(f"\nAll jobs printed! Total: {self.total_jobs_printed}")
    
    def show_queue_status(self):
        """Display queue status."""
        print(f"\nPrinter Queue Status:")
        print(f"Jobs waiting: {self.print_queue.size()}")
        print(f"Jobs printed: {self.total_jobs_printed}")


class BinaryTreeNode:
    """Node for binary tree."""
    
    def __init__(self, value):
        """Initialize a tree node."""
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """
    Binary tree with breadth-first traversal using a queue.
    """
    
    def __init__(self):
        """Initialize an empty binary tree."""
        self.root = None
    
    def insert_level_order(self, values):
        """
        Insert values in level-order (breadth-first).
        
        Args:
            values (list): List of values to insert (None for empty nodes)
        """
        if not values:
            return
        
        self.root = BinaryTreeNode(values[0])
        queue = LinkedListQueue()
        queue.enqueue(self.root)
        
        i = 1
        while i < len(values):
            node = queue.dequeue()
            
            # Insert left child
            if i < len(values) and values[i] is not None:
                node.left = BinaryTreeNode(values[i])
                queue.enqueue(node.left)
            i += 1
            
            # Insert right child
            if i < len(values) and values[i] is not None:
                node.right = BinaryTreeNode(values[i])
                queue.enqueue(node.right)
            i += 1
    
    def breadth_first_traversal(self):
        """
        Perform breadth-first (level-order) traversal.
        
        Returns:
            list: Values in breadth-first order
        """
        if not self.root:
            return []
        
        result = []
        queue = LinkedListQueue()
        queue.enqueue(self.root)
        
        while not queue.is_empty():
            node = queue.dequeue()
            result.append(node.value)
            
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        
        return result
    
    def level_order_with_levels(self):
        """
        Perform level-order traversal with level information.
        
        Returns:
            list: List of lists, each containing values at that level
        """
        if not self.root:
            return []
        
        result = []
        queue = LinkedListQueue()
        queue.enqueue(self.root)
        
        while not queue.is_empty():
            level_size = queue.size()
            level_values = []
            
            for _ in range(level_size):
                node = queue.dequeue()
                level_values.append(node.value)
                
                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)
            
            result.append(level_values)
        
        return result


class CustomerServiceQueue:
    """
    Simulates a customer service queue with multiple service windows.
    """
    
    def __init__(self, num_windows=3):
        """
        Initialize customer service queue.
        
        Args:
            num_windows: Number of service windows
        """
        self.customer_queue = LinkedListQueue()
        self.num_windows = num_windows
        self.customers_served = 0
    
    def customer_arrives(self, customer_id):
        """
        Add a customer to the queue.
        
        Args:
            customer_id: Customer identifier
        """
        self.customer_queue.enqueue(customer_id)
        print(f"Customer #{customer_id} joined the queue (position: {self.customer_queue.size()})")
    
    def serve_customers(self, num_to_serve=None):
        """
        Serve customers from the queue.
        
        Args:
            num_to_serve: Number of customers to serve (None = all)
        """
        if num_to_serve is None:
            num_to_serve = self.customer_queue.size()
        
        served = 0
        while served < num_to_serve and not self.customer_queue.is_empty():
            customer_id = self.customer_queue.dequeue()
            self.customers_served += 1
            print(f"Window serving Customer #{customer_id}")
            served += 1
        
        print(f"Served {served} customers. Remaining in queue: {self.customer_queue.size()}")


def demo_basic_operations():
    """Demonstrate basic queue operations."""
    print("=== BASIC QUEUE OPERATIONS DEMO ===\n")
    
    # Array-based queue
    print("Array-based Queue:")
    array_queue = ArrayQueue()
    
    for item in [10, 20, 30, 40]:
        array_queue.enqueue(item)
        print(f"Enqueued {item}, queue: {array_queue}")
    
    print(f"Front element: {array_queue.front()}")
    
    while not array_queue.is_empty():
        item = array_queue.dequeue()
        print(f"Dequeued {item}, queue: {array_queue}")
    
    print()
    
    # Linked list-based queue
    print("Linked List-based Queue:")
    ll_queue = LinkedListQueue()
    
    for item in ['A', 'B', 'C', 'D']:
        ll_queue.enqueue(item)
        print(f"Enqueued {item}, queue: {ll_queue}")
    
    print(f"Queue size: {ll_queue.size()}")
    
    while not ll_queue.is_empty():
        item = ll_queue.dequeue()
        print(f"Dequeued {item}, queue: {ll_queue}")
    
    print()
    
    # Circular queue
    print("Circular Queue (capacity=5):")
    circular_queue = CircularQueue(5)
    
    for item in [1, 2, 3, 4, 5]:
        circular_queue.enqueue(item)
        print(f"Enqueued {item}, queue: {circular_queue}")
    
    try:
        circular_queue.enqueue(6)
    except OverflowError as e:
        print(f"Cannot enqueue 6: {e}")
    
    print(f"\nDequeuing 2 items...")
    circular_queue.dequeue()
    circular_queue.dequeue()
    print(f"Queue: {circular_queue}")
    
    print(f"\nEnqueuing 6 and 7...")
    circular_queue.enqueue(6)
    circular_queue.enqueue(7)
    print(f"Queue: {circular_queue}")
    
    print("\n" + "="*50 + "\n")


def demo_deque_operations():
    """Demonstrate deque operations."""
    print("=== DEQUE OPERATIONS DEMO ===\n")
    
    deque = Deque()
    
    print("Adding elements:")
    deque.add_rear(1)
    print(f"add_rear(1): {deque}")
    
    deque.add_rear(2)
    print(f"add_rear(2): {deque}")
    
    deque.add_front(0)
    print(f"add_front(0): {deque}")
    
    deque.add_front(-1)
    print(f"add_front(-1): {deque}")
    
    print(f"\nFront: {deque.front()}, Rear: {deque.rear()}")
    
    print("\nRemoving elements:")
    print(f"remove_front(): {deque.remove_front()}, deque: {deque}")
    print(f"remove_rear(): {deque.remove_rear()}, deque: {deque}")
    
    print("\n" + "="*50 + "\n")


def demo_task_scheduler():
    """Demonstrate task scheduling."""
    print("=== TASK SCHEDULER DEMO ===\n")
    
    scheduler = TaskScheduler()
    
    # Add tasks
    tasks = [
        Task(1, "Process user registration", 2),
        Task(2, "Send welcome email", 1),
        Task(3, "Update database", 3),
        Task(4, "Generate report", 1),
        Task(5, "Backup data", 2)
    ]
    
    for task in tasks:
        scheduler.add_task(task)
    
    scheduler.show_status()
    
    # Process all tasks
    scheduler.process_all_tasks()
    
    print("\n" + "="*50 + "\n")


def demo_printer_queue():
    """Demonstrate printer queue simulation."""
    print("=== PRINTER QUEUE DEMO ===\n")
    
    printer = PrinterQueue(pages_per_second=5)
    
    # Submit print jobs
    jobs = [
        PrintJob(1, 10, "Alice"),
        PrintJob(2, 5, "Bob"),
        PrintJob(3, 15, "Charlie"),
        PrintJob(4, 3, "David")
    ]
    
    for job in jobs:
        printer.submit_job(job)
    
    printer.show_queue_status()
    
    # Print all jobs
    printer.print_all_jobs()
    
    print("\n" + "="*50 + "\n")


def demo_breadth_first_traversal():
    """Demonstrate breadth-first tree traversal."""
    print("=== BREADTH-FIRST TRAVERSAL DEMO ===\n")
    
    tree = BinaryTree()
    
    # Create a binary tree:
    #        1
    #       / \
    #      2   3
    #     / \ / \
    #    4  5 6  7
    
    values = [1, 2, 3, 4, 5, 6, 7]
    tree.insert_level_order(values)
    
    print("Tree structure:")
    print("       1")
    print("      / \\")
    print("     2   3")
    print("    / \\ / \\")
    print("   4  5 6  7")
    print()
    
    # Breadth-first traversal
    bfs_result = tree.breadth_first_traversal()
    print(f"Breadth-first traversal: {bfs_result}")
    
    # Level-order with levels
    levels = tree.level_order_with_levels()
    print(f"\nLevel-order by levels:")
    for i, level in enumerate(levels):
        print(f"Level {i}: {level}")
    
    print("\n" + "="*50 + "\n")


def demo_hot_potato():
    """Demonstrate Hot Potato game."""
    print("=== HOT POTATO GAME DEMO ===\n")
    
    players = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']
    num_passes = 7
    
    print(f"Players: {players}")
    print(f"Number of passes: {num_passes}\n")
    
    winner = hot_potato(players, num_passes)
    
    print(f"\nWinner: {winner}!")
    
    print("\n" + "="*50 + "\n")


def demo_palindrome_checker():
    """Demonstrate palindrome checking with deque."""
    print("=== PALINDROME CHECKER DEMO ===\n")
    
    test_strings = [
        "radar",
        "hello",
        "racecar",
        "python",
        "A man a plan a canal Panama",
        "Was it a car or a cat I saw",
        "hello world"
    ]
    
    for text in test_strings:
        result = is_palindrome(text)
        status = "✓ Palindrome" if result else "✗ Not a palindrome"
        print(f"'{text}' -> {status}")
    
    print("\n" + "="*50 + "\n")


def demo_binary_number_generation():
    """Demonstrate binary number generation."""
    print("=== BINARY NUMBER GENERATION DEMO ===\n")
    
    n = 10
    print(f"Generating binary numbers from 1 to {n}:\n")
    
    binary_numbers = generate_binary_numbers(n)
    
    for i, binary in enumerate(binary_numbers, 1):
        print(f"{i:2d} -> {binary}")
    
    print("\n" + "="*50 + "\n")


def demo_customer_service():
    """Demonstrate customer service queue."""
    print("=== CUSTOMER SERVICE QUEUE DEMO ===\n")
    
    service = CustomerServiceQueue(num_windows=3)
    
    # Customers arrive
    print("Customers arriving:")
    for i in range(1, 11):
        service.customer_arrives(i)
    
    print(f"\nTotal customers in queue: {service.customer_queue.size()}\n")
    
    # Serve customers in batches
    print("Serving first batch (3 windows):")
    service.serve_customers(3)
    
    print("\nServing second batch (3 windows):")
    service.serve_customers(3)
    
    print("\nServing remaining customers:")
    service.serve_customers()
    
    print(f"\nTotal customers served: {service.customers_served}")
    
    print("\n" + "="*50 + "\n")


def demo_queue_comparison():
    """Compare different queue implementations."""
    print("=== QUEUE IMPLEMENTATION COMPARISON ===\n")
    
    test_size = 10000
    
    # Array-based queue performance
    array_queue = ArrayQueue()
    
    start_time = time.time()
    for i in range(test_size):
        array_queue.enqueue(i)
    
    for i in range(test_size):
        array_queue.dequeue()
    
    array_time = time.time() - start_time
    
    # Linked list-based queue performance
    ll_queue = LinkedListQueue()
    
    start_time = time.time()
    for i in range(test_size):
        ll_queue.enqueue(i)
    
    for i in range(test_size):
        ll_queue.dequeue()
    
    ll_time = time.time() - start_time
    
    # Circular queue performance
    circular_queue = CircularQueue(test_size)
    
    start_time = time.time()
    for i in range(test_size):
        circular_queue.enqueue(i)
    
    for i in range(test_size):
        circular_queue.dequeue()
    
    circular_time = time.time() - start_time
    
    print(f"Performance test with {test_size} operations:")
    print(f"Array-based queue: {array_time:.6f} seconds")
    print(f"Linked list-based queue: {ll_time:.6f} seconds")
    print(f"Circular queue: {circular_time:.6f} seconds")
    
    print("\nPerformance characteristics:")
    print("- Array-based: O(n) dequeue due to shifting")
    print("- Linked list-based: O(1) for all operations")
    print("- Circular queue: O(1) for all operations, fixed capacity")
    
    print("\n" + "="*50 + "\n")


def main():
    """Run all demonstrations."""
    print("QUEUE DATA STRUCTURE - COMPREHENSIVE DEMO")
    print("="*50)
    print()
    
    demo_basic_operations()
    demo_deque_operations()
    demo_task_scheduler()
    demo_printer_queue()
    demo_breadth_first_traversal()
    demo_hot_potato()
    demo_palindrome_checker()
    demo_binary_number_generation()
    demo_customer_service()
    demo_queue_comparison()
    
    print("All demonstrations completed!")


if __name__ == "__main__":
    main()
