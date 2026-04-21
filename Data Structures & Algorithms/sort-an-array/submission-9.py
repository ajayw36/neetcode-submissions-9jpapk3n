class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums1, nums2):
            i = j = 0
            res = []
            while i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    res.append(nums1[i])
                    i += 1
                else:
                    res.append(nums2[j])
                    j += 1
            while i < len(nums1):
                res.append(nums1[i])
                i += 1
            while j < len(nums2):
                res.append(nums2[j])
                j += 1
            return res
        def mergesort(nums):
            if len(nums) <= 1:
                return nums
            m = len(nums) // 2
            nums1, nums2 = mergesort(nums[:m]), mergesort(nums[m:])
            return merge(nums1, nums2)
        return mergesort(nums)

