#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    newHashTable = HashTable(length)

    for item in tickets:
        newHashTable.put(item.source, item)
    
    route = []

    currentValue = newHashTable.get("NONE")

    return route

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity, table = 0):
        self.capacity = capacity
        self.table = [None] * self.capacity

    def djb2(self, key):
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash
    
    def hash_index(self, key):
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        index = self.hash_index(key)

        if (self.table[index] is None):
            self.table[index] = HashTableEntry(key, value)
        elif (self.table[index].next is None):
            self.table[index].next = HashTableEntry(key, value)
        else:
            node = self.table[index]
            while (node.next is not None):
                node = self.table[index].next
            node.next = HashTableEntry(key, value)

    def get(self, key):
        index = self.hash_index(key)
        cur = self.table[index]

        while cur is not None:
            if cur.key == key:
                return cur.value
            cur = cur.next