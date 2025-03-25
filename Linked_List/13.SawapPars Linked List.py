#Poblem Link
#https://leetcode.com/problems/swap-nodes-in-pairs/?envType=problem-list-v2&envId=linked-list


"Explanation of the problem statement"
#https://www.youtube.com/watch?v=o811TZLAWOo
#https://www.youtube.com/watch?v=M9lsf_ySE9s&t=180s
#https://leetcode.com/problems/swap-nodes-in-pairs/solutions/1775033/swapping-nodes-not-just-the-values-visual-explanation-well-explained-c/?envType=problem-list-v2&envId=linked-list







class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: ListNode) -> ListNode:
    # Create a dummy node to simplify edge cases
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    while prev.next and prev.next.next:
        # Nodes to be swapped
        first = prev.next
        second = prev.next.next
        
        # Swapping
        prev.next = second
        first.next = second.next
        second.next = first
        
        # Move prev to the next pair
        prev = first
    
    return dummy.next


"#Explanation"
#https://chat.deepseek.com/a/chat/s/94743bc9-cf54-4ad3-8532-74b127b23834


print("==================================================================")


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    while head and head.next:
        first = head
        second = head.next
        
        # Swapping
        prev.next = second
        first.next = second.next
        second.next = first
        
        # Move pointers
        prev = first
        head = first.next
    
    return dummy.next

"#Explanation from my chat"
#https://chatgpt.com/c/67d393ed-f3a4-800f-b6e6-4584a8893311