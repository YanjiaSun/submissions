class Solution:
    def toLowerCase(self, str):
        result = ""
        for c in str:
            if "Z" >= c >= "A":
                result = result + chr(ord(c) + ord("a"))
            else:
                result = result + c
        return result
