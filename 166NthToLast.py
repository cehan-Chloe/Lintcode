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
    @param n: An integer.
    @return: Nth to last node of a singly linked list. 
    """
    def nthToLast(self, head, n):
        if not head:
            return head
        dummyHead = ListNode(0)
        dummyHead.next = head
        phead = ptail = dummyHead
        for i in range(n): ptail = ptail.next
        while ptail.next is not None:
            phead = phead.next
            ptail = ptail.next
        return phead.next
     
       
