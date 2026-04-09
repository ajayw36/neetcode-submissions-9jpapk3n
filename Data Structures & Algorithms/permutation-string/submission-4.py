class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        f1 = [0] * 26
        f2 = [0] * 26
        for ch in s1:
            f1[ord(ch)-ord('a')] += 1
        i = j = 0
        while j < len(s2):
            f2[ord(s2[j])-ord('a')] += 1
            while f2[ord(s2[j])-ord('a')] > f1[ord(s2[j])-ord('a')]:
                f2[ord(s2[i])-ord('a')] -= 1
                i += 1
            if f2 == f1:
                return True
            j += 1
        return False