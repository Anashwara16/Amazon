class DLinkedNode(): 
    
    def init(self): 
        self.key = self.value = 0
        self.prev = self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def addNode(self, node):
        node.prev = self.head
        node.next = self.head.next 
        self.head.next.prev = node
        self.head.next = node
        
    def removeNode(self, node):
        prev = node.prev 
        curr = node.next
        prev.next = curr
        curr.prev = prev
        
    def moveToHead(self, node): 
        self.removeNode(node)
        self.addNode(node)
        
    def popTail(self):
        res = self.tail.prev
        self.removeNode(res)
        return res
        
    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node: 
            return -1
        self.moveToHead(node)
        return node.value
        
    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        
        if not node: 
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value
            
            self.cache[key] = newNode
            self.addNode(newNode)
            self.size += 1
            
            if self.size > self.capacity: 
                tail = self.popTail()
                del self.cache[tail.key]
                self.size -= 1
            
        else: 
            node.value = value
            self.moveToHead(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



    

