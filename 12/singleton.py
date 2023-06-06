# Singleton pattern (single instance of a class)

# Manière 1 (Pas top)
from typing import Any


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            print("Creating instance")
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

# Manière 2 (Pythonic)


class Singleton2(object):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(object):
    __metaclass__ = Singleton2
