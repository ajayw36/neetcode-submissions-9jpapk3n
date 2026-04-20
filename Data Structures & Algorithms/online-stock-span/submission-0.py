class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int: 
        count = 1
        i = len(self.prices) - 1
        while self.prices and i >= 0 and self.prices[i] <= price:
            count += 1
            i -= 1
        self.prices.append(price)
        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)