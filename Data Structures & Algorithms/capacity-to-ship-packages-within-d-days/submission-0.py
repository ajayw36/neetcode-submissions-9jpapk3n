class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(m):
            new_weights = weights[:]
            for day in range(days):
                curr = 0
                while new_weights and curr + new_weights[-1] <= m:
                    curr += new_weights.pop()
            return not new_weights

        l, r = max(weights), sum(weights)
        while l <= r:
            m = (l + r) // 2
            if can_ship(m):
                r = m - 1
            else:
                l = m + 1
        return l