"""
Create a hash table from scratch for my own understanding
"""

class HashTable:
    """
    My own implement of a hash table.
    
    attributes:
    table_size -- number of slots in hash table
    keys -- list of keys in hash table
    values -- list of values in hash table
    hash_codes -- list of hash codes in hash table

    methods:
    insert_key_value -- insert key and value into hash table
    retrieve_by_key -- retrieve key and value from hash table

    `insert_key_value`:
    """
    def __init__(self, length):
        assert isinstance(length, int)
        self.table_size = length
        self.hash_codes = [None] * self.table_size
        self.keys = [None] * self.table_size
        self.values = [None] * self.table_size

    def insert_key_value(self, key, value):
        """
        insert a given (key, value) pair into hash table
        """
        hash_code = hash(key)
        insert_pos = hash_code % self.table_size

        while self.keys[insert_pos]:
            # make sure key does not already exist
            if self.hash_codes[insert_pos] == hash_code:
                raise KeyError('key already exists in hash table')
            # iterate 1 position, modulo wraps to beginning of key list
            insert_pos = (insert_pos + 1) % self.table_size
        self.hash_codes[insert_pos] = hash_code
        self.keys[insert_pos] = key
        self.values[insert_pos] = value

    def retrieve_by_key(self, key):
        """
        for a given key, retrieve the corresponding value
        """
        hash_code = hash(key)
        counter = 0
        pos = hash_code % self.table_size
        while self.hash_codes[pos] != hash_code and self.keys[pos] != key:
            # prevent infinite loop
            if counter > self.table_size:
                raise KeyError('key not found in table')
            # iterate 1 position, modulo wraps to beginning of key list
            pos = (pos + 1) % self.table_size
            counter += 1
        return self.keys[pos], self.values[pos]
