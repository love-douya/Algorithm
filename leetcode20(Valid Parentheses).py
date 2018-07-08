class Solution(object):
    def isValid(self, s):
        input_list = list(s)
        stack = []
        while input_list:
            a = input_list.pop()
            if a == ')' or a == ']' or a == '}':
                stack.append(a)
            else:
                if stack:
                    b = stack.pop()
                    if not self.isMatch(a, b):
                        return False
                else:
                    return False       

        if stack:
            return False
        else:
            return True

    def isMatch(self, key, value):
        dic = { '(' : ')' , '[' : ']' , '{' : '}' }
        if dic[key] != value:
            return False
        else:
            return True

if __name__ == '__main__':
    print(Solution().isValid(input('Input String: ')))