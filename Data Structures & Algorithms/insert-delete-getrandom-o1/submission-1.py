class RandomizedSet:

    def __init__(self):
        self.elts = []
        self.map = {}
        

    def insert(self, val: int) -> bool:
        if val in self.map: return
        self.elts.append(val)
        self.map[val] = len(self.elts) - 1
        

    def remove(self, val: int) -> bool:
        if val not in self.map: return
        i = self.map[val]
        j = len(self.elts) - 1
        val2 = self.elts[j]
        self.elts[i], self.elts[j] = self.elts[j], self.elts[i]
        self.elts.pop()
        self.map[val2] = i
        del self.map[val]

    def getRandom(self) -> int:
        i = random.randint(0, len(self.elts) - 1)
        return self.elts[i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()