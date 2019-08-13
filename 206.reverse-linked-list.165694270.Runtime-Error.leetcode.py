class Solution(object):
    def reverseList(self, head):
        prev = None
        while head.next:
            temp = head.next
            head.next = prev
            head = temp
            prev = head
        return prev
