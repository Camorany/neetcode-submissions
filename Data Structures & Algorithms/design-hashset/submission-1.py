class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.hashSet = [ListNode(0) for i in range(10**4)]
        

    def add(self, key: int) -> None:
        currentNode = self.hashSet[key % len(self.hashSet)]
        
        while currentNode.next:
            if currentNode.next.key == key:
                return
            currentNode = currentNode.next
        currentNode.next = ListNode(key)

    def remove(self, key: int) -> None:
        currentNode = self.hashSet[key % len(self.hashSet)]
        
        while currentNode.next:
            if currentNode.next.key == key:
                currentNode.next = currentNode.next.next
                return
            currentNode = currentNode.next

    def contains(self, key: int) -> bool:
        currentNode = self.hashSet[key % len(self.hashSet)]
        
        while currentNode.next:
            if currentNode.next.key == key:
                return True
            currentNode = currentNode.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)