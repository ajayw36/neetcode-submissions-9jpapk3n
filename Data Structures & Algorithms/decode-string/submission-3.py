class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == ']':
                t = ''
                while stack[-1] != '[':
                    t = stack.pop() + t
                stack.pop()
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                num = int(num)
                stack.append(t * num) 
            else:
                stack.append(ch)
        return ''.join(stack)
