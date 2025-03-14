#Link of the problem:

#https://leetcode.ca/2024-03-14-3063-Linked-List-Frequency/
#https://www.youtube.com/watch?v=SkIlCgXCS4M&t=20s


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linked_list_frequency(head):
    # Step 1: Count the frequency of each element
    frequency_map = {}
    current = head
    while current:
        if current.val in frequency_map:
            frequency_map[current.val] += 1
        else:
            frequency_map[current.val] = 1
        current = current.next
    
    # Step 2: Create a new linked list with the frequencies
    dummy = ListNode()
    current_new = dummy
    for freq in frequency_map.values():
        current_new.next = ListNode(freq)
        current_new = current_new.next
    
    return dummy.next



print("===============================================")

from collections import Counter

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linked_list_frequency(head: ListNode) -> ListNode:
    # Step 1: Count the frequency of each distinct element
    freq_counter = Counter()
    current = head
    
    while current:
        freq_counter[current.val] += 1
        current = current.next
    
    # Step 2: Create a new linked list from frequency values
    dummy = ListNode()
    new_head = dummy
    
    for freq in freq_counter.values():
        new_head.next = ListNode(freq)
        new_head = new_head.next
    
    return dummy.next


print("===============================================")

"Without a dummy we can implemnt like this "

def linked_list_frequency(head: ListNode) -> ListNode:                   
    freq_counter = Counter()  
    current = head
    
    while current:
        freq_counter[current.val] += 1
        current = current.next
    
    # Without a dummy node
    new_head = None
    tail = None
    
    for freq in freq_counter.values():
        new_node = ListNode(freq)
        
        if new_head is None:  # Handling the first node separately
            new_head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node  # Move tail pointer
    
    return new_head

"OR"
# Step 2: Create a new linked list with the frequencies
"""
new_head = None
current_new = None
for freq in frequency_map.values():
    if new_head is None:
        new_head = ListNode(freq)
        current_new = new_head
    else:
        current_new.next = ListNode(freq)
        current_new = current_new.next

return new_head
"""





