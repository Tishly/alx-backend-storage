#!/usr/bin/env python3
"""
Database query with pymongo
"""


def list_all(mongo_collection):
    """List all documents in a collection"""
    results = mongo_collection.find()

    """count = 0
    for doc in results:
        count = 1
        if count == 0:
            return []
            """

    return results
