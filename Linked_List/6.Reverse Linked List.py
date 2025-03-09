#Problem 
#https://leetcode.com/problems/reverse-linked-list/description/?envType=problem-list-v2&envId=linked-list

"Explanation "
#https://www.youtube.com/watch?v=G0_I-ZF0S38
#https://www.youtube.com/watch?v=3IN0BP9Ni6E

#Solution 1:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        next_temp = curr.next  # Store the next node
        curr.next = prev       # Reverse the link
        prev = curr            # Move prev to current node
        curr = next_temp       # Move to next node
    return prev  # New head of the reversed list




print("===============================================================")

#Solution 2:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    if not head:
        return None
    
    stack = []  # Initialize an empty stack
    current = head
    
    # Step 1: Push all node values onto the stack
    while current:
        stack.append(current.val)
        current = current.next
    
    # Step 2: Traverse the list again and update values using the stack
    current = head
    while current:
        current.val = stack.pop()  # Pop from the stack and update the node's value
        current = current.next
    
    return head  # Return the head of the reversed list


print("===============================================================")

#Solution 3:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    # Base case: if head is None or only one node, return head
    if not head or not head.next:
        return head
    
    # Recursively reverse the rest of the list
    new_head = reverseList(head.next)
    
    # Reverse current node's pointer
    head.next.next = head
    head.next = None  # Set current node's next to None to avoid cycles
    
    return new_head  # Return the new head of the reversed list




print("===============================================================")

#Solution 4:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(self, head):
        if not head:
            return None

        rev = ListNode(val=head.val, next=None)
        
        while head.next:
            head = head.next
            rev = ListNode(val=head.val, next=rev)
        
        return rev

