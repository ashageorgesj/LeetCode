# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        nextOne = None
        nextnext = None
        middle = None
        if head:
            nextOne = head.next
            if nextOne:
                nextnext = nextOne.next
            else:
                return head
        while nextOne or nextnext:
            if  nextnext is None or nextnext.next is None:
                middle = nextOne
                break
            nextOne = nextOne.next
            count = 0
            while nextnext:
                if count == 2:
                    break
                nextnext = nextnext.next
                count += 1
        return middle
            