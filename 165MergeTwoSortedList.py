"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2: 
            return l1
        dummyHead = ListNode(0)
        p = dummyHead
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if not l1:
            p.next = l2
        if not l2:
            p.next = l1
        return dummyHead.next
