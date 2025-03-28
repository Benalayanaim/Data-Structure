# link of the problem
# https://leetcode.com/problems/sort-list/?envType=problem-list-v2&envId=linked-list

"Explanation of the problem statement"
# https://www.youtube.com/watch?v=TGveA1oFhrc
# https://www.youtube.com/watch?v=8ocB7a_c-Cc&t=37s




"Optimize Solutions "

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sorted_lists(l1, l2):
    dummy = ListNode()
    tail = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    
    tail.next = l1 if l1 else l2
    return dummy.next

def find_middle(head):
    slow, fast = head, head.next
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    return slow

def sort_list(head):
    if not head or not head.next:
        return head
    
    mid = find_middle(head)
    right_head = mid.next
    mid.next = None
    
    left_sorted = sort_list(head)
    right_sorted = sort_list(right_head)
    
    return merge_sorted_lists(left_sorted, right_sorted)


"Explanation from my ChtapGpt"
# https://chatgpt.com/c/67e1f5fb-8b90-800f-8fda-57dfba0fa2d3




# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        # Split the list into two halves
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp
        
        # Recursively sort each half
        left_sorted = self.sortList(left)
        right_sorted = self.sortList(right)
        
        # Merge the sorted halves
        return self.merge(left_sorted, right_sorted)
    
    def getMid(self, head: ListNode) -> ListNode:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        
        if left:
            tail.next = left
        if right:
            tail.next = right
        
        return dummy.next
    
"Explanation "
# https://chat.deepseek.com/a/chat/s/ec32d4fb-7c41-4cbd-a7bb-2736ba26ba96



print("============================================================================")


"Brute force Solutions "

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        gods_amazing = []
        curr = head

        # adding node values to the array
        while curr:
            gods_amazing.append(curr.val)
            curr = curr.next

        # sorting the values
        gods_amazing.sort()

        # replacing the values with the sorted ones
        curr = head
        for i in range(len(gods_amazing)):
            curr.val = gods_amazing[i]
            curr = curr.next

        return head
        


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
       
        temp=head
        new_list=[]

      

        while temp:
            new_list.append(temp.val)
            temp=temp.next

        new_list.sort()

        temp=head

        for val in new_list:
            temp.val=val
            temp=temp.next

        return head    


        
        