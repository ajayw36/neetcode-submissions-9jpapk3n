class Solution:
    def checkValidString(self, s: str) -> bool:
        lstack = []
        sstack = []
        for i in range(len(s)):
            if s[i] == '(':
                lstack.append(i)
            elif s[i] == '*':
                sstack.append(i)
            else:
                if lstack:
                    lstack.pop()
                elif sstack:
                    sstack.pop()
                else:
                    return False
        while lstack and sstack:
            if sstack.pop() < lstack.pop():
                return False
        
        return not lstack