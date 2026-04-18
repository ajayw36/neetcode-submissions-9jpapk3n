class Solution:
    def merge(self, nums1, nums2):
            merged = []
            i = j = 0
            while i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    merged.append(nums1[i])
                    i += 1
                else:
                    merged.append(nums2[j])
                    j += 1
            while i < len(nums1):
                merged.append(nums1[i])
                i += 1
            while j < len(nums2):
                merged.append(nums2[j])
                j += 1
            return merged

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        return self.merge(self.sortArray(nums[:len(nums)//2]), self.sortArray(nums[len(nums)//2:]))
        
            