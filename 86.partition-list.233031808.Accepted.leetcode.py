
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        left, right = ListNode(0), ListNode(0)
        leftPtr, rightPtr = left, right
        while head:
            if head.val < x:
                leftPtr.next = ListNode(head.val)
                leftPtr = leftPtr.next
            else:
                rightPtr.next = ListNode(head.val)
                rightPtr = rightPtr.next
            head = head.next
        if not left.next:
            return right.next
        elif not right.next:
            return left.next
        else:
            leftPtr.next = right.next
            return left.next
# Time: O(N)
# Space: O(N)
