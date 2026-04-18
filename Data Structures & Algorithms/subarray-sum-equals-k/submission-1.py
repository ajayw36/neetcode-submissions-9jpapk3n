from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefs = defaultdict(int)
        prefs[0] = 1
        curr_sum = res = 0
        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            res += prefs[diff]
            prefs[curr_sum] += 1
        return res