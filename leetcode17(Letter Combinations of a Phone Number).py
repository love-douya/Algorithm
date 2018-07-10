class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'0': [' '], '1': [''], '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
    
        result = ['']
        if not digits:
            return []
        else:
            # for i in digits:
            #     for j in dic[i]:
            #         for k in result:
            #             [k + j]
            for i in digits:
                result = [k + j for j in dic[i] for k in result]
            return result

class Solution1:
    def letterCombinations(self, digits):
        dict_num = { '1': '', '2': 'abc', '3': 'def',
        '4': 'ghi', '5': 'jkl', '6': 'mno',
        '7': 'pqrs','8': 'tuv', '9': 'wxyz',
        '0': ' '}
        if not digits:
            return []
        else:
            answer = ['']
            for i in digits:
                answer = [b+a for a in dict_num[i] for b in answer] 
            return answer

if __name__ == '__main__':
    print(Solution().letterCombinations(input('Input the phone number: ')))