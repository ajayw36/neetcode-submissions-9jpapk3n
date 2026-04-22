class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        minHeap = [] 
        res = []
        tasks = [(tasks[i][0], tasks[i][1], i) for i in range(len(tasks))]
        tasks.sort()
        time = tasks[0][0]
        index = 0
        while True:
            if index == len(tasks) and not minHeap: break
            while index < len(tasks) and tasks[index][0] <= time:
                heapq.heappush(minHeap, (tasks[index][1], tasks[index][2]))
                index += 1
            if minHeap:
                processingTime, i = heapq.heappop(minHeap)
                time += processingTime
                res.append(i)
            else:
                time = tasks[index][0]
        return res