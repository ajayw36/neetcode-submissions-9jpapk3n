class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        for p in path:
            if p == '..':
                if stack:
                    stack.pop()
            elif p != '' and p != '.':
                stack.append(p)
        s = '/'.join(stack)
        return '/' + s