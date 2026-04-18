from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = [False] * n
        count = 0
        def dfs(i):
            visited[i] = True
            for j in graph[i]:
                if not visited[j]:
                    dfs(j)
        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)
        return count