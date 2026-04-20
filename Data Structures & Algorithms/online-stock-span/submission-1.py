class StockSpanner:

    def __init__(self):
        self.stack = [(float('inf'), 0)]
        self.day = 0

    def next(self, price: int) -> int:
        self.day += 1
        while price >= self.stack[-1][0]:
            self.stack.pop()
        days = self.day - self.stack[-1][1]
        self.stack.append((price, self.day))
        return days
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)