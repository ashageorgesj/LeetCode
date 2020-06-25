#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3369/
import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        
        q = collections.deque()
        count = 0
        if root:
            count += 1
            q.append(root)
        while(len(q) > 0):
            current = q.popleft()
            #print(current.val,count)
            if current.left:
                count += 1
                q.append(current.left)
            if current.right:
                count += 1
                q.append(current.right)
        
        return count
                
