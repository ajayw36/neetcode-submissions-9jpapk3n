class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        seen = set()
        for j in range(len(nums)):
            if j - i > k:
                seen.remove(nums[i])
                i += 1
            if nums[j] in seen:
                return True
            seen.add(nums[j])
        return False
        
        