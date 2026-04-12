class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        map = {}
        map[2] = ['a', 'b', 'c']
        map[3] = ['d', 'e', 'f']
        map[4] = ['g', 'h', 'i']
        map[5] = ['j', 'k', 'l']
        map[6] = ['m', 'n', 'o']
        map[7] = ['p', 'q', 'r', 's']
        map[8] = ['t', 'u', 'v']
        map[9] = ['w', 'x', 'y', 'z']

        res = []
        curr = []
        def backtrack(n):
            if n == len(digits):
                res.append(''.join(curr))
                return
            for char in map[int(digits[n])]:
                curr.append(char)
                backtrack(n+1)
                curr.pop()
        
        backtrack(0)
        return res