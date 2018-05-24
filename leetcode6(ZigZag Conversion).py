# zigzag pattern on a given number
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

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

# zigzag pattern on a given number
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

class MySolution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        group_len = 2 * numRows - 2
        result = []
        index = 0
        for i in range(0, group_len // 2 + 1):
            index = i
            start_index = 0
            while index < len(s):
                if index % (group_len // 2) == 0:
                    result.append(s[index])
                else:
                    #result.extend([s[index], s[start_index + group_len - 1 - index]])
                    result.append(s[index])
                    if 2 * start_index - index + group_len < len(s):
                        result.append(s[2 * start_index - index + group_len])
                index += group_len
                start_index += group_len
                #print(start_index)
        return "".join(result)

if __name__ == "__main__":
    #Solution().convert("PAYPALISHIRING", 4) == True
    print(Solution().convert("PAYPALISHIRING", 4))
    print(MySolution().convert("PAYPALISHIRING", 4))