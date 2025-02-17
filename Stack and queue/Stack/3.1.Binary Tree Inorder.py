#Problem : https://leetcode.com/problems/binary-tree-inorder-traversal/description/?envType=problem-list-v2&envId=stack



#Solution 1:

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root: TreeNode):
    result = []
    
    def dfs(node):
        if node:
            dfs(node.left)  # Traverse left subtree
            result.append(node.val)  # Visit node
            dfs(node.right)  # Traverse right subtree
            
    dfs(root)
    return result

# Construct the tree: [1,2,3,4,5,null,8,null,null,6,7,9]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)
root.right.right.left = TreeNode(9)

print(inorderTraversal(root))  # Output: [4, 2, 6, 5, 7, 1, 3, 9, 8]



print("=========================================================")

#Solution 2

def inorderTraversal(self, root):
    res = []
    self.helper(root, res)
    return res

def helper(self, root, res):
    if root is not None:
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)




print("================================================")

#Solution 3
def inorderTraversal(root):
        result = []
        stack = []
        current = root

        # Traverse the tree
        while current or stack:
            # Reach the leftmost node of the current node
            while current:
                stack.append(current)
                current = current.left

            # Current must be None at this point, pop the stack
            current = stack.pop()
            result.append(current.val)  # Add the node value to result

            # We have visited the node and its left subtree, now go to the right subtree
            current = current.right

        return result
    
    

print("================================================")

#Solution 4:

def inorderTraversal(root):
        st = []
        res = []

        while root or st:
            while root:
                st.append(root)
                root = root.left
            
            root = st.pop()
            res.append(root.val)

            root = root.right
        
        return res   



#Explanation : https://chatgpt.com/c/6788ed67-8b00-800f-b1e7-d4e629ad4dc1
