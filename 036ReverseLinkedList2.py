"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    def reverseLinkedList(self, cur_start, cur_end):
        cur = None
        while cur_start != None and cur_start != cur_end:
            tmp = cur_start.next
            cur_start.next = cur
            cur = cur_start
            cur_start = tmp
        cur_start.next = cur
        return cur_start
    
    def reverseBetween(self, head, m, n):
        if head is None and head.next is None:
            return head
        # dummy = ListNode(-1, head) is more simple
        dummyHead = ListNode(-1)
        dummyHead.next = head
        # to avoid the situation that m is 1
        pre = dummyHead
        
        for i in xrange(m-1):
            pre = pre.next
        cur_start = pre.next
        cur_end = cur_start
        
        for i in xrange(n-m):
            cur_end = cur_end.next
        end = cur_end.next
        cur_start = self.reverseLinkedList(cur_start, cur_end)
        
        tmp = cur_start
        while tmp.next:
            tmp = tmp.next
        cur_end = tmp
        
        pre.next = cur_start
        cur_end.next = end
        return dummyHead.next
        
        
        
        
            
        

