class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.table = [ListNode(0, 0) for _ in range(10**3)]

    def put(self, key: int, value: int) -> None:
        index = key % 10**3
        curr = self.table[index]
        while curr.next != None:
            curr = curr.next
            if curr.key == key:
                curr.value = value
                return
        curr.next = ListNode(key, value)
        

    def get(self, key: int) -> int:
        index = key % 10**3
        curr = self.table[index]
        while curr.next != None:
            curr = curr.next
            if curr.key == key:
                return curr.value
        return -1

    def remove(self, key: int) -> None:
        if self.get(key) == -1:
            return
        index = key % 10**3
        prev = self.table[index]
        curr = prev.next
        while curr.key != key:
            curr = curr.next
            prev = prev.next
        prev.next = curr.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)