#!/usr/bin/python3
""" LFUCache module that inherits from BaseCaching """

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """ LFUCache defines an LFU caching system """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.frequency = defaultdict(int)
        self.usage_order = []

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.frequency.values())
                lfu_keys = [k for k, v in self.frequency.items()
                            if v == min_freq]

                if len(lfu_keys) > 1:
                    lfu_key = next(k for k in self.usage_order
                                   if k in lfu_keys)
                else:
                    lfu_key = lfu_keys[0]

                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                self.usage_order.remove(lfu_key)
                print("DISCARD: {}".format(lfu_key))

            self.cache_data[key] = item
            self.frequency[key] = 1

        if key in self.usage_order:
            self.usage_order.remove(key)
        self.usage_order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
