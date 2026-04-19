class MyHashSet:
    class ListNode:
        def __init__(self, key):
            self.key = key
            self.next = None

    def __init__(self):
        self.table = [self.ListNode(0) for i in range(10000)]

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        curr = self.table[key%10000]
        while curr.next != None:
            curr = curr.next
        curr.next = self.ListNode(key)

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        prev = self.table[key%10000]
        curr = prev.next
        while curr.key != key:
            curr = curr.next
            prev = prev.next
        prev.next = curr.next

    def contains(self, key: int) -> bool:
        curr = self.table[key%10000].next
        while curr != None:
            if curr.key == key:
                return True
            curr = curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)