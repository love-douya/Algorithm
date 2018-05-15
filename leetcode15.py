import sys
import string

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
        s = list(set(nums))
        s.sort()
        res = set()
        for i, a in enumerate(s):
            d[a] -= 1
            for b in s[i:]:
                if d[b] == 0:
                    continue
                c = - a - b
                if c >= b and c in d and d[c] > (1 if c == b else 0):
                    res.add((a, b, c))
            d[a] = d[a] + 1
        return list(res)
 
if __name__ == "__main__":
    nums = []
    print("Input nums: ")
    nums = list(map(int, sys.stdin.readlines().strip().split()))
    print(Solution1().threeSum(nums))
