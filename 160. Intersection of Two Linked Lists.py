# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def findlen(ll):
            len=1
            curr=ll#headnode
            while curr.next:
                len+=1
                curr=curr.next
            return len
        lenA,lenB=findlen(headA),findlen(headB)
        if lenA>lenB:
            for i in range(lenA-lenB):
                headA=headA.next
        else:
            for i in range(lenB-lenA):
                headB=headB.next
        while headA.next!=headB.next:
            headA=headA.next
            headB=headB.next
        if headA==headB:
            return headA
        else:
            return headA.next
