from typing import Optional, Dict


class CacheNode:

    def __init__(
        self,
        key: int,
        val: int,
        prev: Optional["CacheNode"] = None,
        next: Optional["CacheNode"] = None,
    ):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.head: Optional[CacheNode] = None
        self.tail: Optional[CacheNode] = None
        self.capacity = capacity
        self.nodes_map: Dict[int, CacheNode] = {}

    def __delete_node(self, node: CacheNode):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if self.tail == node:
            self.tail = node.prev

        node.prev = None
        node.next = None

    def __insert_to_head(self, node: CacheNode):
        if self.head:
            node.next = self.head
            self.head.prev = node
        else:
            self.tail = node
        self.head = node

    def get(self, key: int) -> int:
        if key not in self.nodes_map:
            return -1

        node = self.nodes_map[key]
        if node != self.head:
            self.__delete_node(node)
            self.__insert_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.nodes_map:
            node = self.nodes_map[key]
            node.val = value
            self.get(key)
        else:
            node = CacheNode(key, value)
            self.nodes_map[key] = node
            self.__insert_to_head(node)

            if len(self.nodes_map.keys()) > self.capacity and self.tail:
                tail_node = self.tail
                self.tail = tail_node.prev
                del self.nodes_map[tail_node.key]
                self.__delete_node(tail_node)


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(2, 1)
    cache.put(1, 1)
    cache.put(2, 3)
    cache.put(4, 1)
    assert cache.get(1) == -1
    assert cache.get(2) == 3
