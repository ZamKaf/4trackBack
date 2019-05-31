from werkzeug.contrib.cache import MemcachedCache
cache = MemcachedCache(['127.0.0.1:11211'])

def get_cache_hello():
    rv = cache.get('hello')
    if rv is None:
        print('SET CACHE')
        rv = 'World'
        cache.set('hello', rv, timeout=5*60)
    return  rv

def just4test():
    print(get_cache_hello())