# simple cache

cache = {}

def getPage(url):
    if cache.get(url):
        print('using the cache')
        return cache[url]
    else:
        print('getting the data')
        data = "Some data for " + url
        cache[url] = data
        return data
        
        
print(getPage('google.com'))
print(getPage('facebook.com'))
print(getPage('yhat.com'))
print(getPage('google.com'))