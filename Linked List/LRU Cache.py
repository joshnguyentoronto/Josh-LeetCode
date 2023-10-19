'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.


Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
    LRUCache lRUCache = new LRUCache(2);
    lRUCache.put(1, 1); // cache is {1=1}
    lRUCache.put(2, 2); // cache is {1=1, 2=2}
    lRUCache.get(1);    // return 1
    lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    lRUCache.get(2);    // returns -1 (not found)
    lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    lRUCache.get(1);    // return -1 (not found)
    lRUCache.get(3);    // return 3
    lRUCache.get(4);    // return 4
'''


class Node:
    def __init__(self, key, val, next, prev):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity):
        self.table = {}
        self.cap = capacity
        self.head = Node(0, 0, None, None)
        self.tail = Node(0, 0, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    # remove from list
    def remove(self, node):
        pre, nxt = node.prev, node.next
        pre.next, nxt.prev = nxt, pre

    # insert in the right before tail
    def insert(self, node):
        pre, nxt = self.tail.prev, self.tail
        pre.next = nxt.prev = node
        node.prev, node.next = pre, nxt

    def get(self, key):
        if key in self.table:
            self.remove(self.table[key])
            self.insert(self.table[key])
            return self.table[key].val
        return -1

    def put(self, key, value):
        if key in self.table:
            self.remove(self.table[key])
        self.table[key] = Node(key,value, None, None)
        self.insert(self.table[key])

        if len(self.table) > self.cap:
            lru = self.head.next
            self.remove(lru)
            del self.table[lru.key]
            
                
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)