class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        list3 = []
        len1 = len(nums1) - 1
        len2 = len(nums2) - 1
        len3 = len1 + len2 + 2
        i = 0
        j = 0
        while i <= len1 and j <= len2:
            if nums1[i] <= nums2[j]:
                list3.append(nums1[i])
                i += 1
            else:
                list3.append(nums2[j])
                j += 1
        while i <= len1:
            list3.append(nums1[i])
            i += 1
        while j <= len2:
            list3.append(nums2[j])
            j += 1
        if len3 % 2 == 0:
            median = (list3[int(len3 / 2 - 1)] + list3[int(len3 / 2)]) / 2
        else:
            median = list3[len3 // 2]
        return median

if __name__ == "__main__":
    nums1 = list(map(int, input("Input Sorted List1: ")))
    nums2 = list(map(int, input("Input Sorted List2: ")))
    print(Solution().findMedianSortedArrays(nums1, nums2))