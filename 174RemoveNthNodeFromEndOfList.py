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
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        if head is None: return None
        dummyHead = ListNode(0)
        dummyHead.next = head
        fast = slow = dummyHead
        for i in range(n): fast = fast.next
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummyHead.next 
