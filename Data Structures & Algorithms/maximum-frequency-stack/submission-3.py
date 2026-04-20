class FreqStack:

    def __init__(self):
        self.heap = []
        self.counts = defaultdict(int)
        self.index = 0

    def push(self, val: int) -> None:
        self.counts[val] += 1
        freq = self.counts[val]
        heapq.heappush(self.heap, (-freq, -self.index, val))
        self.index += 1

    def pop(self) -> int:
        _, _, val = heapq.heappop(self.heap)
        self.counts[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()