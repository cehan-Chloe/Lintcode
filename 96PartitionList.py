"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param x: an integer
    @return: a ListNode 
    """
    def partition(self, head, x):
        if head is None:
            return head
        dummyHead1 = ListNode(0)
        p1 = dummyHead1
        dummyHead2 = ListNode(0)
        p2 = dummyHead2
        while head is not None:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else: 
                p2.next = head
                p2 = p2.next
            head = head.next
        p2.next = None #reason? if no this statement there would cause an error
        p1.next = dummyHead2.next
        return dummyHead1.next
