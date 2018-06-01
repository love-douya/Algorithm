#Recursion Version
class Solution_C:
    def isMatch(self, s, p):
        if p == None:
            return s == None
        if len(p) == 1:
            return (len(s) == 1) and (s[0] == p[0] or p[0] == '.')
        if p[1] != '*':
            if s == None:
                return False
            return (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])
        while s != None and (s[0] ==p[0] or p[0] == '.'):
            if self.isMatch(s, p[2:]):
                return True
            s = s[1:]
        return self.isMatch(s, p[1:]) 

class Char:
    def __init__(self, char, repeat=False):
        self.char = char
        self.repeat = repeat
        self.wildcard = (char == ".")

    def __repr__(self):
        return str((self.char, self.repeat))

    def match(self, char):
        return self.wildcard or self.char == char

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        chars = []

        i = 0
        while i < len(p):
            if (i < len(p)-1) and (p[i+1] == "*"):
                chars.append(Char(p[i], True))
                i += 1
            else:
                chars.append(Char(p[i]))
            i += 1

        # Speeds things up a lot checking from the end of the string first
        while len(chars) > 0 and len(s) > 0 and not chars[-1].repeat:
            if not chars[-1].match(s[-1]):
                return False

            chars = chars[:-1]
            s = s[:-1]


        # The number of total repeats must be the #s - #non-repeated-characters
        repeats = len(s) - sum([1 for x in chars if not x.repeat])

        return self.test_patterns(chars, repeats, s)


    def test_patterns(self, chars, repeats, string):
        # Base cases
        if repeats < 0:
            return False
        if len(chars) == 0:
            return len(string) == 0
        if len(string) == 0:
            return (len(chars) == 0) or all([c.repeat for c in chars])

        char = chars[0]

        if char.repeat:
            # Test the branch where the current char is repeatable but skipped
            if self.test_patterns(chars[1:], repeats, string):
                return True

            # Test the branch where the current char is repeatable and used
            if char.match(string[0]) and self.test_patterns(chars, repeats-1, string[1:]):
                return True

        # Test the branch where the current char is not repeatable and thus must be used
        return char.match(string[0]) and self.test_patterns(chars[1:], repeats, string[1:])

if __name__ == "__main__":
    print(Solution().isMatch("abcaaad", "abca*d"))
    #print(Solution_C().isMatch("abcaad", "abca*"))