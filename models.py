import time
from threading import RLock


class SimpleCache(dict):
    def __init__(self):
        super(SimpleCache, self).__init__()
        self.lock = RLock()

    def pop(self, key, default=None):
        """ Get item from the dict and remove it.

        Return default if expired or does not exist. Never raise KeyError.
        """
        with self.lock:
            try:
                item = dict.__getitem__(self, key)
                del self[key]
                return item[0]
            except KeyError:
                return default

    def get(self, key, default=None):
        """ Return the value for key if key is in the dictionary, else default. """
        with self.lock:
            try:
                value, max_age = dict.__getitem__(self, key)
                expired = max_age-time.time() if max_age else None

                if not expired or expired > 0:
                    return value
                else:
                    del self[key]
                    raise KeyError(key)
            except KeyError:
                return default

    def set(self, key, value, ttl=None):
        """ Set key to value. """
        with self.lock:
            max_age = None
            if ttl is not None:
                max_age = time.time() + ttl
            dict.__setitem__(self, key, (value, max_age))

            return value

    def get_all_keys(self):
        """ Return a copy of the dictionary's list of (key, value) pairs. """
        r = []
        with self.lock:
            for key in self.keys():
                if self.get(key):
                    r.append(key)

            return r


