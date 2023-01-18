#!/usr/bin/env python3
"""Database query with pymongo """


def insert_school(mongo_collection, **kwargs):
    """Insert new document in mongo_collection"""
    return mongo_collection.insert(kwargs)

