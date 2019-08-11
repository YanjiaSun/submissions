class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        word_len = len(words[0])
        word_total = len(words) * word_len
        ans = []
        word_cnt = collections.Counter(words)
        rangeEnd = len(s) - word_total + 1
        for i in range(min(word_len, rangeEnd)):
            start = i
            cur_cnt = collections.Counter()
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j: j + word_len]
                if word in word_cnt:
                    cur_cnt[word] += 1
                    while cur_cnt[word] > word_cnt[word]:
                        cur_cnt[s[start: start + word_len]] -= 1
                        start += word_len
                else:
                    cur_cnt.clear()
                    start = j + word_len
                if(start + word_total == j):
                    ans.append(start)
        return ans
