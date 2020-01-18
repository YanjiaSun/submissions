class Solution(object):
    def toLowerCase(self, str):
        res = []
        gap = ord('a') - ord('A')
        for c in str:
            if ord(c) >= ord('A') and ord(c) <= ord('Z'):
                res.append(chr(ord(c) + gap))
            else:
                res.append(c)
        return ''.join(res)
