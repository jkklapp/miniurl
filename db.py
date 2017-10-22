import redis

class DB():

    def __init__(self, config):
        """
        Open connection to the DB.

        :param config: Configuration depending on the env
        """
        self.r = redis.StrictRedis(host=config['REDIS_HOST'],
                                   port=config['REDIS_PORT'],
                                   db=config['REDIS_DB'])

    def store(self, hash, original_url):
        """
        Persist the shortened url and the original.

        :param hash: String, the hash for the original URL.
        :param original_url: String, the original URL.
        """
        self.r.set(hash, original_url)

    def fetch(self, hash):
        """
        Retrieve the original URL.

        :param hash: String, the hash for the original URL.
        :return: The original URL.
        """
        return self.r.get(hash)
