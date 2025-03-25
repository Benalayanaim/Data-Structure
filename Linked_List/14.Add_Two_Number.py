#probelm Link 
#https://leetcode.com/problems/add-two-numbers/?envType=problem-list-v2&envId=linked-list


"Explanation of the problem statement"
#https://www.youtube.com/watch?v=wgFPrzTjm7s&t=1s
#https://www.youtube.com/watch?v=KMS0WFxrsT8&t=2s
#https://www.youtube.com/watch?v=XmRrGzR6udg&t=1s





class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next
        
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    return dummy.next


print("=======================================================================")

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # Initialize a dummy node to simplify the construction of the result linked list
    dummy = ListNode()
    # Initialize a pointer 'current' to build the result linked list
    current = dummy
    # Initialize 'carry' to 0 to keep track of the carry-over during addition
    carry = 0
    
    # Loop until both input linked lists are fully traversed and there is no carry left
    while l1 or l2 or carry:
        # Get the value of the current node in l1, or 0 if l1 is None
        val1 = l1.val if l1 else 0
        # Get the value of the current node in l2, or 0 if l2 is None
        val2 = l2.val if l2 else 0
        
        # Calculate the total sum of the current digits and the carry
        total = val1 + val2 + carry
        # Update the carry for the next iteration (total // 10 gives the carry)
        carry = total // 10
        # Calculate the digit to be placed in the result linked list (total % 10 gives the digit)
        digit = total % 10
        
        # Create a new node with the calculated digit and attach it to the result linked list
        current.next = ListNode(digit)
        # Move the 'current' pointer to the newly created node
        current = current.next
        
        # Move to the next nodes in the input linked lists if they exist
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    # Return the result linked list, which starts from the next node of the dummy node
    return dummy.next




print("=======================================================================")



"Brute force solution"
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        final = []
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum = val1 + val2 + carry
            carry = sum //10
            #final.append(sum%10)
            digit = sum % 10
            final.append(digit)
            

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        dummy = ListNode()
        curr = dummy
        for num in final:
            curr.next = ListNode(num)
            curr = curr.next
        
        return dummy.next
