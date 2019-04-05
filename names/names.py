import time
from lru_cache import LRUCache

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

cache = LRUCache(20000)

duplicates = []


def duplicatesfinder(names_1, names_2):
    names_1 = list(set(names_1))
    names_2 = list(set(names_2))
    namesets = names_1 + names_2
    for name in namesets:
        if name in cache.cache:
            print(name)
            duplicatename = cache.get(name)
            duplicates.append(duplicatename)
        else:
            cache.set(name, name)


duplicatesfinder(names_1, names_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
