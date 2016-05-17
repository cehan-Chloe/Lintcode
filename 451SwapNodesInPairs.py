# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None is None:
            return head
        dummyHead = ListNode(0)
        dummyHead.next = head
        slow = dummyHead
        fast = dummyHead.next
        while fast.next is not None:
            slow.next = fast.next
            fast.next = slow.next.next
            slow.next.next = fast
            if fast.next is not None:
                fast = slow.next
                slow = slow.next.next
                fast = fast.next.next
        return dummyHead.next
