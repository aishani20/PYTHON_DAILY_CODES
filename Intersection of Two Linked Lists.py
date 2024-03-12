# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr1=headA
        curr2=headB

        lenA=0
        while curr1:
            lenA+=1
            curr1=curr1.next

        lenB=0
        while curr2:
            lenB+=1
            curr2=curr2.next
        
        difference=abs(lenA-lenB)

        while difference:
            if lenA>lenB:
                while difference>0:
                      headA = headA.next
                      difference -= 1
            else:
                while difference > 0:
                    headB = headB.next
                    difference -= 1

        while headA and headB:
            if headA == headB:
                return headA
            headA=headA.next
            headB=headB.next
        
        return None



