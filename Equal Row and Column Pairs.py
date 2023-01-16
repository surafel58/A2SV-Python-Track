class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        pairCounter = 0
        rowFreq = defaultdict(int)
        colFreq = defaultdict(int)

        n = len(grid)
        m = len(grid[0])

        for row in range(n):
            rowValues = []
            for col in range(m):
                rowValues.append(grid[row][col])

            rowFreq[tuple(rowValues)] += 1

        for col in range(m):
            colValues = []
            for row in range(n):
                colValues.append(grid[row][col])

            colFreq[tuple(colValues)] += 1

        for rowValues in rowFreq:
            if rowValues in colFreq:
                pairCounter += rowFreq[rowValues] * colFreq[rowValues]
       
        return pairCounter
