# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head and not head.next:
            return

        slow = fast = head
        prev = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            
        curr = slow.next
        slow.next = prev

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        first = head
        sec = prev

        while sec:
            t1 = first.next
            t2 = sec.next

            first.next = sec
            sec.next = t1

            first = t1
            sec = t2

