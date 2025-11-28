class SuppressAndLog:
    def __init__(self, *exc_types):
        self.exc_types = exc_types

    def __enter__(self):
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            return False
        if any(issubclass(exc_type, t) for t in self.exc_types):
            print(f"Suppressed {exc_type.__name__}: {exc_val}")
            return True
        return False