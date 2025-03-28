#Link Problem
#https://leetcode.com/problems/partition-list/?envType=problem-list-v2&envId=linked-list

"Explantion the problem statement"
#https://www.youtube.com/watch?v=KT1iUciJr4g




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head: ListNode, x: int) -> ListNode:
    less_head = ListNode(0)  # Dummy node for the 'less than x' list
    greater_head = ListNode(0)  # Dummy node for the 'greater or equal to x' list
    less = less_head
    greater = greater_head
    
    while head:
        if head.val < x:
            less.next = head
            less = less.next
        else:
            greater.next = head
            greater = greater.next
        head = head.next
    
    greater.next = None  # End the greater list
    less.next = greater_head.next  # Connect the two lists
    
    return less_head.next  # Return the new head




print("===================================================================")

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x):
    # Create two dummy nodes to act as the heads of the two partitions
    less_head = ListNode(0)
    greater_head = ListNode(0)
    
    # Pointers to the current end of each partition
    less = less_head
    greater = greater_head
    
    # Traverse the original list
    current = head
    while current:
        if current.val < x:
            less.next = current
            less = less.next
        else:
            greater.next = current
            greater = greater.next
        current = current.next
    
    # Connect the two partitions
    less.next = greater_head.next
    greater.next = None  # End the greater partition
    
    # Return the head of the combined list
    return less_head.next

