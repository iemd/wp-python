# Build a Hash Table

class HashTable:
    def __init__(self):
        self.collection = {}
    
    def hash(self, key):
        hashed = 0;
        for char in key:
            hashed += ord(char) 
        return hashed

    def add(self, key, value):
        hashed = self.hash(key)
        if hashed in self.collection:
            self.collection[hashed].update({key: value})
        else:
            self.collection[hashed] = {key: value}

    def remove(self, key):
        hashed = self.hash(key)
        if hashed in self.collection:
            self.collection[hashed].pop(key, None)

    def lookup(self, key):
        hashed = self.hash(key)
        if hashed in self.collection:
            return self.collection[hashed].pop(key, None)

hashtable = HashTable()
hashtable.add('golf', 'sport')
print(hashtable.collection)

hashtable.add('dear', 'friend')
hashtable.add('read', 'book')
print(hashtable.collection)

hashtable.remove('dear')
print(hashtable.collection)

print(hashtable.lookup('golf'))
