


class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head1, head2 = head, slow.next
        slow.next = None
        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        head = self.merge(head1, head2)
        return head

    def merge(self, head1, head2):
        if not head1:
            return head2
        if not head2:
            return head1
        result = ListNode(0)
        p = result
        while head1 and head2:
            if head1.val <= head2.val:
                p.next = ListNode(head1.val)
                head1 = head1.next
                p = p.next
            else:
                p.next = ListNode(head2.val)
                head2 = head2.next
                p = p.next
        if head1:
            p.next = head1
        if head2:
            p.next = head2
        return result.next
