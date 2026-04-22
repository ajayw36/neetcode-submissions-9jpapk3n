class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        indices = [i for i in range(len(tasks))]
        indices.sort(key = lambda i : tasks[i][0])
        res = []
        time = tasks[indices[0]][0]
        minHeap = []
        i = 0
        while True:
            if not minHeap and i == len(tasks): return res
            while i < len(indices) and tasks[indices[i]][0] <= time:
                heapq.heappush(minHeap, (tasks[indices[i]][1], indices[i])) # processing time, index
                i += 1
            if minHeap:
                proc_time, index = heapq.heappop(minHeap)
                time += proc_time
                res.append(index)
            else:
                time = tasks[indices[i]][0]

