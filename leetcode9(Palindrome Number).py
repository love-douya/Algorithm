class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_reverse_str= str(x)[::-1]
        if x_reverse_str == str(x):
            return True
        else:
            return False

if __name__ == "__main__":
    print(Solution().isPalindrome(input("Input a number: ")))