#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#

# @lc code=start
class ListNode:
    def __init__(self, key=0, val=0):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = ListNode(key, value)
            self.addToHead(node)
            self.size += 1
            self.cache[key] = node
            while self.size > self.capacity:
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.val = value
            self.moveToHead(node)
        
    def moveToHead(self, node: ListNode) -> None:
        self.removeNode(node)
        self.addToHead(node)
    
    def removeNode(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def addToHead(self, node: ListNode) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def removeTail(self) -> ListNode:
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev
        return node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

