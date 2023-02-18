#!/usr/bin/env python3
"""Python file to test redis"""
import redis
import uuid
from typing import Union, Optional


class Cache():
    """Redis in Python script"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: (Union[str, bytes, int, float])) -> str:
        """
        Generates a random key, store the input data in Redis using the
        random key and return the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, int, bytes, float]:
        """Takes string and converts to desired format"""
        data = self._redis.get(key)
        if fn:
            value = fn(data)
            return data

    def get_str(self, key: str) -> Union[str, None]:
        """Gets a string from the cache"""
        return self._redis.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, None]:
        """ Get int from the cache"""
        data = self._redis.get(key)
        try:
            data =int(data.decode('utf-8'))
        except Exception:
            data = 0
        return data
