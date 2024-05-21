#!/usr/bin/python3
"""  FIFOcache module that inherite from BaseCaching"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOcache define FIFO cache system"""
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
                oldest_key = self.order.pop(0)
                del self.cache_data[oldest_key]
                print("DISCARD: {}".format(oldest_key))

        self.cache_data[key] = item
        if key not in self.order:
            self.order.append(key)

    def get(self, key):
        """ get item by key"""
        return self.cache_data.get(key, None)
