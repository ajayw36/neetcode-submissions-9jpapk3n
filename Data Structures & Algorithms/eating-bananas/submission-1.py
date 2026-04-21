class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        def can_eat(speed):
            count = 0
            for pile in piles:
                if count > h: return False
                count += math.ceil(pile / speed)
            return count <= h


        while l < r:
            m = (l + r) // 2
            if can_eat(m):
                r = m
            else:
                l = m + 1
        
        return l