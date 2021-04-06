# encoding: utf-8
# @author: fengr358
# @time: 2021/3/7 22:10
# @desc: python dict 底层实现

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash_function(self, key, size):
        return key % size

    def hash_re_function(self, old_hash, size):
        return (old_hash + 1) % size

    def put(self, key, data):
        hash_value = self.hash_function(key, self.size)
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                # 替换
                self.data[hash_value] = data
            else:
                # 再散列
                re_hash = self.hash_re_function(hash_value, self.size)
                while self.slots[re_hash] is not None and self.slots[re_hash] != key:
                    re_hash = self.hash_re_function(re_hash, self.size)
                if self.slots[re_hash] is None:
                    self.slots[re_hash] = key
                    self.data[re_hash] = data
                else:
                    self.data[re_hash] = data

    def get(self, key):
        hash_value = self.hash_function(key, self.size)
        if self.slots[hash_value] is None:
            return None
        else:
            if self.slots[hash_value] == key:
                return self.data[hash_value]
            else:
                re_hash = self.hash_re_function(hash_value, self.size)
                while self.slots[re_hash] is not None and self.slots[re_hash] != key:
                    re_hash = self.hash_re_function(re_hash, self.size)
                if self.slots[re_hash] is None:
                    return None
                else:
                    return self.data[re_hash]