#Problem 
#https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=problem-list-v2&envId=linked-list


#Explanation of the problem:
#https://www.youtube.com/watch?v=XVuQxVej6y8&t=72s
#https://www.youtube.com/watch?v=6gI8OMoac4Q
#https://www.youtube.com/watch?v=3kMKYQ2wNIU&t=67s


"Brute force solution "
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    curr = head
    length = 0
    # First pass: Calculate the length of the linked list
    while curr:
        length += 1
        curr = curr.next
    
    # Calculate the target node to remove
    target = length - n
    
    # If the target is the head, remove it by returning head.next
    if target == 0:
        return head.next
    
    # Second pass: Traverse to the node just before the target
    curr = head
    count = 0
    while count < target - 1:
        curr = curr.next
        count += 1
    
    # Remove the target node by adjusting the next pointer
    if curr and curr.next:
        curr.next = curr.next.next
    
    return head



print("======================================================================")



"Optimise Solution"
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    # Create a dummy node to handle edge cases where the head needs to be removed
    dummy = ListNode(0)
    dummy.next = head
    
    # Initialize two pointers
    slow = dummy
    fast = dummy
    
    # Move the fast pointer n steps ahead
    for _ in range(n):
        fast = fast.next
    
    # Move both pointers until fast reaches the end
    while fast.next:
        slow = slow.next
        fast = fast.next
    
    # Remove the nth node from the end
    slow.next = slow.next.next
    
    # Return the new head
    return dummy.next


