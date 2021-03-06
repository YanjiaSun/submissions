class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        a, b = headA, headB
        while a or b:
            if not a:
                a = headB
            if not b:
                b = headA
            if a == b:
                return a
            a, b = a.next, b.next
