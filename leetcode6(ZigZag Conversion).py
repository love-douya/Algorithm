class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s): 
            return s
        row, direction, res = 0, -1, [""] * numRows
        for char in s:
            res[row] += char
            if row == 0 or row == numRows - 1: 
                direction *= -1 
            row += direction
        return "".join(res)

class MySolution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        group_len = 2 * numRows - 2
        result = []
        index = 0
        for i in range(0, group_len):
            index = i
            while index < len(s):
                result.append(s[index])
                index += group_len
        return "".join(result)


if __name__ == "__main__":
    #Solution().convert("PAYPALISHIRING", 4) == True
    print(Solution().convert("PAYPALISHIRING", 4))
    print(MySolution().convert("PAYPALISHIRING", 4))