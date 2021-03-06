# This is the HashTable Class

class HashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=41):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table.
    ''' 
    #Original
    def insert(self, item):
        # get the bucket list where this item will go.
        bucket = hash(item) % len(self.table)
        bucket_list = self.table[bucket]

        # insert the item to the end of the bucket list.
        bucket_list.append(item)
    '''

    #This function allows objects to be inserted and updated in the hash table

    def insert(self, key, item):  # does both insert and update. Time complexity is O(1)
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    '''
        # Original
        def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        print(bucket_list)

        # search for the key in the bucket list
        if key in bucket_list:
            # find the item's index and return the item that is in the bucket list.
            item_index = bucket_list.index(key)
            return bucket_list[item_index]
        else:
            # the key is not found.
            return None
    '''

    # This function searches for items in the hash table based on the item's key

    def search(self, key):
        # get the bucket list where this key would be. Time complexity is O(N)
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket_list)

        # search for the key in the bucket list
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                return kv[1]  # value
        return None

    # Removes an item with matching key from the hash table.
    '''
        def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        if key in bucket_list:
            bucket_list.remove(key)
    '''

    # Function removes items from the hash table based on an item's key

    def remove(self, key):
        # get the bucket list where this item will be removed from.  Time complexity is O(1)
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # removes the item from the bucket list if it is present.
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])