#Problem
#https://leetcode.com/problems/implement-queue-using-stacks/description/?envType=problem-list-v2&envId=queue







class MyQueue:
    def __init__(self):
        self.stack_in = []  # Used for enqueue operation
        self.stack_out = []  # Used for dequeue operation

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        self._move()  # Move elements if needed
        return self.stack_out.pop()
    
    def peek(self) -> int:
        self._move()  # Ensure elements are in correct order
        return self.stack_out[-1]  # Peek at the front element
    
    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out
    
    def _move(self):
        """Move elements from stack_in to stack_out if stack_out is empty."""
        if not self.stack_out:  # Only move when stack_out is empty
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())  # Reverse order

# Example usage:
myQueue = MyQueue()
myQueue.push(1)  # Queue: [1]
myQueue.push(2)  # Queue: [1, 2]
print(myQueue.peek())  # Output: 1 (Front element)
print(myQueue.pop())   # Output: 1 (Removes front element, Queue: [2])
print(myQueue.empty()) # Output: False (Queue still has elements)


print("=====================================================================")

class MyQueue:

    def __init__(self):
        
        # Two stacks for input and output
        self.stack_push = []
        self.stack_pop = []

    def push(self, x: int) -> None:
        # Push to the input stack
        self.stack_push.append(x)

    def pop(self) -> int:
        # If the output stack is empty, transfer all elements from input stack
        if not self.stack_pop:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
        # Pop from the output stack
        return self.stack_pop.pop()

    def peek(self) -> int:
        # If the output stack is empty, transfer all elements from input stack
        if not self.stack_pop:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
        # Peek the element at the front of the queue (top of the output stack)
        return self.stack_pop[-1]

    def empty(self) -> bool:
        # The queue is empty if both stacks are empty
        return not self.stack_push and not self.stack_pop

# Example usage:
myQueue = MyQueue()
myQueue.push(1)  # Queue: [1]
myQueue.push(2)  # Queue: [1, 2]
print(myQueue.peek())  # Output: 1 (Front element)
print(myQueue.pop())   # Output: 1 (Removes front element, Queue: [2])
print(myQueue.empty()) # Output: False (Queue still has elements)



print("=====================================================================")

from collections import deque

class MyQueue:
    def __init__(self):
        self.stack_in = deque()  # Used for enqueue operation
        self.stack_out = deque()  # Used for dequeue operation

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        self._move()
        return self.stack_out.pop()

    def peek(self) -> int:
        self._move()
        return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out
    
    def _move(self):
        """Move elements from stack_in to stack_out if stack_out is empty."""
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

# Example usage:
myQueue = MyQueue()
myQueue.push(1)  # Queue: [1]
myQueue.push(2)  # Queue: [1, 2]
print(myQueue.peek())  # Output: 1 (Front element)
print(myQueue.pop())   # Output: 1 (Removes front element, Queue: [2])
print(myQueue.empty()) # Output: False (Queue still has elements)



print("=====================================================================")

from collections import deque

class MyQueue:

    def __init__(self):
        # Initialize a deque to store the queue elements
        self.queue = deque()

    def push(self, x: int) -> None:
        # Add an element to the back of the queue
        self.queue.append(x)

    def pop(self) -> int:
        # Remove and return the element from the front of the queue
        return self.queue.popleft()

    def peek(self) -> int:
        # Return the element at the front of the queue without removing it
        return self.queue[0]

    def empty(self) -> bool:
        # Check if the queue is empty
        return not self.queue
    
# Example usage:
myQueue = MyQueue()
myQueue.push(1)  # Queue: [1]
myQueue.push(2)  # Queue: [1, 2]
print(myQueue.peek())  # Output: 1 (Front element)
print(myQueue.pop())   # Output: 1 (Removes front element, Queue: [2])
print(myQueue.empty()) # Output: False (Queue still has elements)



#Explanation : https://chatgpt.com/c/67b317ad-7210-800f-b951-b15e4ea4e942
#Explanation : https://chat.deepseek.com/a/chat/s/cdf494af-0a13-4f7c-ad5e-9b9dc6c612cb

"Resource : https://www.geeksforgeeks.org/deque-in-python/"