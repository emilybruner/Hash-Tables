class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__ (self, capacity):
        self.capacity = capacity #num of buckets in hash table
        self.storage = [None] * capacity
        self.elements = 0

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for i in key:
            hash = (hash * 33) + ord(i)
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def load_factor(self):
        return self.elements / self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        #make new entry variable
        # use the hash index function to find the bucket
        index = self.hash_index(key)
        existing_entry = self.storage[index]
        new_entry = HashTableEntry(key, value)

        # Check to see if that hash index exists:
        if existing_entry:
            last_entry = None
            # Look through this hash index list
            while existing_entry:
                # Search list for key
                if existing_entry.key == key:
                    # Found an existing key, can replace the value
                    existing_entry.value = value
                    return
                # Continue looking through list until None
                last_entry = existing_entry
                existing_entry = existing_entry.next
            # Did not find existing key, add to end of this hash index list
            last_entry.next = new_entry
            self.elements += 1
            # Automatically resize by double if load factor is greater than .7
            if self.load_factor() > 0.7:
                self.resize(self.capacity * 2)

        # If hash index doesn't exists, can add new entry in that spot
        else:
            self.storage[index] = new_entry
            self.elements += 1
            # Automatically resize by double if load factor is greater than .7
            if self.load_factor() > 0.7:
                self.resize(self.capacity * 2)


        
    #     if node is not None:
    #         prev = None
    #         while node is not None:
    #             if node.key == key:
    #                 node.value = value
    #                 return
    #             #assign current node to prev
    #             prev = node
    #             #next node is assigned to current node
    #             node = node.next
    #         prev.next = new_node
    #         self.entry_count += 1
    #         #after adding an item, check the load count and resize depending on the result
    #         if self.load_factor() > .7:
    #             self.resize(self.capacity)
    #     # if node doesn't exist create new node and insert into the hash table
    #     else:
    #         self.storage[index] = new_node
    #         self.entry_count += 1
    #     #after adding an item, check the load count and based on the conditions
    #     if self.load_factor() > 0.7:
    #         self.resize(self.capacity)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.storage[index]
        prev = None
        # while the node exists and the keys do not match, go through the linked list
        while node is not None and node.key != key:
            prev = node
            node = node.next
        #if node does not exist, give a warning 
        if node is None:
            print("Warning: key not found")
        #otherwise, if node exists with no other conditions required
        else:
            if prev is None:
                self.storage[index] = node.next
            else:
                prev.next = node.next
        self.elements -= 1

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.storage[index]

        while node is not None:
            if node.key == key:
                return node.value
            else:
                node = node.next
        return None

    def resize(self, new_capacity):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        #get old hash table
        prev_storage = self.storage
        # expand new table capacity
        self.capacity = new_capacity
        # create a new hash table with expanded capacity
        self.storage = [None] * new_capacity 
        # loop over the old hash table checking for values, if they exist rehash and readd them
        for i in range(len(prev_storage)):
            #check previous storage at index i
            existing_entry = prev_storage[i]
            
            #if hash index exists
            if existing_entry:
                #look through this hash index list
                while existing_entry:
                    if existing_entry.key:
                        #if found, rehash to new storage
                        self.put(existing_entry.key, existing_entry.value)
                        #continue looking through list until none
                        existing_entry = existing_entry.next

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
