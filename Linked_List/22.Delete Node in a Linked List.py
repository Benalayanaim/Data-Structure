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



"Explanation from My chatGpt"
# https://chatgpt.com/c/67e892f6-e518-800f-a46c-c5d940bac296

# https://chat.deepseek.com/a/chat/s/e9709600-9ed3-4f16-84ae-d62d57addfbd


"Other vizulization of the code solution"
# https://leetcode.com/problems/delete-node-in-a-linked-list/solutions/5113147/detailed-explanation-extremely-simple-1-2-liner-o-1-time-and-space-complexity/?envType=problem-list-v2&envId=linked-list
# https://leetcode.com/problems/delete-node-in-a-linked-list/solutions/354949/python3-change-value-and-change-pointer/?envType=problem-list-v2&envId=linked-list