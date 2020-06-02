# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self,node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = None
        while(node and node.next):
            newVal = node.next.val
            node.val = newVal
            prev = node
            node = node.next
        if prev:
            prev.next = None
        
        
        