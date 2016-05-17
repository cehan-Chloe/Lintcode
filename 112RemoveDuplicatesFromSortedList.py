"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        dummyHead = ListNode(0)
        pdummy = dummyHead
        pdummy.next = head
        head = head.next
        pdummy = pdummy.next
        while head:
            if head.val == pdummy.val:
                head = head.next
                continue
            else:
                pdummy.next = head
                head = head.next
                pdummy = pdummy.next
        pdummy.next = None
        return dummyHead.next
