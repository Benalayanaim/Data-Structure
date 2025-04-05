#Problem link 
# https://leetcode.com/problems/delete-node-in-a-linked-list/?envType=problem-list-v2&envId=linked-list






class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNode(node):
    """
    Deletes the given node from the singly linked list.
    Since we don't have access to the head, we overwrite the given node with the next node.
    """
    node.val = node.next.val  # Copy the next node's value to the current node
    node.next = node.next.next  # Remove the next node from the list


"Other vizulization of the code solution"
# https://leetcode.com/problems/delete-node-in-a-linked-list/solutions/5113147/detailed-explanation-extremely-simple-1-2-liner-o-1-time-and-space-complexity/?envType=problem-list-v2&envId=linked-list
# https://leetcode.com/problems/delete-node-in-a-linked-list/solutions/354949/python3-change-value-and-change-pointer/?envType=problem-list-v2&envId=linked-list
