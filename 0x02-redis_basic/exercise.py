#!/usr/bin/env python3
"""Python file to test redis"""
import redis
import uuid
from typing import Union


Class Cache():
    """Redis in Python script"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random key, store the input data in Redis using the
        random key and return the key"""
        key = uuid.uuid5(data)
        return key
