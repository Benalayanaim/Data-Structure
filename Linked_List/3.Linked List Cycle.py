#Problem
#https://leetcode.com/problems/linked-list-cycle/description/?envType=problem-list-v2&envId=linked-list








"Solution 1"

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: ListNode) -> bool:
    if not head or not head.next:
        return False
    
    slow = head  # Tortoise (moves one step at a time)
    fast = head  # Hare (moves two steps at a time)
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True  # Cycle detected
    
    return False  # No cycle found

# Example 1: Cycle exists
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Cycle

print(hasCycle(node1))  # """this is the Head"""

# Example 2: Cycle exists
node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2
node2.next = node1  # Cycle

print(hasCycle(node1))  #"""this is the Head"""

# Example 3: No cycle
node1 = ListNode(1)
print(hasCycle(node1))  #"""this is the Head"""


"Solution 2=========================================================================="

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: ListNode) -> bool:
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next  # Move slow pointer by 1 step
        fast = fast.next.next  # Move fast pointer by 2 steps
        
        if slow == fast:
            return True  # Cycle detected
    
    return False  # No cycle


"Solution 3=========================================================================="

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 
        
def hasCycle(head: ListNode) -> bool:
        visited_nodes = set()  # Set to keep track of visited nodes
        current_node = head    # Start from the head of the linked list        
        
        while current_node:
            if current_node in visited_nodes:

                return True  # Cycle detected
            
            visited_nodes.add(current_node)
            current_node = current_node.next     

        return False  # No cycle found

# Linked list: 1 -> 2 -> 3 -> None
"Example 1: No Cycle"
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

head = node1 #node1 is current_node

# Linked list: 1 -> 2 -> 3 -> 2 (cycle)
"Example 2: Cycle Exists"
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
node3.next = node2  # Cycle

head = node1 # node1 is current_node

"Fom chat mte3iii"
#Explanation :https://chatgpt.com/c/67c47d19-5930-800f-a315-27882b305172
#Explanation https://chat.deepseek.com/a/chat/s/ec59358f-b7ba-4be6-9882-932eb87675ff

"this is a very good explanation"
#https://www.youtube.com/watch?v=gBTe7lFR3vc&t=559s


        




"""Full code
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False

# Helper function to create a linked list from an array and add a cycle
def createLinkedList(arr, pos):
    if not arr:
        return None

    # Create the head of the linked list
    head = ListNode(arr[0])
    current = head
    cycle_node = None

    # Create the rest of the linked list
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next

        # Save the node where the cycle should connect
        if i == pos:
            cycle_node = current

    # Create the cycle
    if pos != -1:
        current.next = cycle_node

    return head

# Example 1: List with a cycle [3, 2, 0, -4], pos = 1 (cycle at index 1)
arr = [3, 2, 0, -4]
pos = 1
head = createLinkedList(arr, pos)

s = Solution()
print(s.hasCycle(head))  # Output should be True

# Example 2: List without a cycle [1, 2, 3, 4, 5], pos = -1 (no cycle)
arr = [1, 2, 3, 4, 5]
pos = -1
head = createLinkedList(arr, pos)

print(s.hasCycle(head))  # Output should be False
"""
     