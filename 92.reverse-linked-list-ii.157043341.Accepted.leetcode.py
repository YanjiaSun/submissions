class Solution(object):
    def reverseBetween(self, head, m, n):
        dummy = ListNode(-1)
        dummy.next = head
        prevM = dummy
        for index in range(1, n + 1):
            if index < m:
                prevM = prevM.next
            elif index == m:
                pre = prevM.next
                head = pre.next
            else:
                temp = head.next
                head.next = pre
                pre = head
                head = temp
        prevM.next.next = head
        prevM.next = pre
        return dummy.next
