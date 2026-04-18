class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate_0, candidate_1 = nums[0], nums[0]
        count_0, count_1 = 0, 0
        for i in range(len(nums)):
            if nums[i] == candidate_0:
                count_0 += 1
            elif nums[i] == candidate_1:
                count_1 += 1
            elif count_0 == 0:
                candidate_0 = nums[i]
                count_0 = 1
            elif count_1 == 0:
                candidate_1 = nums[i]
                count_1 = 1
            else:
                count_0 -= 1
                count_1 -= 1
        
        count_0, count_1 = 0, 0
        for num in nums:
            if num == candidate_0:
                count_0 += 1
            elif num == candidate_1:
                count_1 += 1
        res = []
        if count_0 > math.floor(len(nums) / 3):
            res.append(candidate_0)
        if count_1 > math.floor(len(nums) / 3):
            res.append(candidate_1)
        return res

