#Problem
#https://leetcode.com/problems/intersection-of-two-linked-lists/description/?envType=problem-list-v2&envId=linked-list


"Explanation"
#https://www.youtube.com/watch?v=0JHQ26NQcPk
#https://www.youtube.com/watch?v=D0X0BONOQhI








#Solution 
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    if not headA or not headB:
        return None

    pA, pB = headA, headB

    # Traverse both lists
    while pA != pB:
        # Move pA to the next node or redirect to headB
        if pA:
            pA = pA.next
        else:
            pA = headB

        # Move pB to the next node or redirect to headA
        if pB:
            pB = pB.next
        else:
            pB = headA

    # If pA and pB meet, return the intersection node
    # If both reach the end (null), return null
    return pA




#"Explanation : https://chat.deepseek.com/a/chat/s/b9e07ed2-1348-42f6-aee2-cb428035ed82"



print("=======================================Solution two====================================== ")

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) :
        st = set()
        while headA!=None:
            st.add(headA)
            headA = headA.next
        while headB!=None:
            if headB in st:
                return headB
            headB = headB.next
        return None
        


            
        
        