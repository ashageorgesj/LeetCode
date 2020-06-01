# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        stack = []
        stack.append(root)
        while len(stack) > 0:
            current = stack.pop()
            left = current.left
            temp = left
            right = current.right
            #if right:
            current.left = right
            current.right = temp
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        return root
                