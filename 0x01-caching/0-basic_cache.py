#!/usr/bin/env python3

'''Task 0: Basic dictionary BasicCache
'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''A class `BasicCache` that is a caching system
    '''

    def put(self, key, item):
        '''assign to the dictionary `self.cache_data`
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''return the value in self.cache_data'''

        return self.cache_data.get(key, None)
