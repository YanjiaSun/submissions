class Trie(object):
    class TrieNode(object):
        def __init__(self, content=' '):
            self.content = content
            self.isWord = False
            self.nexts = {}

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word):
        if self.search(word):
            return
        current = self.root
        for i in range(0, len(word)):
            c = word[i]
            node = current.nexts.get(c, None)
            if not node:
                current.nexts[c] = self.TrieNode(c)
                node = current.nexts.get(c, None)
            current = node
        current.isWord = True

    def search(self, word):
        current = self.root
        for i in range(0, len(word)):
            node = current.nexts.get(word[i], None)
            if not node:
                return False
            current = node
        return current.isWord

    def startsWith(self, prefix):
        current = self.root
        for i in range(0, len(prefix)):
            node = current.nexts.get(prefix[i], None)
            if not node:
                return False
            current = node
        return True
