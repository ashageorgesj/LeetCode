# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        values = []
        
        if root:
            values = self.traverse(root,values,k)
        if (k-1) < len(values):
            return values[k - 1]
            
    def traverse(self,current:TreeNode,values:List[int],k:int) -> List[int]:
        if current:
            values = self.traverse(current.left,values,k)
            values.append(current.val)
            if len(values) == k:
                return values
            values = self.traverse(current.right,values,k)
        return values
                
