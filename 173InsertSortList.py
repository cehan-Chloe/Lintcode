class Solution:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    """ 
    def insertionSortList(self, head):
        if not head:
            return head
        dummyNode = ListNode(0)
        dummyNode.next = head
        cur = head
        while cur.next:
            if cur.next.val < cur.val:
                pre = dummyNode
                while pre.next.val < cur.next.val:
                    pre = pre.next
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
            else:
                cur = cur.next
        return dummyNode.next
