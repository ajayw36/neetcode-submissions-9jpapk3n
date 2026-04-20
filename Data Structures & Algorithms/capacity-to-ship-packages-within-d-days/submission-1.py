class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(m):
            ships = 1
            curr = 0
            for i in range(len(weights)):
                if curr + weights[i] <= m:
                    curr += weights[i]
                else:
                    curr = weights[i]
                    ships += 1
                    if ships > days:
                        return False
            return True

        l, r = max(weights), sum(weights)
        while l <= r:
            m = (l + r) // 2
            if can_ship(m):
                r = m - 1
            else:
                l = m + 1
        return l