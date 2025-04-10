# 【20分钟内】设计实现一个简单的LRU Cache实现
# LRU Cache: 容量受限的Cache， 最久被访问的元素首先被淘汰。
# 结果主要评估：
# 1. put时间复杂度 （建议O（1）实现）
# 2. get时间复杂度 （建议O（1）实现）
# 3.del时间复杂度 （建议O（1）实现）
class List:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = List()
        self.tail = List()
        self.head.next = self.tail
        self.tail.next = self.head

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        return node.value

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = self.head
            node.next = self.head.next

            self.head.next.prev = node
            self.head.next = node

        else:
            node = List(key, value)
            self.cache[key] = node

            node.prev = self.head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            if len(self.cche) > self.capacity:

                removed = self.tail.prev
                removed.prev.next = remove.next
                removed.next.prev = removed.prev

                del self.cache[removed.key]


if __name__ == '__main__':
    lru = LRUCache(3)
    lru.put(1, 1)
    lru.put(2, 2)
    lru.put(3, 3)
    print(lru.get(1))
    lru.put(4, 4)
    print(lru.get(2))
    print(lru.get(3))
    print(lru.get(4))





