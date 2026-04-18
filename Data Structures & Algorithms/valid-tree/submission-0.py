class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)}
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)    
        
        path = set()
        def detect_cycle(i, parent):
            if i in path:
                return True            
            path.add(i)
            for j in graph[i]:
                if j == parent:
                    continue
                if detect_cycle(j, i):
                    return True
            return False
        
        return not detect_cycle(0, -1) and len(path) == n