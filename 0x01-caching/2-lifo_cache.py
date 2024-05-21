#!/usr/bin/python3
"""  LIFOcache module that inherite from BaseCaching"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOcache define LIFO cache system"""
    def __init__(self):
        """ initialisation"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ add an item to cache"""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = self.order.pop()
                del self.cache_data[last_key]
                print("DISCARD: {}".format(last_key))

        self.cache_data[key] = item
        if key not in self.order:
            self.order.append(key)
        else:
            self.order.remove(key)
            self.order.append(key)


    def get(self, key):
        """ get item by key"""
        return self.cache_data.get(key, None)
