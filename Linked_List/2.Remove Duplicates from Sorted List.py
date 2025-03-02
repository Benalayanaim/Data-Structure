#Problem : 
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/?envType=problem-list-v2&envId=linked-list

"Demonstration"
#https://www.youtube.com/watch?v=irBmJbVarQg&t=500s



#solution
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: ListNode) -> ListNode:
    current = head

    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    
    return head



"the solution 2 the same than 1 but more clear"

#solution2
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: ListNode) -> ListNode:
        current = head

        while current is not None and current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
    


"implementaion af the linked list with the code solution"

#solution
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: ListNode) -> ListNode:
    current = head

    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    
    return head

# Helper function to convert a list to a linked list
def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list
def linkedlist_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst

# Example usage:
if __name__ == "__main__":
    # Example 1
    head1 = list_to_linkedlist([1, 1, 2])
    result1 = deleteDuplicates(head1)
    print(linkedlist_to_list(result1))  

    # Example 2
    head2 = list_to_linkedlist([1, 1, 2, 3, 3])
    result2 = deleteDuplicates(head2)
    print(linkedlist_to_list(result2))  



#Explanation : https://chat.deepseek.com/a/chat/s/6e452228-be63-4099-90b1-f4b6ae180e05
