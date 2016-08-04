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
        dummyNode = ListNode(-1)
        # at first, the establish of connection of head and dummyNode is ignored
        dummyNode.next = head
        pre = dummyNode
        cur = head
        while cur and cur.next:
            cur_val = cur.val
            if cur_val != cur.next.val:
                pre = pre.next
                cur = cur.next
            else:
                while cur.next != None and cur.next.val == cur_val:
                    cur = cur.next
                cur = cur.next
                pre.next = cur
        return dummyNode.next
