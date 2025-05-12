"""
keep mru in the tail and lru in the head,
keep dummy head and tail to avoid edge cases
if key exits, remove the node and add new node to the tail
"""


class Node:
    def __init__(self, key, value, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.n_map = {}
        # head for lru, tail for mru
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.count = 0

    def add_node(self, node):
        self.n_map[node.key] = node
        # this is mru
        node.prev = self.tail.prev
        self.tail.prev.next = node
        node.next = self.tail
        self.tail.prev = node
        self.count += 1

    def remove_node(self, node):
        del self.n_map[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        self.count -= 1

    def get(self, key: int) -> int:
        # move the node to the tail
        if key not in self.n_map:
            return -1
        node = self.n_map[key]
        self.remove_node(node)
        self.add_node(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.n_map:
            self.remove_node(self.n_map[key])
        node = Node(key, value)
        self.add_node(node)
        # add pair to the cache while considering capacity
        if self.count > self.capacity:
            lru = self.head.next
            self.remove_node(lru)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
