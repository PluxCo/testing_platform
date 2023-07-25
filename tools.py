import pickle
import os


class Settings(dict):
    def __init__(self):
        super().__init__()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Settings, cls).__new__(cls)
        return cls.instance

    def setup(self, filename, default_values: dict):
        self.file = filename
        self._update_handlers = []

        for k, v in default_values.items():
            self.setdefault(k, v)

        if not os.path.exists(filename):
            with open(filename, "wb") as file:
                pickle.dump(Settings(), file)

        with open(filename, "rb") as file:
            self.update(pickle.load(file))

    def update_settings(self):
        with open(self.file, "wb") as file:
            pickle.dump(self, file)
        for handler in self._update_handlers:
            handler()

    def add_update_handler(self, handler):
        self._update_handlers.append(handler)
