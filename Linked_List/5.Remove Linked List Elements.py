#Problem 
#https://leetcode.com/problems/remove-linked-list-elements/description/?envType=problem-list-v2&envId=linked-list

"Expalantion"
#https://www.youtube.com/watch?v=JI71sxtHTng&t=1s   
#https://www.youtube.com/watch?v=uIcClozwlxc



#Solution 1:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head: ListNode, val: int) -> ListNode:
    dummy = ListNode(0)  # Step 1: Create a dummy node
    dummy.next = head     # Step 2: Point dummy to head
    current = dummy       # Step 3: Use a pointer to traverse
    
    while current.next:   # Step 4: Traverse the list
        if current.next.val == val:
            current.next = current.next.next  # Remove the node
        else:
            current = current.next  # Move to the next node
            
    return dummy.next  # Step 5: Return new head (skip dummy)


print("=============================================================")

#solution 2:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(self, head, val):
    dummy_head = ListNode(-1)
    dummy_head.next = head
    current_node = dummy_head

    while current_node.next != None:
        
        if current_node.next.val == val:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next
            
    return dummy_head.next



print("=============================================================")

#solution 3:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val: int):

    prev, curr = None, head
    
    while curr:

        if curr.val == val:  # cases 1-3
            if prev:  # cases 1-2
                prev.next = curr.next
            else:  # case 3
                head = curr.next
            curr = curr.next  # for all cases

        else:  # case 4
            prev, curr = curr, curr.next

    return head


