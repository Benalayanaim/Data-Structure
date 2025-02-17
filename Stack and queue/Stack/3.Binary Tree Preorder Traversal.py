
#Problem : https://leetcode.com/problems/binary-tree-preorder-traversal/description/?envType=problem-list-v2&envId=stack







#Solution 1:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def preorderTraversal(root):
    if not root:
        return []

    stack, result = [root], []

    while stack:
        node = stack.pop()
        result.append(node.val)

        if node.right:
            stack.append(node.right)  # Right child is pushed first (processed last)
        if node.left:
            stack.append(node.left)  # Left child is pushed second (processed next)

    return result

# Example usage:
# Example 1
root1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(preorderTraversal(root1)) 

# Example 2
root2 = TreeNode(1, 
                 TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))), 
                 TreeNode(3, None, TreeNode(8, TreeNode(9))))
print(preorderTraversal(root2)) 

# Example 3
root3 = None
print(preorderTraversal(root3))  
# Example 4
root4 = TreeNode(1)
print(preorderTraversal(root4))  


""" Explanation : 
# 
#         __1
#        /
#       2
#      / \
#     3   4
#
#     node     node.left   node.right  stack    ans
#   –––––––––  –––––––––   –––––––––   ––––––  ––––––
#                                       [1]     []
#       1          2         None       [2]     [1]
#       2          3          4         [4,3]   [1,2]
#       3        None        None       [4]     [1,2,3]
#       4        None        None       [4]     [1,2,3,4]
"""


print("==============================================")

#Solution 2


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def preorderTraversal(root):
    def dfs(root):
        if not root:
            return []
        
        return [root.val]+dfs(root.left)+dfs(root.right)
    
    return dfs(root)
    

print("==============================================")

#Solution 3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def preorderTraversal(root):
    if not root:
        return []
    
    l = preorderTraversal(root.left)
    r = preorderTraversal(root.right)

    return [root.val] + l + r



#Explanation : https://chatgpt.com/c/6787bae9-5b3c-800f-a073-6cbcdd8a3a53