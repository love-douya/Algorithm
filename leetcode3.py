class Solution:
    def lengthOfLongestSubstring(self, s):
        substr = ""
        max_ = 0
        d = {}
        for i in range(len(s)):
            if s[i] not in substr:
               substr += s[i]
            else:
                substr = s[d[s[i]] + 1 : i + 1]
            max_ = max(max_, len(substr))
            d[s[i]] = i
            #d.update({s[i] : i})
        return max_

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abdfakiad"))