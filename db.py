import redis

def store(hash, original_url):
    """
    Persist the shortened url and the original.

    :param hash: String, the hash for the original URL.
    :param original_url: String, the original URL.
    """
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.set(hash, original_url)

def fetch(hash):
    """
    Retrieve the original URL.

    :param hash: String, the hash for the original URL.
    :return: The original URL.
    """
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.get(hash)
