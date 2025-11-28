class TransactionalSaver:
    def __init__(self, obj):
        self.obj = obj
        self._original_state = {}

    def __enter__(self):
        self._original_state = dict(self.obj.__dict__)
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.obj.__dict__.clear()
            self.obj.__dict__.update(self._original_state)
            return False
        return False
    




