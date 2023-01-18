#!/usr/bin/env python3
"""
Database query with pymongo
"""


def list_all(mongo_collection):
    """List all documents in a collection"""
    results = mongo_collection.find()
    return results
