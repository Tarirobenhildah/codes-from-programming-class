class CacheManager:
    _STORAGE = {}

    def __init__(self, key):
        self.key = key
        self._local = None

    def __enter__(self):
        if self.key in CacheManager._STORAGE:
            return CacheManager._STORAGE[self.key]
        self._local = {}
        return self._local

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None and self._local is not None:
            CacheManager._STORAGE[self.key] = self._local
        return False
    