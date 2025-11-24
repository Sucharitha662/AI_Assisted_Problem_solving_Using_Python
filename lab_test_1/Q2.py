#You are a Python programming assistant. Write Python classes for common data structures. Each example should include: 
#A clear class definition 
#Methods implementation 
#A small usage example 
#Proper handling of edge cases 
"""Example 1: Stack 

class Stack: def init(self): self.items = [] 

def push(self, item): 
    self.items.append(item) 
 
def pop(self): 
    if self.items: 
        return self.items.pop() 
    return None 

stack = Stack() stack.push(10) stack.push(20) print(stack.pop()) # 20 

 

Example 2: Queue 

class Queue: def init(self): self.items = [] 

def enqueue(self, item): 
    self.items.append(item) 
 
def dequeue(self): 
    if self.items: 
        return self.items.pop(0) 
    return None 
 queue = Queue() queue.enqueue(1) queue.enqueue(2) print(queue.dequeue()) # 1 

 

Now, write Python code for a Singly Linked List with the following specifications: 

insert(data): Insert a new node at the end of the list. 

delete(value): Delete a node by its value. 

display(): Print all nodes in order. 

Include a usage example demonstrating insertion, deletion, and display. Make sure the code handles edge cases like deleting from an empty list or deleting a value not present in the list."""

# Node class for singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, value):
        """Delete the first node with the specified value."""
        current = self.head
        prev = None

        while current and current.data != value:
            prev = current
            current = current.next

        if not current:
            print(f"Value {value} not found in the list.")
            return

        if prev is None:
            # Deleting the head node
            self.head = current.next
        else:
            prev.next = current.next

    def display(self):
        """Print all nodes in the list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Usage example
if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    ll.display()  # 10 -> 20 -> 30 -> None

    ll.delete(20)
    ll.display()  # 10 -> 30 -> None

    ll.delete(100)  # Value 100 not found in the list
