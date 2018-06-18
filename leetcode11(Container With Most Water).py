class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = []
        i = 0
        j = len(height) - 1
        while j > i:
            if height[i] > height[j]:
                l.append(height[j] * (j - i))
                j -= 1
            else:
                l.append(height[i] * (j - i))
                i += 1
        return max(l)

if __name__ == "__main__":
    print(Solution().maxArea(list(map(int, input("Input List: ")))))