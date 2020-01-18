class Solution:
    def mostCommonWord(self, paragraph, banned):
        import re
        from collections import Counter
        d = Counter([word.lower() for word in re.split(r'\W+', paragraph) if word and word.lower() not in banned]).most_common(1)
        return d[0][0]
