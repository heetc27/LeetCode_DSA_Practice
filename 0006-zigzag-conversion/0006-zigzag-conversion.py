class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]
        row = 0
        direction = 1
        for char in s:
            rows[row].append(char)
            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = -1
            row += direction
        return "".join("".join(row) for row in rows)