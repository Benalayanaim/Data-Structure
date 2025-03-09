#problem Link

#https://leetcode.ca/2019-12-13-1474-Delete-N-Nodes-After-M-Nodes-of-a-Linked-List/
#https://www.youtube.com/watch?v=dLxAMSmVapE



#solution 1:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNodes(head: ListNode, m: int, n: int) -> ListNode:
    current = head
    while current:
        # Keep m nodes
        for _ in range(m - 1):
            if current is None:
                return head
            current = current.next
        
        if current is None:
            return head
        
        # Remove n nodes
        temp = current.next
        for _ in range(n):
            if temp is None:
                break
            temp = temp.next
        
        # Link the retained part with the remaining nodes
        current.next = temp
        current = temp
    
    return head

print("====================================================================================")

#solution 2:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNodes(head: ListNode, m: int, n: int) -> ListNode:
    current = head
    
    while current:
        # Keep the first m nodes
        for _ in range(m - 1):
            if current:
                current = current.next
            else:
                break
        
        if not current:
            break
        
        # Skip the next n nodes
        temp = current.next
        for _ in range(n):
            if temp:
                temp = temp.next
            else:
                break
        
        # Connect the current node to the node after the skipped n nodes
        current.next = temp
        
        # Move to the next node after the skipped n nodes
        current = temp
    
    return head

print("====================================================================================")

#solution 3:
# Python program to delete n nodes
# after m nodes of a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to skip m nodes and then delete n nodes
# of the linked list
def skipMdeleteN(head, m, n):
    curr = head  # Current node pointer
    count = 0    # Counter variable

    # Traverse through the entire linked list
    while curr:

        # Skip m nodes
        for count in range(1, m):
            if curr is None:
                return head
            curr = curr.next

        # If end of the list is reached, return the head
        if curr is None:
            return head

        # Start from the next node and delete n nodes
        t = curr.next
        for count in range(1, n + 1):
            if t is None:
                break
            temp = t
            t = t.next
            del temp  # Delete the node

        # Link the current node to the remaining list
        curr.next = t

        # Move the current pointer to the next node
        curr = t

    return head

"see the whole implementaion for this solution"
#https://www.geeksforgeeks.org/delete-n-nodes-after-m-nodes-of-a-linked-list/







