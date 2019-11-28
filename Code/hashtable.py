#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.size = 0

    def __iter__(self):
        """ Returns the iteator object """
        return self.items()
    
    def __next__(self):
        #  while self.items() != None:
        #     item = self.curr.data
        #     self.curr = self.curr.next
        #     return item
        # raise StopIteration
        # pass
        # curr = self.items()[0]
        # for i in self.items():
        #     return i
        # raise StopIteration
        pass
    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(n2) Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        all_values = []
        for bucket in self.buckets:
            for key,value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items
        print(all_items)

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""
        return self.size

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        try:
            self.get(key)
            return True

        except KeyError:
            return False
        
    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        index = self._bucket_index(key)
        ll = self.buckets[index]
        # use find method
        for buck_key, buck_value in ll.items():
            if key is buck_key:
                return buck_value
        raise KeyError('Key not found: {}'.format(key))
        # return False

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        index = self._bucket_index(key)
        ll = self.buckets[index]
        for buck_key, buck_value in ll.items():
            if key is buck_key:
                ll.replace((buck_key,buck_value), (key, value))
                return
        ll.append((key, value))
        self.size += 1
    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        index = self._bucket_index(key)
        ll = self.buckets[index]
        for buck_key, buck_value in ll.items():
            if key is buck_key:
                ll.delete((buck_key,buck_value))
                self.size -= 1
                return
        raise KeyError('Key not found: {}'.format(key))

    def __setitem__(self, key, value):
        self.set(key, value)
    
    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return self.contains(key)
    
    def __len__(self):
        return self.size
    

def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    # test_hash_table()
    ht = HashTable()

    ht['liya'] = 'myself'
    ht['josi'] = 'bro'
    ht['boni'] = 'sis'
    print(ht.items())
    # print(ht)
    # print(ht['liya'])
    # for i in ht.items():
    #     print(i)
    # print(len(ht))
    # print(iter(ht.items()))
    # print(next(ht.items()))
    # if "liya" in ht:
    #     print("Exist!")