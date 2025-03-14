#problem
#https://leetcode.com/problems/middle-of-the-linked-list/description/?envType=problem-list-v2&envId=linked-list

"#Explanation:"
#https://www.youtube.com/watch?v=A2_ldqM4QcY
#https://www.youtube.com/watch?v=IPaMfcxQtP0



# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution:
    def middleNode(self, head):
        # Initialize both pointers to the head of the list
        slow = head
        fast = head
        
        # Traverse the list
        while fast and fast.next:
            slow = slow.next          # Move slow pointer one step
            fast = fast.next.next     # Move fast pointer two steps
        
        # When fast pointer reaches the end, slow pointer will be at the middle
        return slow

"""Explanation of the Code:
Initialization:

Both slow and fast pointers start at the head of the list.

Traversal:

The fast pointer moves two steps at a time, while the slow pointer moves one step at a time.

When the fast pointer reaches the end of the list (i.e., fast is None or fast.next is None), the slow pointer will be at the middle node.

Return the Middle Node:

The slow pointer now points to the middle node, which is returned."""

#Why This Works:
"""
For an odd number of nodes, the fast pointer will land exactly on the last node, and the slow pointer will be at the middle node.
For an even number of nodes, the fast pointer will land on None, and the slow pointer will be at the second middle node 
(as required by the problem)."""




print("=====================================================================")

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def middleNode(self, head):
        length = 0
        cur = head

        # Step 1: Count the number of nodes in the list
        while cur:
            length += 1
            cur = cur.next

        # Step 2: Calculate the middle position
        middle = length // 2

        # Step 3: Traverse to the middle node 
        cur = head
        while middle:
            cur = cur.next
            middle -= 1
        # Step 4: Return the middle node
        return cur


#First, it calculates the total length of the linked list.
#Then, it traverses the list again to find the middle node.
"""
We traverse the list once to count the nodes.
We traverse the list again to find the middle node.
"""
#Why It Works for Both Cases 
"""
The formula middle = length // 2 ensures that:

For odd lengths, it correctly identifies the exact middle node.

For even lengths, it identifies the second middle node (which is what the problem requires).

This works because integer division (//) in Python rounds down to the nearest whole number. For example:

    If length = 5, then 5 // 2 = 2.

    If length = 6, then 6 // 2 = 3.

In both cases, the result of length // 2 gives the number of steps needed to reach the desired middle node.

Summary:
middle = length // 2 works because:

For odd lengths, it gives the exact middle node.

For even lengths, it gives the second middle node (as required).

This approach is simple and easy to understand but requires two traversals of the list. For optimization, 
consider using the two-pointer approach."""




#Comparison with the Two-Pointer Approach:
"""This approach requires two traversals of the list, whereas the two-pointer approach (using slow and fast pointers) 
finds the middle node in a single traversal."""
