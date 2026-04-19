class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        seen = set()
        i = j = 0
        while j <= k and j < len(nums):
            if nums[j] in seen:
                return True
            seen.add(nums[j])
            j += 1
        
        while j < len(nums):
            seen.remove(nums[i])
            i += 1
            if nums[j] in seen:
                return True
            seen.add(nums[j])
            j += 1   

        return False
        