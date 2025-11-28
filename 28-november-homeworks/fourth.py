class MockAttributes:
    def __init__(self, obj, **mocks):
        self.obj = obj
        self.mocks = mocks
        self._originals = {}

    def __enter__(self):
        for attr, value in self.mocks.items():
            if hasattr(self.obj, attr):
                self._originals[attr] = (True, getattr(self.obj, attr))
            else:
                self._originals[attr] = (False, None)
            setattr(self.obj, attr, value)
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        for attr, (existed, old_value) in self._originals.items():
            if existed:
                setattr(self.obj, attr, old_value)
            else:
                delattr(self.obj, attr)
        return False