#!/usr/bin/env python3
"""Python file to test redis"""
import redis

Class Cache():
    """Redis in Python script"""
    def __init__(self):
        _redis = redis.Redis()
        _redis.flushdb

    def store(data: Union[str, bytes, int, float]) -> str:
        """
        Stores data with random uuid
        """
        pass
