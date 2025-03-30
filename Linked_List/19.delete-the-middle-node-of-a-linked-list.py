#Problem Link
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/?envType=problem-list-v2&envId=linked-list




"Using dummy"
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        
        if head == None :return None
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next
        return dummy.next

print("==========================================================================")

"Without dummy"
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        # Single node case: return None
        if not head.next:
            return None
        
        # Initialize pointers
        slow = head
        fast = head.next.next  # Start fast two steps ahead
        
        # Move until fast reaches end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Delete middle node
        slow.next = slow.next.next
        
        return head
    

print("==========================================================================")

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        temp = head
        n = 0
        while temp != None:
            temp = temp.next
            n += 1
        mid = n//2
        prev = head
        
        while mid > 0:
            temp = prev
            prev = prev.next
            mid -= 1
        
        temp.next = prev.next
        
        return head


print("==========================================================================")


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        curr = head
        c = 0

        while curr:
            curr = curr.next
            c += 1
        
        if c == 1:
            head = None
            return head
        curr = head
        
        for i in range(c // 2):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        
        return head
    


"befor see the explanation walkthrough each example with paper, then see"
"Explanation all solution"
#https://chat.deepseek.com/a/chat/s/13641615-2fd5-4a7a-a188-536744aa8dba