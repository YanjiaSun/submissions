import string


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        # two way bfs
        # one way is not sufficient
        wordList.discard(beginWord)
        wordList.discard(endWord)
        hash_map, res = {}, []
        res = self.bfs(set([beginWord]), set([endWord]), wordList, 2)
        return res

    def bfs(self, forward, backward, wordlist, level):
        if len(forward) == 0 or len(backward) == 0:
            return 0
        if len(forward) > len(backward):
            return self.bfs(backward, forward, wordlist, level)
        is_connected = False
        next_level = set()
        for word in forward:
            for c in string.ascii_lowercase:
                for index in range(len(word)):
                    neigh = word[:index] + c + word[index + 1:]
                    if neigh in backward:
                        is_connected = True
                        return level
                    if not is_connected and neigh in wordlist:
                        next_level.add(neigh)
                        wordlist.discard(neigh)
        if not is_connected:
            return self.bfs(next_level, backward, wordlist, level + 1)


if __name__ == "__main__":
    s = Solution()