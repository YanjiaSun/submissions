class Solution:
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        c = Solution.getRow(self, rowIndex - 1)
        newrow = []
        gauche = [0] + c
        droite = c + [0]
        for i in range(len(gauche)):
            newrow.append(gauche[i] + droite[i])
        return newrow
