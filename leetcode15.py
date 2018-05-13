class Solution1:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        d = dict()
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        
        for i, value in enumerate(nums):
            

if __name__ == "__main__":
    print(Solution1().threeSum(input("Please input nums: ")))
