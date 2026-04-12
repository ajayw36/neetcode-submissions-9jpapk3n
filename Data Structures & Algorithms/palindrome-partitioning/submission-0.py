class Solution:
    def partition(self, s: str) -> List[List[str]]:
        curr = []
        res = []
        def palindrome(string):
            i, j = 0, len(string) - 1
            while i < j:
                if string[i] != string[j]:
                    return False
                i += 1
                j -= 1
            return True

        def backtrack(j, i):
            if i == len(s):
                if j == len(s):
                    res.append(curr[:])
                return
            backtrack(j, i + 1)

            if palindrome(s[j:i+1]):
                curr.append(s[j:i+1])
                backtrack(i + 1, i + 1)
                curr.pop()
        
        backtrack(0, 0)
        return res
            

            