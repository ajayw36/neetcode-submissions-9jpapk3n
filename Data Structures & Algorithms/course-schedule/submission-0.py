class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # setting up our graph
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # algorithm to detect cycle
        path = set()
        def detect_cycle(crs):
            if crs in path:
                return True
            if preMap[crs] == []:
                return False

            path.add(crs)
            for pre in preMap[crs]:
                if detect_cycle(pre):
                    return True
            path.remove(crs)
            preMap[crs] = []
            return False
        
        for i in range(numCourses):
            if detect_cycle(i):
                return False
        return True
            