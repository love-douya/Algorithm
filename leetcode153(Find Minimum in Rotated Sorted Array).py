class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in len(nums) - 1:
            if nums[i + 1] != nums[i] + 1:
                return nums[i + 1]
            else:
                return False 

if __name__ == "__main__":
    print(Solution().findMin(list(map(int, input("Input list: ")))))