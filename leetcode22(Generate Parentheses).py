import sys

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def dfs(res, n, s, left, right) :
            if right == n : res.append(s)
            if left < n :
                dfs(res, n, s + "(", left+1, right)
            if left > right :
                dfs(res, n, s + ")", left, right+1)
        dfs(res, n, '', 0, 0)
        return res

if __name__ == '__main__':
    print('Result is: {0}'.format(Solution().generateParenthesis(int(input('Input number of parentheses pairs: ')))))