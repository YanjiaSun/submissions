


class Solution(object):
    def indexPairs(self, text, words):
        """
        :type text: str
        :type words: List[str]
        :rtype: List[List[int]]
        """
        if not words:
            return []
        result = []
        for word in words:
            starting = [index for index in range(len(text)) if text.startswith(word, index)]
            for start in starting:
                result.append([start, start + len(word) - 1])
            # print starting
        result.sort()
        return result
