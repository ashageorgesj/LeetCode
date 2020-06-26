#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3372
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        total = 0
        stack = []
        if root:
            stack.append((root,str(root.val)))
        while len(stack) > 0:
            current,strSum = stack.pop()
            if not current.right and not current.left:
                total += int(strSum)
            else:
                if current.right:
                    stack.append((current.right , strSum + str(current.right.val)))
                if current.left:
                    stack.append((current.left, strSum + str(current.left.val)))
        return total