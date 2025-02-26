#Problem
#https://leetcode.com/problems/merge-two-sorted-lists/description/?envType=problem-list-v2&envId=linked-list





#Solution 1:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    # Create a dummy node to act as the start of the merged list
    dummy = ListNode()
    current = dummy
    
    # Traverse both lists and merge them
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # If one of the lists is not empty, append it to the merged list
    if list1:
        current.next = list1
    elif list2:
        current.next = list2
    
    # The merged list starts from the next of the dummy node
    return dummy.next

"What If We Don't Use a Dummy Node"
print("================================================================")
#solution:
def mergeTwoLists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1
    
    if list1.val < list2.val:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next
    
    current = head
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    current.next = list1 if list1 else list2
    return head


"read both explanation very intersting"
"mii chat mte3iii"
#https://chatgpt.com/c/67bf2f68-abf4-800f-a6d7-df4b5f8f7f07
#https://chat.deepseek.com/a/chat/s/9d7a335d-fa19-4563-9e3e-08c9d1774396

print("==============================================================")


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"These main problem, the other in the comment to implement linked List with python by the helpr function"

def mergeTwoLists(self, list1, list2) :
    # Create a dummy node to act as the head of the merged list 
    dummy = ListNode()
    current = dummy

    #Loop until either list is exhausted
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    #if any node are left in either list, anppend them 
    if list1:
        current.next = list1
    if list2:
        current.next = list2
    
    #the merged list starts after the dummy node
    return dummy.next

"# Helper function to convert a list to a linked list"
#def list_to_linkedlist(lst):
#    dummy = ListNode()
#    current = dummy
#    for val in lst:
#        current.next = ListNode(val)
#        current = current.next
#    return dummy.next
#
"# Helper function to convert a linked list to a list"
#def linkedlist_to_list(node):
#    lst = []
#    while node:
#        lst.append(node.val)
#        node = node.next
#    return lst

"# Example usage:"
#list2 = list_to_linkedlist([1, 3, 4])
#merged_list = mergeTwoLists(list1, list2)
#print(linkedlist_to_list(merged_list))  
#list1 = list_to_linkedlist([1, 2, 4])

"""Explanation:
--ListNode class: This is a typical class definition for a node in a singly linked list. Each node contains a value (val) and a 
pointer to the next node (next).

--mergeTwoLists function:

--We initialize a dummy node to simplify the logic for adding nodes to the new merged list.
--The current pointer is used to track where to add the next node in the merged list.
--We loop through both lists (list1 and list2) until one is exhausted, always linking the smaller value to the current node and moving 
forward in the list.
--After the loop, if either list still has remaining nodes, we link the rest of that list directly to the current pointer.
--Finally, we return dummy.next, as the dummy node is just a placeholder and the actual merged list starts after it.
"""

