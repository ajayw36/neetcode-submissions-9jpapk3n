class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = 1
        seen = set()
        seen.add(1)
        for num in nums:
            seen.add(num)
            if num == res:
                while res in seen:
                    res += 1
        return res