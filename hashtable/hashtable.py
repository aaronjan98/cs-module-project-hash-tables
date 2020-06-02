class LinkedList:
    def __init__(self, HashTableEntry=None):
        self.head = HashTableEntry
        self.tail = HashTableEntry

    def __repr__(self):
        return f'{repr(self.head)}'

    def insert(self, HashTableEntry):
        new_entry = HashTableEntry
        if self.head is None:
            self.head = new_entry
            self.tail = new_entry
        elif self.contains(HashTableEntry.key) is not False:
            current = self.head
            while current is not None:
                if current.key == HashTableEntry.key:
                    # print(f"CKey: {current.key}, HKey: {HashTableEntry.key}")
                    # print(
                    #     f"CValue:{current.value} HValue: {HashTableEntry.value}")
                    current.value = HashTableEntry.value
                    break
                else:
                    current = current.next
        else:
            self.tail.next = new_entry
            self.tail = new_entry

    def contains(self, key):
        current = self.head
        while current is not None:
            if current.key == key:
                return current.value
            else:
                current = current.next
        return False

    def remove(self, key):
        if self.head.key == key:
            # victum = self.head
            self.head = self.head.next
            # victum.next = None
        else:
            current = self.head
            prev = None
            while current is not None:
                if current.key == key:
                    # print(current.key)
                    prev.next = current.next
                    current.next = None
                    return current.value
                prev = current
                current = current.next
            return False
# todo research garbage cleanup


class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f'{repr(self.key)}'
        # , {repr(self.value)})


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        self.capacity = capacity
        if self.capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
        self.table = [None for _ in range(capacity)]
        self.count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.table)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        number of things stored in hash table / num of slots in array
        """
        # Your code here
        return self.count/len(self.table)

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # hash = offset_basis
        # for each piece_of_data to be hashed:
        #     hash = hash * FNV_prime
        #     hash = hash xor piece_of_data
        # return hash
        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # self.table[self.hash_index(key)] = HashTableEntry(key, value)
        # Your code here
        slot, entry = self.table[self.hash_index(
            key)], HashTableEntry(key, value)
        self.count += 1
        if slot is None:
            self.table[self.hash_index(
                key)] = LinkedList(entry)
        else:
            slot.insert(entry)
        # print({slot}, self.table)
        if self.get_load_factor() > 0.7:
            print(
                f"{key} LF: {self.get_load_factor()}")
            self.resize(self.capacity*2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # if not self.get(key):
        #     print(f'{key} was not found.')
        # else:
        #     self.put(key, None)
        # Your code here
        slot = self.table[self.hash_index(key)]
        if slot and slot.contains(key) is not False:
            print(self.table)
            self.count -= 1
            slot.remove(key)
        else:
            return False

        if self.get_load_factor() < 0.2:
            print(f"{key} LF: {self.get_load_factor()}")
            self.resize(int(self.capacity/2))

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # hash_entry = self.table[self.hash_index(key)]
        # if hash_entry is not None:
        #     return hash_entry.value
        # return None
        # Your code here
        slot = self.table[self.hash_index(key)]
        if slot and slot.contains(key) is not False:
            return slot.contains(key)
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # if new_capacity < MIN_CAPACITY:
        #     new_capacity = MIN_CAPACITY

        # self.capacity = new_capacity
        # new_table = [None for _ in range(self.capacity)]
        # for i in range(len(self.table)):
        # print(i)
        #     if(self.table[i]):
        #         key, value = self.table[i].key, self.table[i].value
        #         slot = self.hash_index(key)
        #         new_table[slot] = HashTableEntry(key, value)
        # self.table = new_table
        # Your code here
        if new_capacity < MIN_CAPACITY:
            new_capacity = MIN_CAPACITY
        self.capacity = new_capacity
        new_table = [None for _ in range(self.capacity)]
        self.count = 0
        for i in range(len(self.table)):
            if self.table[i] is not None:
                cur = self.table[i].head
                while cur is not None:
                    slot = new_table[self.hash_index(cur.key)]
                    self.count += 1
                    if slot is None:
                        new_table[self.hash_index(
                            cur.key)] = LinkedList(cur)
                        cur = cur.next
                    else:
                        slot.insert(cur)
                        cur = cur.next
        self.table = new_table

        # for index in previous hashtable
        # pop off tails until it is empty and run a hashing function and insert into new list
        # delete old list


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")
    ht.put("line_13", "And stood test awhile in thought.")

    # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(i, ht.get(f"line_{i}"))
    # print(ht.table)
    # # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")
    print(ht.table)
    # Test if data intact after resizing
    for i in range(1, 13):
        print(i, ht.get(f"line_{i}"))
    # print(ht.get("line_9"))
