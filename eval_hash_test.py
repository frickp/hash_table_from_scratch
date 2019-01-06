"""
Tests for custom hash table
"""

import pytest
from hash_table import HashTable

class TestClass:
    """
    Tests for hash table
    """
    def test_insertion_retrieval(self):
        """
        insert and retrieve 5 elements. Ensure key matches values
        """
        h = HashTable(10)
        h.insert_key_value('dog', 'woof')
        h.insert_key_value('cat', 'meow')
        h.insert_key_value('bird', 'tweet')
        h.insert_key_value('lion', 'roar')
        h.insert_key_value('snake', 'hiss')
        noises = []

        for key in ['dog', 'cat', 'bird', 'lion', 'snake']:
            noises.append(h.retrieve_by_key(key)[1])

        assert noises == ['woof', 'meow', 'tweet', 'roar', 'hiss']

    def test_reject_duplicate_keys(self):
        """
        Make sure identical keys are not inserted
        """
        h = HashTable(10)
        with pytest.raises(KeyError):
            h.insert_key_value('flower', 'petal')
            h.insert_key_value('flower', 'stem')


# content of test_sysexit.py


#def f():
#    raise SystemExit(1)


#def test_mytest():
#    with pytest.raises(SystemExit):
#        f()


#thing = h.retrieve_by_key('cat')
"""
print(h.retrieve_by_key('dog'))
print(h.retrieve_by_key('cat'))
print(h.retrieve_by_key('bird'))
print(h.retrieve_by_key('lion'))
print(h.retrieve_by_key('snake'))
"""
