# Stack of Stacks
from collections import defaultdict
class FreqStack:
    def __init__(self):
        self.stacks = [[]]
        self.counts = defaultdict(int)

    def push(self, val: int) -> None:
        self.counts[val] += 1
        if self.counts[val] == len(self.stacks):
            self.stacks.append([val])
        else:
            self.stacks[self.counts[val]].append(val)

    def pop(self) -> int:
        top_element = self.stacks[-1].pop()
        if not self.stacks[-1]:
            self.stacks.pop()
        self.counts[top_element] -= 1
        return top_element



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()