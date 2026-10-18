# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def reverse(head):
            prev = None
            while head:
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt
            return prev

        head = reverse(head)
        max_val = head.val
        curr = head

        while curr.next:
            if curr.next.val < max_val:
                curr.next = curr.next.next
            else:
                curr = curr.next
                max_val = curr.val

        return reverse(head)