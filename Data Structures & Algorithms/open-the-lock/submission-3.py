class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        
        if '0000' in deadends:
            return -1
        
        q = deque()
        q.append('0000')
        count = 0
        visited = set()

        def children(code):
            res = []
            for i in range(len(code)):
                res.append(code[:i] + str((int(code[i]) + 1) % 10) + code[i+1:])
                res.append(code[:i] + str((int(code[i]) - 1) % 10) + code[i+1:])
            return res

        while q:
            for _ in range(len(q)):
                code = q.popleft()
                if code == target: return count
                for child in children(code):
                    if child not in deadends and child not in visited:
                        q.append(child)
                        visited.add(child)
            count += 1

        return -1

        