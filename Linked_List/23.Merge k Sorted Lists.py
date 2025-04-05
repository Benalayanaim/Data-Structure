#Link of the problem
# https://leetcode.com/problems/merge-k-sorted-lists/description/?envType=problem-list-v2&envId=linked-list


"Explanation of the Problem statement"
# https://www.youtube.com/watch?v=1zktEppsdig&t=3s
# https://www.youtube.com/watch?v=kpCesr9VXDA



"Brute Force with Sorting"
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        # Step 1: Collect all node values
        all_values = []
        for head in lists:
            current = head
            while current:
                all_values.append(current.val)
                current = current.next
        
        # Step 2: Sort the collected values
        all_values.sort()
        
        # Step 3: Build the merged linked list
        dummy = ListNode(0)
        current = dummy
        for val in all_values:
            current.next = ListNode(val)
            current = current.next
        
        return dummy.next






print("====================================================")

"Merge Lists One by One"
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        
        # Start with the first list as the merged list
        merged_list = lists[0]
        
        # Iterate through the remaining lists and merge them one by one
        for i in range(1, len(lists)):
            merged_list = self.mergeTwoLists(merged_list, lists[i])
        
        return merged_list
    
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        # Attach the remaining nodes of l1 or l2
        current.next = l1 if l1 else l2
        
        return dummy.next
print("====================================================")




"Priority Queue (Min-Heap)"
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        # Create a min-heap
        min_heap = []
        # Use a counter to avoid comparing ListNode objects when heap values are equal
        counter = 0
        
        # Initialize the heap with the first node of each list
        for head in lists:
            if head:
                heapq.heappush(min_heap, (head.val, counter, head))
                counter += 1
        
        # Dummy node to build the result
        dummy = ListNode(0)
        current = dummy
        
        while min_heap:
            val, _, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, counter, node.next))
                counter += 1
        
        return dummy.next

