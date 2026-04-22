class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                prev, prev_i = stack.pop()
                res[prev_i] = i - prev_i
            stack.append((temperature, i))
        return res
        
            