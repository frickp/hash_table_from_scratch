"""
Try using custom hash table
"""
from hash_table import HashTable

h = HashTable(10)

h.insert_key('dog', 'woof')
h.insert_key('cat', 'meow')
h.insert_key('bird', 'tweet')
h.insert_key('lion', 'roar')
h.insert_key('snake', 'hiss')

print(h.retrieve_by_key('dog'))
print(h.retrieve_by_key('cat'))
print(h.retrieve_by_key('bird'))
print(h.retrieve_by_key('lion'))
print(h.retrieve_by_key('snake'))
