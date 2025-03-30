#Link of the problem 
# https://leetcode.com/problems/odd-even-linked-list/description/?envType=problem-list-v2&envId=linked-list

"Explanation of the problem statement"
# https://www.youtube.com/watch?v=WoUAs7R3Ao4
# https://www.youtube.com/watch?v=qf6qp7GzD5Q







"Brute Force Solution"
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # Base case
        if not head:
            return None
        
        # Initialize variables to store odd and even nodes
        odd_nodes = []
        even_nodes = []
        
        # Initialize index
        index = 1
        
        # Traverse the linked list
        current = head
        while current:
            # Check if the index is odd or even
            if index % 2 != 0:
                odd_nodes.append(current.val)
            else:
                even_nodes.append(current.val)
            
            # Move to the next node and increment the index
            current = current.next
            index += 1
        
        # Create a new linked list with the odd and even nodes
        dummy = ListNode()
        current = dummy
        for val in odd_nodes + even_nodes:
            current.next = ListNode(val)
            current = current.next
        
        # Return the head of the reordered list
        return dummy.next


"""
The line for val in odd_nodes + even_nodes: is iterating over the combined list of odd_nodes and even_nodes.

Here's a breakdown of what's happening:
odd_nodes + even_nodes: This is concatenating (joining) the two lists odd_nodes and even_nodes together.
for val in ...: This is a Python for loop that's iterating over the combined list.
"""
#OR
"""
Instead of concatenating odd_nodes and even_nodes using the + operator, you can also use the following methods to join them:

Using the extend() method

"""
#OR
"""
for val in odd_nodes: # do something odd_nodes.extend(even_nodes) for val in odd_nodes: # do something

   However, this will modify the `odd_nodes` list in place.

2. **Using a loop**:
   ```python
for val in odd_nodes:
    # do something
for val in even_nodes:
    # do something
    # """




"Optimize solution"
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        even_head = even
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = even_head
        return head
    


