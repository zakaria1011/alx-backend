#!/usr/bin/python3
""" LRUcache mudule that inherite from BaseCaching"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache define a caching system """
    def __init__(self):
        """ initialization"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ add an item to the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD: {}".format(lru_key))

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
