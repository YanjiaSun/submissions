class Solution(object):
    def verifyPreorder(self, preorder):
        minV = -sys.maxint - 1
        stack = [sys.maxint]

        for num in preorder:

            while stack[-1] < num:
                minV = stack.pop()
            stack.append(num)

        return True
