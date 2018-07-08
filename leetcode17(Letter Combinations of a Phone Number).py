class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        phone_number = list(digits).remove('0').remove('1')
        result = []
        string = None
        for i in phone_number:
            for j in dic[i]:
                for k in phone_number:
                    result.append(string + j)

        return result

if __name__ == '__main__':
    print(Solution().letterCombinations(input('Input the phone number: ')))