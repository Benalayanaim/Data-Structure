# Problem 
# https://leetcode.com/problems/palindrome-linked-list/description/?envType=problem-list-v2&envId=linked-list

"Explanation of the Problem statement"
# https://www.youtube.com/watch?v=yOzXms1J6Nk
# https://www.youtube.com/watch?v=WyI5dXMHW5c&list=PLFdAYMIVJQHN6J5-OCh7pbG0o8WHC9so3&index=18
# https://www.youtube.com/watch?v=lRY_G-u_8jk





class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: ListNode) -> bool:
    if not head or not head.next:
        return True
    
    # Step 1: Find the middle of the linked list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Step 2: Reverse the second half of the list
    prev, curr = None, slow
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    # Step 3: Compare the first and second halves
    first, second = head, prev
    while second:  # The second half will be shorter or equal in length
        if first.val != second.val:
            return False
        first = first.next
        second = second.next
    
    return True

"Explanation from my ChatGpt"
# https://chatgpt.com/c/67e34382-2574-800f-b76d-b0cdd2c9fd60

# https://chat.deepseek.com/a/chat/s/68d11f48-9c9a-4310-88f6-83c5522c41da


print("================================================================")

"Using List"
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head:ListNode) -> bool:
        list_vals=[]
        while head:
            list_vals.append(head.val)
            head = head.next
        if list_vals==list_vals[::-1]:
            return True
        else:
            return False
        

print("================================================================")

"Using List"
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        values = []
        cur = head 
        while cur is not None:
            values.append(cur.val)
            cur = cur.next
        left = 0
        right = len(values)-1
        while left < right:
            if values[left] != values[right]:
                return False
            left+=1
            right-=1
        return True
        
        


print("================================================================")

"Using Stack"
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack: list[int] = []
        result = True
        curr = head

        while curr:
            stack.append(curr.val)
            curr = curr.next

        while head:
            if head.val != stack.pop():
                result = False
                break
            head = head.next

        return result
        




