import ctypes
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        

if __name__ == "__main__":
    raw_number = input("Input number: ")
    modified_number = ctypes.c_long(raw_number & 0xFFFFFFFF).value
    print(Solution().reverse(modified_number))