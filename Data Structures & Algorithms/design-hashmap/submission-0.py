class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hashmap = [ListNode(0,0) for i in range(10**4)]
        

    def put(self, key: int, value: int) -> None:
        currentNode = self.hashmap[key % len(self.hashmap)]

        while currentNode.next:
            if currentNode.next.key == key:
                currentNode.next.value = value
                return
            currentNode = currentNode.next
        
        currentNode.next = ListNode(key, value)

    def get(self, key: int) -> int:
        currentNode = self.hashmap[key % len(self.hashmap)]

        while currentNode.next:
            if currentNode.next.key == key:
                return currentNode.next.value
            currentNode = currentNode.next
        
        return -1

    def remove(self, key: int) -> None:
        currentNode = self.hashmap[key % len(self.hashmap)]

        while currentNode.next:
            if currentNode.next.key == key:
                currentNode.next = currentNode.next.next
                return
            currentNode = currentNode.next
            

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)