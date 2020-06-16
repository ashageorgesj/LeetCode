#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3361/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        current = root
        if current and current.val == val:
            return current
        while (current):
            #print(current.val)
            if current.val == val:
                return current
            elif val < current.val:
                current = current.left 
            elif val > current.val:
                current = current.right
        return None