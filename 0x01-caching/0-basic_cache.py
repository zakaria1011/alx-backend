#!/usr/bin/python3
""" BasicCache module that inherits from BadicCaching"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache define caching system whitout limite"""

    def put(self, key, item):
        """ add an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
