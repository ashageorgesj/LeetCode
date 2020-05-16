# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        oddVal = []
        evenVal = []
        current = head
        odd = True
        while current:
            if odd:
                oddVal.append(current.val)
                odd = False
            else:
                evenVal.append(current.val)
                odd = True
            current = current.next
        current = head
        odd = True
        oddIndex = 0
        evenIndex = 0
        while current:
            if odd:   
                if oddIndex < len(oddVal):
                    current.val = oddVal[oddIndex]
                    current = current.next
                else:
                    odd = False
                oddIndex += 1
            else:
                if evenIndex < len(evenVal):
                    current.val = evenVal[evenIndex]
                    current = current.next
                    evenIndex += 1
                else:
                    break
        return head
                    
