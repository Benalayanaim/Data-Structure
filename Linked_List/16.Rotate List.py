#Problem 
#https://leetcode.com/problems/rotate-list/description/?envType=problem-list-v2&envId=linked-list

"Explanation of the Problem Statement"
#https://www.youtube.com/watch?v=UcGtPs2LE_c
#https://www.youtube.com/watch?v=uT7YI7XbTY8



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head, k):
    if not head or k == 0:
        return head
    
    # Step 1: Find the length of the linked list
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1
    
    # Step 2: Calculate the effective number of rotations
    k = k % length
    if k == 0:
        return head
    
    # Step 3: Find the new head and tail
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    
    # Step 4: Rotate the list
    new_tail.next = None
    tail.next = head
    
    return new_head


"explanation "
#https://chat.deepseek.com/a/chat/s/2ffb7403-23c4-4c40-94b4-dbca3ea0b7c2


print("======================================================")

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head: ListNode, k: int) -> ListNode:
    if not head or not head.next or k == 0:
        return head
    
    # Compute the length of the linked list
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1
    
    # Make it a circular linked list
    tail.next = head
    
    # Find the new tail: (length - k % length - 1)th node
    k = k % length
    if k == 0:
        tail.next = None
        return head
    
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next
    
    # New head is next of new_tail
    new_head = new_tail.next
    new_tail.next = None
    
    return new_head


"explanation from My ChatGpt"
#https://chatgpt.com/c/67dcbc10-6724-800f-8265-4460d85d0808

print("======================================================")


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head: ListNode, k: int) -> ListNode:
    if not head:
        return None
    if k == 0:
        return head
    temp = head
    a = []
    while temp:
        a.append(temp.val)
        temp = temp.next
    k = k % len(a)
    b = a[-k:] + a[:-k]
    dummy = ListNode()
    t = dummy
    for i in b:
        t.next = ListNode(i)
        t = t.next
    return dummy.next


"explanation for the last soluiton"
#https://chat.deepseek.com/a/chat/s/2ffb7403-23c4-4c40-94b4-dbca3ea0b7c2

#https://chatgpt.com/c/67dcbc10-6724-800f-8265-4460d85d0808
