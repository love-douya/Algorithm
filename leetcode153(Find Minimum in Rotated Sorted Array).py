class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0, len(nums) - 1):
            if nums[i + 1] < nums[i] + 1:
                return nums[i + 1]
        return nums[0]

if __name__ == "__main__":
    print(Solution().findMin(list(map(int, input("Input list: ")))))