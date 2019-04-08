import collections


class LRUCache:
    def __init__(self, limit=10):
        self.limit = limit
        self.cache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self.cache.pop(key)
            return value
        except KeyError:
            return None

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.limit:
                self.cache.popitem(last=False)
        self.cache[key] = value


# cache = LRUCache()
# cache.set('one', 1)
# print(cache.get('one'), 'first test')
# print('one' in cache.cache)
# print(cache.get('one'), 'second test')
# print(cache.get('two'), 'this does not exist')
