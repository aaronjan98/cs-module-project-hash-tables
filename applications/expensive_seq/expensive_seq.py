cache = {}


def expensive_seq(x, y, z):

    # packaging vars as tuple
    firstkey = (x, y, z)

    def add_to_cache(key):
        # If that key result doesn't exist run the operation
        # and add to cache
        if key not in cache:
            cache[key] = inner_expensive_seq(key)

    def inner_expensive_seq(key):
        if key not in cache:

            # For readability unpack the tuple
            x = key[0]
            y = key[1]
            z = key[2]

            if x <= 0:
                cache[key] = y + z

            if x > 0:
                newkey1 = (x-1, y+1, z)
                newkey2 = (x-2, y+2, z*2)
                newkey3 = (x-3, y+3, z*3)

                add_to_cache(newkey3)
                add_to_cache(newkey2)
                add_to_cache(newkey1)

                result1 = cache[newkey1]
                result2 = cache[newkey2]
                result3 = cache[newkey3]

                cache[key] = result1+result2+result3

        return cache[key]

    return inner_expensive_seq(firstkey)

'''
cache = {}

def expensive_seq(x, y, z):
    global cache
    # Base case, recursive call breaks when x is <= 0
    if x <= 0:
        return y + z
    # if key is found in cache return the value
    elif (x, y, z) in cache.get(x, y, z):
        return cache.get((x, y, z))
    else:
        # we can go ahead and save our answer to the cache 
        append_to_cache = expensive_seq(x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)
        cache.update({(x, y, z): append_to_cache})
    return cache[(x, y, z)]
'''

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
