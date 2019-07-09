_author_ = 'jake'
_project_ = 'leetcode'








class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard = {}
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        for i, row in enumerate(rows):
            for c in row:
                keyboard[c] = i
        result = []
        for word in words:
            row = -1
            for c in word:
                if row == -1:
                    row = keyboard[c.lower()]
                elif keyboard[c.lower()] != row:
                    break
            else:
                result.append(word)
        return result