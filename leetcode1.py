#!/usr/local/bin/python3
#Time limit exceed
class Solution1:
    def twoSum(self, nums, target):
        result = []
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if int(nums[i]) + int(nums[j]) == int(target):
                    result.extend([i, j])
        return result

class Solution2:
    def twoSum(self, nums, target):
        visited = {}
        for i in range(0, len(nums)):
            if int(target) - int(nums[i]) in visited:
                return [visited[int(target) - int(nums[i])], i]
            else:
                visited[int(nums[i])] = i

if __name__ == "__main__":
    print(Solution2().twoSum(input("Please input nums: "), input("Please input target: ")))

        